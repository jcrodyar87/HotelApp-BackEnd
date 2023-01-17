from datetime import datetime, timedelta
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import hashlib
from config.database import SessionLocal, engine
import schemas, models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/auth",tags=["Authentication"],responses={404:{"message":"No encontrado"}})

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "344cd505052803822360339a8f20c5ab592345efd15caa51d62b4464c1b0a377"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def generate_token(token):
    hash_object = hashlib.sha256(token.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return str(hex_dig)

def get_user(db, username: str):
    user = db.query(models.User).filter_by(username=username).first()
    if not user:
        return False
    return user

def authenticate_user(username: str, password: str, db: Session=Depends(get_db)):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme),  db: Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = db.query(models.User).filter_by(username=username).first()
        if user is None:
            raise HTTPException(status_code=404, detail="No se ha encontrado al usuario")
    except JWTError:
        raise credentials_exception
    return user

#async def get_current_active_user(current_user: User = Depends(get_current_user)):
#    if current_user.status == 0:
#        raise HTTPException(status_code=400, detail="Inactive user")
#    return current_user

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me/",response_model=schemas.UserWithRole, response_model_exclude={'password'})
async def read_current_user(user: schemas.UserWithRole = Depends(get_current_user)):
    return  user

@router.post("/recovery-password/")
async def recovery_password(user_params: schemas.UserAuth, db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(username=user_params.username).first()
    if user is None:
        raise HTTPException(status_code=400, detail="No existe un usuario con ese email")
    else:
        user.token = generate_token(user.username)
        db.commit()
        db.refresh(user)
        raise HTTPException(status_code=200, detail="Se ha enviado un email para que puedas recuperar tu contraseña")
    
@router.post("/change-password/")
async def change_password(user_params: schemas.UserNewPassword, db: Session=Depends(get_db)):
    user = db.query(models.User).filter_by(token=user_params.token).first()
    if user is None:
        raise HTTPException(status_code=400, detail="No se ha cambiado la contraseña")
    else:
        user.password = get_password_hash(user_params.password)
        user.token = None
        db.commit()
        db.refresh(user)
        raise HTTPException(status_code=200, detail="Se ha cambiado la contraseña exitosamente")
    
@router.post("/",response_model=schemas.User, response_model_exclude={'password'})
async def create_user(user_params: schemas.User, db: Session=Depends(get_db)):
    user = models.User(
        username = user_params.username,
        firstname = user_params.firstname,
        lastname = user_params.lastname,
        password = get_password_hash(user_params.password),
        status = user_params.status,
        role_id = user_params.role_id
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user