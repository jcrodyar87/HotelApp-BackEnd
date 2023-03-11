-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: hotelapp
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounting_document`
--

DROP TABLE IF EXISTS `accounting_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounting_document` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `client_number` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `client_name` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `client_address` varchar(300) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `issue_date` date DEFAULT NULL,
  `type` int DEFAULT NULL,
  `currency_type` int DEFAULT NULL,
  `total_sale` decimal(10,0) DEFAULT NULL,
  `tax` decimal(10,0) DEFAULT NULL,
  `total` decimal(10,0) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `reservation_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_id` (`reservation_id`),
  KEY `ix_accounting_document_id` (`id`),
  CONSTRAINT `accounting_document_ibfk_1` FOREIGN KEY (`reservation_id`) REFERENCES `reservation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounting_document`
--

LOCK TABLES `accounting_document` WRITE;
/*!40000 ALTER TABLE `accounting_document` DISABLE KEYS */;
INSERT INTO `accounting_document` VALUES (1,'F001-1','20448544801','ORELLANA VIAJES S.A.C.','Calle Nisperos 344','2023-02-19',1,1,123,27,150,1,1,'2023-02-08 01:41:29','2023-02-12 23:03:31'),(2,'F001-2','1044854480','LOS VIAJES S.A.C','NISPEROS','2023-02-11',0,0,0,8,0,1,8,'2023-02-11 15:22:46','2023-02-11 15:22:46'),(3,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 17:52:17','2023-02-12 17:52:17'),(4,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 17:53:36','2023-02-12 17:53:36'),(5,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 17:55:29','2023-02-12 17:55:29'),(6,'F1-16','44854480','LAS UILISE','CALLE PORTAL 44','2023-02-10',1,1,160,8,173,1,9,'2023-02-12 17:57:03','2023-02-17 14:56:53'),(7,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 18:03:02','2023-02-12 18:03:02'),(8,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 18:05:21','2023-02-12 18:05:21'),(9,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 18:11:01','2023-02-12 18:11:01'),(11,'','','','','2023-02-12',0,0,0,8,0,1,NULL,'2023-02-12 18:28:04','2023-02-12 18:28:04'),(12,'','','','','2023-02-10',0,0,0,8,0,1,12,'2023-02-12 18:36:50','2023-02-25 04:54:26'),(13,'F001-18','5555','FRT','ASDD','2023-02-11',1,0,160,8,173,1,NULL,'2023-02-12 18:40:42','2023-02-17 14:46:32'),(14,'F1-20','44854480','JU','CALLE LOS CALES','2023-02-17',1,1,160,18,189,1,11,'2023-02-17 14:53:02','2023-02-17 14:53:02'),(15,'F1-18','44854480','LOS VIAJES','CALLE LOS OLIVOS','2023-02-18',1,1,150,18,177,1,10,'2023-02-18 16:35:21','2023-02-18 16:35:21'),(16,'F01-17','44854489','TRAVEL SAC','CALLE VIVA 123','2023-03-04',1,1,170,31,201,1,17,'2023-03-04 16:02:11','2023-03-04 16:02:11'),(17,'F1-25','44678890','ORELLANA SAC','CALLE ORTIZ 678','2023-03-04',1,1,190,34,224,1,18,'2023-03-04 16:04:05','2023-03-04 16:04:05'),(18,'F1-25','44567890','RAYI SCA','CALLE PORTALES','2023-03-04',1,1,180,32,212,1,25,'2023-03-04 23:29:33','2023-03-04 23:29:33'),(19,'','','','','2023-03-10',0,0,0,0,0,1,27,'2023-03-10 22:37:30','2023-03-10 22:37:30'),(20,'F1-028','10448045674','LOS VIAJES SA','CALLE LOS ARTEAGAS 234','2023-03-10',1,1,150,27,177,1,23,'2023-03-10 22:48:08','2023-03-10 22:48:08');
/*!40000 ALTER TABLE `accounting_document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `document` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reservations_quantity` int DEFAULT '0',
  `last_reservation` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  KEY `ix_client_id` (`id`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'María Veronica','Castro','44808956','966733612','maria@gmail.com',0,'2023-01-24 17:09:20',1,37,'2023-01-24 17:09:20','2023-02-13 19:03:21'),(2,'Catalina','Castro','44808956','966733612','maria@gmail.com',6,'2023-03-04 22:23:37',1,37,'2023-01-24 17:12:29','2023-03-04 04:25:58'),(3,'Laura','García','09808071','966713689','laura@gmail.com',6,'2023-03-04 22:16:55',1,40,'2023-01-24 17:13:26','2023-01-24 17:13:26'),(4,'Raul','Martinez','08127890','909789611','raul@gmail.com',3,'2023-03-04 22:24:45',1,40,'2023-01-28 02:22:23','2023-01-28 02:22:23'),(5,'Carlos','Ugarte','44564890','909089678','carlos@gmail.com',3,'2023-03-10 22:48:08',1,40,'2023-01-28 02:23:07','2023-01-28 02:23:07'),(6,'Pedro','Orellana','44117890','909789609','pedroorell@gmail.com',0,'2023-01-28 02:24:42',1,40,'2023-01-28 02:24:42','2023-01-28 02:24:42'),(8,'Maria','Bellido','44854478','956789012','mariabell@gmail.com',2,'2023-03-04 23:29:33',1,40,'2023-02-13 19:16:04','2023-03-04 22:24:11'),(9,'Mariano','Torres','44567890','945678923','mario@gmail.com',0,'2023-03-01 15:52:12',1,9,'2023-03-01 15:52:12','2023-03-04 22:24:22'),(10,'Romulo','Rivas','44567890','966788787','romulo@gmail.com',0,'2023-03-01 19:25:47',3,50,'2023-03-01 19:25:47','2023-03-01 19:25:47'),(11,'Hugo','Figueroa','44678800','974232244','hugoortiz@gmail.com',2,'2023-03-10 22:37:30',0,157,'2023-03-04 23:17:40','2023-03-04 23:20:18');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `closed_schedule`
--

DROP TABLE IF EXISTS `closed_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `closed_schedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `description` varchar(350) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int DEFAULT NULL,
  `room_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_id` (`room_id`),
  KEY `ix_closed_schedule_id` (`id`),
  CONSTRAINT `closed_schedule_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `closed_schedule`
--

LOCK TABLES `closed_schedule` WRITE;
/*!40000 ALTER TABLE `closed_schedule` DISABLE KEYS */;
INSERT INTO `closed_schedule` VALUES (1,'2023-02-15','2023-02-15','San Valentin',1,1,'2023-02-12 17:07:33','2023-02-12 17:10:16'),(2,'2023-02-21','2023-02-21','Huelga',1,2,'2023-02-12 17:10:21','2023-02-12 17:11:54'),(3,'2023-02-15','2023-02-15','San Valentin',1,2,'2023-02-12 17:29:54','2023-02-12 17:29:54'),(4,'2023-02-15','2023-02-15','San Valentin',1,3,'2023-02-12 17:29:58','2023-02-12 17:29:58'),(5,'2023-02-15','2023-02-15','San Valentin',1,4,'2023-02-12 17:30:01','2023-02-12 17:30:01'),(6,'2023-02-15','2023-02-15','San Valentin',1,5,'2023-02-12 17:30:05','2023-02-12 17:30:05'),(7,'2023-02-15','2023-02-15','San Valentin',1,6,'2023-02-12 17:30:08','2023-02-12 17:30:08'),(8,'2023-02-15','2023-02-15','San Valentin',1,7,'2023-02-12 17:30:10','2023-02-12 17:30:10'),(9,'2023-02-15','2023-02-15','San Valentin',1,8,'2023-02-12 17:30:13','2023-02-12 17:30:13'),(10,'2023-02-15','2023-02-15','San Valentin',1,9,'2023-02-12 17:30:15','2023-02-12 17:30:15'),(11,'2023-02-15','2023-02-15','San Valentin',1,10,'2023-02-12 17:30:18','2023-02-12 17:30:18'),(12,'2023-02-21','2023-02-21','Huelga',1,1,'2023-02-12 17:36:49','2023-02-12 17:36:49'),(13,'2023-02-21','2023-02-21','Huelga',1,3,'2023-02-12 17:36:52','2023-02-12 17:36:52'),(14,'2023-02-21','2023-02-21','Huelga',1,4,'2023-02-12 17:36:55','2023-02-12 17:36:55'),(15,'2023-02-21','2023-02-21','Huelga',1,5,'2023-02-12 17:36:58','2023-02-12 17:36:58'),(16,'2023-02-21','2023-02-21','Huelga',1,6,'2023-02-12 17:37:00','2023-02-12 17:37:00'),(17,'2023-02-21','2023-02-21','Huelga',1,7,'2023-02-12 17:37:03','2023-02-12 17:37:03'),(18,'2023-02-21','2023-02-21','Huelga',1,8,'2023-02-12 17:37:05','2023-02-12 17:37:05'),(19,'2023-02-21','2023-02-21','Huelga',1,9,'2023-02-12 17:37:07','2023-02-12 17:37:07'),(20,'2023-02-21','2023-02-21','Huelga',1,10,'2023-02-12 17:37:10','2023-02-12 17:37:10'),(21,'2023-02-21','2023-02-21','Huelga',1,11,'2023-02-12 17:37:13','2023-02-12 17:37:13'),(22,'2023-02-21','2023-02-21','Huelga',1,12,'2023-02-12 17:37:16','2023-02-12 17:37:16'),(23,'2023-02-21','2023-02-21','Huelga',1,13,'2023-02-12 17:37:19','2023-02-12 17:37:19'),(24,'2023-02-21','2023-02-21','Huelga',1,14,'2023-02-12 17:37:21','2023-02-12 17:37:21'),(25,'2023-02-21','2023-02-21','Huelga',1,15,'2023-02-12 17:37:23','2023-02-12 17:37:23'),(26,'2023-02-21','2023-02-21','Huelga',1,16,'2023-02-12 17:37:25','2023-02-12 17:37:25'),(27,'2023-02-21','2023-02-21','Huelga',1,17,'2023-02-12 17:37:28','2023-02-12 17:37:28'),(28,'2023-02-21','2023-02-21','Huelga',1,18,'2023-02-12 17:37:30','2023-02-12 17:37:30'),(29,'2023-02-21','2023-02-21','Huelga',1,19,'2023-02-12 17:37:33','2023-02-12 17:37:33'),(30,'2023-02-21','2023-02-21','Huelga',1,20,'2023-02-12 17:37:36','2023-02-12 17:37:36'),(32,'2024-02-21','2024-02-21','Huelga',1,1,'2023-02-13 20:29:30','2023-02-13 20:29:30'),(33,'2024-02-21','2024-02-21','Huelga',1,2,'2023-02-13 20:29:30','2023-02-13 20:29:30'),(34,'2023-03-08','2023-03-08','Limpieza',1,1,'2023-02-18 14:42:20','2023-02-18 14:42:20'),(35,'2023-03-08','2023-03-08','Limpieza',1,2,'2023-02-18 14:42:20','2023-02-18 14:42:20'),(36,'2023-03-15','2023-03-15','Limpieza',1,1,'2023-02-18 14:54:28','2023-02-18 14:54:28'),(37,'2023-03-15','2023-03-15','Limpieza',1,2,'2023-02-18 14:54:28','2023-02-18 14:54:28'),(38,'2023-03-22','2023-03-22','Limpieza',1,1,'2023-02-18 15:18:23','2023-02-18 15:18:23'),(39,'2023-03-22','2023-03-22','Limpieza',1,2,'2023-02-18 15:18:23','2023-02-18 15:18:23'),(40,'2023-02-26','2023-02-26','Por limpieza',1,2,'2023-02-24 04:09:23','2023-02-24 04:09:23'),(41,'2023-02-26','2023-02-26','Por limpieza',1,3,'2023-02-24 04:09:23','2023-02-24 04:09:23'),(42,'2024-02-21','2024-02-21','prueba',1,1,'2023-02-25 15:13:06','2023-02-25 15:13:06'),(43,'2024-02-21','2024-02-21','prueba',1,2,'2023-02-25 15:13:06','2023-02-25 15:13:06'),(44,'2023-03-27','2023-03-27','Desinfección',1,1,'2023-03-01 18:22:51','2023-03-01 18:22:51'),(45,'2023-03-03','2023-03-03','limpieza',3,1,'2023-03-01 18:23:59','2023-03-01 18:23:59'),(46,'2023-03-03','2023-03-03','limpieza',1,2,'2023-03-01 18:23:59','2023-03-01 18:23:59'),(47,'2023-03-11','2023-03-11','Limpieza',1,1,'2023-03-06 14:47:09','2023-03-06 14:47:09'),(48,'2023-03-11','2023-03-11','Limpieza',1,2,'2023-03-06 14:47:09','2023-03-06 14:47:09'),(49,'2023-03-11','2023-03-11','Limpieza',1,3,'2023-03-06 14:47:09','2023-03-06 14:47:09'),(50,'2023-03-24','2023-03-24','MANTENIMIENTO',1,1,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(51,'2023-03-24','2023-03-24','MANTENIMIENTO',1,2,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(52,'2023-03-24','2023-03-24','MANTENIMIENTO',1,3,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(53,'2023-03-24','2023-03-24','MANTENIMIENTO',1,4,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(54,'2023-03-24','2023-03-24','MANTENIMIENTO',1,5,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(55,'2023-03-24','2023-03-24','MANTENIMIENTO',1,6,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(56,'2023-03-24','2023-03-24','MANTENIMIENTO',1,7,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(57,'2023-03-24','2023-03-24','MANTENIMIENTO',1,8,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(58,'2023-03-24','2023-03-24','MANTENIMIENTO',1,9,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(59,'2023-03-24','2023-03-24','MANTENIMIENTO',1,10,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(60,'2023-03-24','2023-03-24','MANTENIMIENTO',1,11,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(61,'2023-03-24','2023-03-24','MANTENIMIENTO',1,12,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(62,'2023-03-24','2023-03-24','MANTENIMIENTO',1,13,'2023-03-10 22:39:36','2023-03-10 22:39:36'),(63,'2023-03-24','2023-03-24','MANTENIMIENTO',1,14,'2023-03-10 22:39:36','2023-03-10 22:39:36');
/*!40000 ALTER TABLE `closed_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `alpha3` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_country_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'Afganistán','AFG',1,'2023-01-24 15:47:08','2023-01-24 15:47:08'),(2,'Albania','ALB',1,'2023-01-24 15:47:22','2023-01-24 15:47:22'),(3,'Alemania','DEU',1,'2023-01-24 15:47:36','2023-01-24 15:47:36'),(4,'Andorra','AND',1,'2023-01-24 15:47:46','2023-01-24 15:47:46'),(5,'Angola','AGO',1,'2023-01-24 15:47:58','2023-01-24 15:47:58'),(6,'Antigua y Barbuda','ATG',1,'2023-01-24 15:48:09','2023-01-24 15:48:09'),(7,'Arabia Saudita','SAU',1,'2023-01-24 15:48:25','2023-01-24 15:48:25'),(8,'Argelia','DZA',1,'2023-01-24 15:48:38','2023-01-24 15:48:38'),(9,'Argentina','ARG',1,'2023-01-24 15:49:14','2023-01-24 15:49:14'),(10,'Armenia','ARM',1,'2023-01-24 15:49:29','2023-01-24 15:49:29'),(11,'Australia','AUS',1,'2023-01-24 15:49:39','2023-01-24 15:49:39'),(12,'Austria','AUT',1,'2023-01-24 15:49:49','2023-01-24 15:49:49'),(13,'Azerbaiyán','AZE',1,'2023-01-24 15:50:12','2023-01-24 15:50:12'),(14,'Bahamas','BHS',1,'2023-01-24 15:50:30','2023-01-24 15:50:30'),(15,'Bahrein','BHR',1,'2023-01-24 15:50:41','2023-01-24 15:50:41'),(16,'Bangladesh','BGD',1,'2023-01-24 15:50:51','2023-01-24 15:50:51'),(17,'Barbados','BRB',1,'2023-01-24 15:51:05','2023-01-24 15:51:05'),(18,'Belarús','BLR',1,'2023-01-24 15:51:16','2023-01-24 15:51:16'),(19,'Bélgica','BEL',1,'2023-01-24 15:51:27','2023-01-24 15:51:27'),(20,'Belice','BLZ',1,'2023-01-24 15:51:37','2023-01-24 15:51:37'),(21,'Benin','BEN',1,'2023-01-24 15:52:19','2023-01-24 15:52:19'),(22,'Bhután','BTN',1,'2023-01-24 15:52:30','2023-01-24 15:52:30'),(23,'Bolivia','BOL',1,'2023-01-24 15:52:49','2023-01-24 15:52:49'),(24,'Bosnia y Herzegovina','BIH',1,'2023-01-24 15:53:03','2023-01-24 15:53:03'),(25,'Botswana','BWA',1,'2023-01-24 15:53:17','2023-01-24 15:53:17'),(26,'Brasil','BRA',1,'2023-01-24 15:53:27','2023-01-24 15:53:27'),(27,'Brunei Darussalam','BRN',1,'2023-01-24 15:53:38','2023-01-24 15:53:38'),(28,'Bulgaria','BGR',1,'2023-01-24 15:53:50','2023-01-24 15:53:50'),(29,'Burkina Faso','BFA',1,'2023-01-24 15:54:00','2023-01-24 15:54:00'),(30,'Burundi','BDI',1,'2023-01-24 15:55:11','2023-01-24 15:55:11'),(31,'Cabo Verde','CPV',1,'2023-01-24 15:55:28','2023-01-24 15:55:28'),(32,'Camboya','KHM',1,'2023-01-24 15:55:50','2023-01-24 15:55:50'),(33,'Camerún','CMR',1,'2023-01-24 15:56:08','2023-01-24 15:56:08'),(34,'Canadá','CAN',1,'2023-01-24 15:56:29','2023-01-24 15:56:29'),(35,'Chad','TCD',1,'2023-01-24 15:56:40','2023-01-24 15:56:40'),(36,'Chequia','CZE',1,'2023-01-24 15:56:53','2023-01-24 15:56:53'),(37,'Chile','CHL',1,'2023-01-24 15:57:08','2023-01-24 15:57:08'),(38,'China','CHN',1,'2023-01-24 15:57:19','2023-01-24 15:57:19'),(39,'Chipre','CYP',1,'2023-01-24 15:57:29','2023-01-24 15:57:29'),(40,'Colombia','COL',1,'2023-01-24 15:57:39','2023-01-24 15:57:39'),(41,'Comoras','COM',1,'2023-01-24 15:57:51','2023-01-24 15:57:51'),(42,'Congo','COG',1,'2023-01-24 15:58:03','2023-01-24 15:58:03'),(43,'Costa Rica','CRI',1,'2023-01-24 15:58:13','2023-01-24 15:58:13'),(44,'Côte d’Ivoire','CIV',1,'2023-01-24 15:58:40','2023-01-24 15:58:40'),(45,'Croacia','HRV',1,'2023-01-24 15:58:53','2023-01-24 15:58:53'),(46,'Cuba','CUB',1,'2023-01-24 15:59:07','2023-01-24 15:59:07'),(47,'Dinamarca','DNK',1,'2023-01-24 16:00:21','2023-01-24 16:00:21'),(48,'Djibouti','DJI',1,'2023-01-24 16:00:44','2023-01-24 16:00:44'),(49,'Dominica','DMA',1,'2023-01-24 16:00:55','2023-01-24 16:00:55'),(50,'Ecuador','ECU',1,'2023-01-24 16:01:10','2023-01-24 16:01:10'),(51,'Egipto','EGY',1,'2023-01-24 16:01:21','2023-01-24 16:01:21'),(52,'El Salvador','SLV',1,'2023-01-24 16:01:32','2023-01-24 16:01:32'),(53,'Emiratos Árabes Unidos','ARE',1,'2023-01-24 16:01:54','2023-01-24 16:01:54'),(54,'Eritrea','ERI',1,'2023-01-24 16:02:07','2023-01-24 16:02:07'),(55,'Eslovaquia','SVK',1,'2023-01-24 16:02:17','2023-01-24 16:02:17'),(56,'Eslovenia','SVN',1,'2023-01-24 16:02:54','2023-01-24 16:02:54'),(57,'España','ESP',1,'2023-01-24 16:03:04','2023-01-24 16:03:04'),(58,'Estados Unidos de América','USA',1,'2023-01-24 16:03:17','2023-01-24 16:03:17'),(59,'Estonia','EST',1,'2023-01-24 16:03:37','2023-01-24 16:03:37'),(60,'Eswatini','SWZ',1,'2023-01-24 16:03:48','2023-01-24 16:03:48'),(61,'Etiopía','ETH',1,'2023-01-24 16:03:58','2023-01-24 16:03:58'),(62,'Federación de Rusia','RUS',1,'2023-01-24 16:04:13','2023-01-24 16:04:13'),(63,'Fiji','FJI',1,'2023-01-24 16:04:25','2023-01-24 16:04:25'),(64,'Filipinas','PHL',1,'2023-01-24 16:04:34','2023-01-24 16:04:34'),(65,'Finlandia','FIN',1,'2023-01-24 16:04:46','2023-01-24 16:04:46'),(66,'Francia','FRA',1,'2023-01-24 16:04:55','2023-01-24 16:04:55'),(67,'Gabón','GAB',1,'2023-01-24 16:05:05','2023-01-24 16:05:05'),(68,'Gambia','GMB',1,'2023-01-24 16:05:15','2023-01-24 16:05:15'),(69,'Georgia','GEO',1,'2023-01-24 16:05:26','2023-01-24 16:05:26'),(70,'Ghana','GHA',1,'2023-01-24 16:05:37','2023-01-24 16:05:37'),(71,'Granada','GRD',1,'2023-01-24 16:05:48','2023-01-24 16:05:48'),(72,'Grecia','GRC',1,'2023-01-24 16:05:58','2023-01-24 16:05:58'),(73,'Guatemala','GTM',1,'2023-01-24 16:06:08','2023-01-24 16:06:08'),(74,'Guinea','GIN',1,'2023-01-24 16:06:19','2023-01-24 16:06:19'),(75,'Guinea Ecuatorial','GNQ',1,'2023-01-24 16:06:42','2023-01-24 16:06:42'),(76,'Guinea-Bissau','GNB',1,'2023-01-24 16:06:55','2023-01-24 16:06:55'),(77,'Guyana','GUY',1,'2023-01-24 16:07:05','2023-01-24 16:07:05'),(78,'Haití','HTI',1,'2023-01-24 16:07:34','2023-01-24 16:07:34'),(79,'Honduras','HND',1,'2023-01-24 16:07:43','2023-01-24 16:07:43'),(80,'Hungría','HUN',1,'2023-01-24 16:07:54','2023-01-24 16:07:54'),(81,'India','IND',1,'2023-01-24 16:08:05','2023-01-24 16:08:05'),(82,'Indonesia','IDN',1,'2023-01-24 16:08:15','2023-01-24 16:08:15'),(83,'Irán','IRN',1,'2023-01-24 16:08:26','2023-01-24 16:08:26'),(84,'Iraq','IRQ',1,'2023-01-24 16:08:38','2023-01-24 16:08:38'),(85,'Irlanda','IRL',1,'2023-01-24 16:08:49','2023-01-24 16:08:49'),(86,'Islandia','ISL',1,'2023-01-24 16:09:01','2023-01-24 16:09:01'),(87,'Islas Cook','COK',1,'2023-01-24 16:09:12','2023-01-24 16:09:12'),(88,'Islas Marshall','MHL',1,'2023-01-24 16:09:31','2023-01-24 16:09:31'),(89,'Islas Salomón','SLB',1,'2023-01-24 16:09:45','2023-01-24 16:09:45'),(90,'Israel','ISR',1,'2023-01-24 16:09:58','2023-01-24 16:09:58'),(91,'Italia','ITA',1,'2023-01-24 16:10:08','2023-01-24 16:10:08'),(92,'Jamaica','JAM',1,'2023-01-24 16:10:17','2023-01-24 16:10:17'),(93,'Japón','JPN',1,'2023-01-24 16:10:26','2023-01-24 16:10:26'),(94,'Jordania','JOR',1,'2023-01-24 16:10:38','2023-01-24 16:10:38'),(95,'Kazajstán','KAZ',1,'2023-01-24 16:10:49','2023-01-24 16:10:49'),(96,'Kenya','KEN',1,'2023-01-24 16:11:09','2023-01-24 16:11:09'),(97,'Kirguistán','KGZ',1,'2023-01-24 16:11:21','2023-01-24 16:11:21'),(98,'Kiribati','KIR',1,'2023-01-24 16:11:31','2023-01-24 16:11:31'),(99,'Kuwait','KWT',1,'2023-01-24 16:11:41','2023-01-24 16:11:41'),(100,'Lesotho','LSO',1,'2023-01-24 16:11:58','2023-01-24 16:11:58'),(101,'Letonia','LVA',1,'2023-01-24 16:12:08','2023-01-24 16:12:08'),(102,'Líbano','LBN',1,'2023-01-24 16:12:19','2023-01-24 16:12:19'),(103,'Liberia','LBR',1,'2023-01-24 16:12:28','2023-01-24 16:12:28'),(104,'Libia','LBY',1,'2023-01-24 16:12:40','2023-01-24 16:12:40'),(105,'Liechtenstein','LIE',1,'2023-01-24 16:12:48','2023-01-24 16:12:48'),(106,'Lituania','LTU',1,'2023-01-24 16:12:57','2023-01-24 16:12:57'),(107,'Luxemburgo','LUX',1,'2023-01-24 16:13:07','2023-01-24 16:13:07'),(108,'Madagascar','MDG',1,'2023-01-24 16:13:17','2023-01-24 16:13:17'),(109,'Malasia','MYS',1,'2023-01-24 16:13:35','2023-01-24 16:13:35'),(110,'Malawi','MWI',1,'2023-01-24 16:14:07','2023-01-24 16:14:07'),(111,'Maldivas','MDV',1,'2023-01-24 16:14:17','2023-01-24 16:14:17'),(112,'Malí','MLI',1,'2023-01-24 16:14:30','2023-01-24 16:14:30'),(113,'Malta','MLT',1,'2023-01-24 16:14:41','2023-01-24 16:14:41'),(114,'Marruecos','MAR',1,'2023-01-24 16:14:51','2023-01-24 16:14:51'),(115,'Mauricio','MUS',1,'2023-01-24 16:15:02','2023-01-24 16:15:02'),(116,'Mauritania','MRT',1,'2023-01-24 16:15:13','2023-01-24 16:15:13'),(117,'México','MEX',1,'2023-01-24 16:15:30','2023-01-24 16:15:30'),(118,'Micronesia','FSM',1,'2023-01-24 16:16:05','2023-01-24 16:16:05'),(119,'Mónaco','MCO',1,'2023-01-24 16:16:16','2023-01-24 16:16:16'),(120,'Mongolia','MNG',1,'2023-01-24 16:16:26','2023-01-24 16:16:26'),(121,'Montenegro','MNE',1,'2023-01-24 16:16:35','2023-01-24 16:16:35'),(122,'Mozambique','MOZ',1,'2023-01-24 16:16:44','2023-01-24 16:16:44'),(123,'Myanmar','MMR',1,'2023-01-24 16:16:54','2023-01-24 16:16:54'),(124,'Namibia','NAM',1,'2023-01-24 16:17:18','2023-01-24 16:17:18'),(125,'Nauru','NRU',1,'2023-01-24 16:17:27','2023-01-24 16:17:27'),(126,'Nepal','NPL',1,'2023-01-24 16:17:38','2023-01-24 16:17:38'),(127,'Nicaragua','NIC',1,'2023-01-24 16:17:49','2023-01-24 16:17:49'),(128,'Níger','NER',1,'2023-01-24 16:18:00','2023-01-24 16:18:00'),(129,'Nigeria','NGA',1,'2023-01-24 16:18:08','2023-01-24 16:18:08'),(130,'Niue','NIU',1,'2023-01-24 16:18:18','2023-01-24 16:18:18'),(131,'Noruega','NOR',1,'2023-01-24 16:18:29','2023-01-24 16:18:29'),(132,'Nueva Zelandia','NZL',1,'2023-01-24 16:18:41','2023-01-24 16:18:41'),(133,'Omán','OMN',1,'2023-01-24 16:18:55','2023-01-24 16:18:55'),(134,'Países Bajos','NLD',1,'2023-01-24 16:19:08','2023-01-24 16:19:08'),(135,'Pakistán','PAK',1,'2023-01-24 16:19:19','2023-01-24 16:19:19'),(136,'Palau','PLW',1,'2023-01-24 16:19:30','2023-01-24 16:19:30'),(137,'Panamá','PAN',1,'2023-01-24 16:19:41','2023-01-24 16:19:41'),(138,'Papua Nueva Guinea','PNG',1,'2023-01-24 16:19:53','2023-01-24 16:19:53'),(139,'Paraguay','PRY',1,'2023-01-24 16:20:05','2023-01-24 16:20:05'),(140,'Perú','PER',1,'2023-01-24 16:20:16','2023-01-24 16:20:16'),(141,'Polonia','POL',1,'2023-01-24 16:20:29','2023-01-24 16:20:29'),(142,'Portugal','PRT',1,'2023-01-24 16:20:39','2023-01-24 16:20:39'),(143,'Qatar','QAT',1,'2023-01-24 16:20:48','2023-01-24 16:20:48'),(144,'Reino Unido','GBR',1,'2023-01-24 16:21:11','2023-01-24 16:21:11'),(145,'República Árabe Siria','SYR',1,'2023-01-24 16:21:28','2023-01-24 16:21:28'),(146,'República Centroafricana','CAF',1,'2023-01-24 16:22:17','2023-01-24 16:22:17'),(147,'República de Macedonia del Norte','MKD',1,'2023-01-24 16:22:33','2023-01-24 16:22:33'),(148,'Corea del Sur','KOR',1,'2023-01-24 16:22:51','2023-01-24 16:22:51'),(149,'Corea del Norte','PRK',1,'2023-01-24 16:23:05','2023-01-24 16:23:05'),(150,'Rumania','ROU',1,'2023-01-24 16:23:17','2023-01-24 16:23:17'),(151,'Rwanda','RWA',1,'2023-01-24 16:23:38','2023-01-24 16:23:38'),(152,'Senegal','SEN',1,'2023-01-24 16:23:49','2023-01-24 16:23:49'),(153,'Serbia','SRB',1,'2023-01-24 16:23:58','2023-01-24 16:23:58'),(154,'Singapur','SGP',1,'2023-01-24 16:24:07','2023-01-24 16:24:07'),(155,'Suecia','SWE',1,'2023-01-24 16:24:18','2023-01-24 16:24:18'),(156,'Suiza','CHE',1,'2023-01-24 16:24:27','2023-01-24 16:24:27'),(157,'Ucrania','UKR',1,'2023-01-24 16:24:42','2023-01-24 16:24:42');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `checkin` date DEFAULT NULL,
  `checkout` date DEFAULT NULL,
  `adults` int DEFAULT NULL,
  `children` int DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT '0.00',
  `additional_amount` decimal(10,2) DEFAULT '0.00',
  `observations` text COLLATE utf8mb4_unicode_ci,
  `total` decimal(10,0) DEFAULT NULL,
  `done_payment` decimal(10,0) DEFAULT NULL,
  `pending_payment` decimal(10,0) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `client_id` int DEFAULT NULL,
  `room_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `client_id` (`client_id`),
  KEY `room_id` (`room_id`),
  KEY `ix_reservation_id` (`id`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,'2023-01-28','2023-01-28',2,0,150.00,0.00,NULL,150,150,0,1,1,1,'2023-01-24 17:33:04','2023-01-24 17:33:04'),(2,'2023-01-27','2023-01-27',2,0,150.00,0.00,NULL,150,150,0,1,2,3,'2023-01-24 17:33:41','2023-01-24 17:33:41'),(3,'2023-02-02','2023-02-02',2,0,300.00,0.00,NULL,300,300,300,1,3,2,'2023-02-03 16:52:08','2023-02-03 16:52:08'),(4,'2023-01-31','2023-01-31',1,0,150.00,0.00,NULL,150,150,150,1,3,1,'2023-02-03 17:00:29','2023-02-10 14:32:08'),(5,'2023-02-02','2023-02-02',1,0,150.00,0.00,NULL,150,150,150,1,4,1,'2023-02-03 17:02:37','2023-02-10 14:32:18'),(6,'2023-02-05','2023-02-04',1,0,150.00,0.00,NULL,150,0,150,1,1,4,'2023-02-03 17:03:57','2023-02-04 14:29:32'),(7,'2023-02-04','2023-02-04',2,1,150.00,0.00,NULL,0,150,150,1,6,2,'2023-02-04 16:03:53','2023-02-04 16:03:53'),(8,'2023-02-08','2023-02-08',2,1,150.00,0.00,NULL,0,150,150,1,1,1,'2023-02-11 15:22:46','2023-02-11 15:51:38'),(9,'2023-02-16','2023-02-16',1,0,150.00,0.00,NULL,0,150,150,1,2,1,'2023-02-12 17:57:03','2023-02-17 14:56:53'),(10,'2023-02-18','2023-02-18',1,0,150.00,0.00,NULL,0,150,150,1,2,1,'2023-02-12 18:13:10','2023-02-18 16:35:21'),(11,'2023-02-19','2023-02-19',1,0,200.00,0.00,NULL,0,200,200,1,3,2,'2023-02-12 18:15:50','2023-02-17 14:53:02'),(12,'2023-02-22','2023-02-22',1,0,200.00,60.00,'camarote',260,0,260,1,2,1,'2023-02-12 18:36:50','2023-02-25 04:54:26'),(13,'2023-02-17','2023-02-17',1,0,200.00,0.00,NULL,0,200,200,3,4,1,'2023-02-12 18:40:42','2023-02-12 18:40:42'),(14,'2023-02-26','2023-02-26',1,0,150.00,20.00,'frigobar',0,170,170,1,1,1,'2023-02-24 03:23:21','2023-02-24 03:23:21'),(15,'2023-02-24','2023-02-24',1,0,150.00,20.00,'por cama extra',0,170,170,1,1,1,'2023-02-24 03:41:45','2023-02-24 03:41:45'),(16,'2023-02-25','2023-02-25',1,0,150.00,20.00,'cama extra',170,0,170,1,3,3,'2023-02-25 15:55:02','2023-02-25 15:55:02'),(17,'2023-03-01','2023-03-01',1,2,150.00,20.00,'cama adicional',170,0,170,1,3,3,'2023-03-01 18:29:34','2023-03-04 16:02:11'),(18,'2023-03-04','2023-03-04',2,0,150.00,40.00,'CAMA EXTRA',190,190,0,1,6,1,'2023-03-04 16:03:05','2023-03-04 16:04:05'),(19,'2023-03-05','2023-03-05',1,0,150.00,20.00,'cama extra',170,0,170,1,5,1,'2023-03-04 22:13:09','2023-03-04 22:13:09'),(20,'2023-03-06','2023-03-06',1,2,150.00,40.00,'cama extra',190,0,190,1,2,4,'2023-03-04 22:13:53','2023-03-04 22:13:53'),(21,'2023-03-06','2023-03-06',1,2,300.00,0.00,'',300,0,300,1,4,2,'2023-03-04 22:14:50','2023-03-04 22:14:50'),(22,'2023-03-07','2023-03-07',1,0,150.00,0.00,'',150,0,150,1,3,1,'2023-03-04 22:16:55','2023-03-04 22:16:55'),(23,'2023-02-28','2023-02-28',1,0,150.00,0.00,'',150,0,150,1,5,1,'2023-03-04 22:23:11','2023-03-10 22:48:08'),(24,'2023-03-15','2023-03-15',1,0,150.00,0.00,'',150,0,150,1,2,3,'2023-03-04 22:23:37','2023-03-04 22:23:37'),(25,'2023-03-16','2023-03-16',1,0,180.00,0.00,'',180,0,180,1,8,6,'2023-03-04 22:24:01','2023-03-04 23:29:33'),(26,'2023-03-16','2023-03-16',1,0,150.00,0.00,'',150,0,150,1,4,1,'2023-03-04 22:24:45','2023-03-04 22:24:45'),(27,'2023-03-12','2023-03-12',3,0,150.00,50.00,'CAMA EXTRA',200,100,100,1,11,1,'2023-03-10 22:36:14','2023-03-10 22:37:30');
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `modules` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_role_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'Administradora del hotel','[\"calendar\", \"clients\", \"rooms\", \"users\", \"roles\"]',1,'2023-01-24 15:44:26','2023-01-24 15:44:26'),(2,'Recepcionista del hotel','[\"calendar\", \"clients\"]',1,'2023-01-24 15:44:53','2023-01-24 15:44:53'),(3,'Limpieza','[\"rooms\"]',3,'2023-03-06 14:01:30','2023-03-06 14:01:30'),(4,'Super Administrador','[\"calendar\", \"clients\", \"rooms\", \"users\", \"roles\"]',1,'2023-03-06 15:03:41','2023-03-06 15:13:57'),(5,'Externo','[\"calendar\", \"clients\", \"rooms\"]',1,'2023-03-08 02:43:28','2023-03-08 02:44:10');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `price` decimal(10,0) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `room_type_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_type_id` (`room_type_id`),
  KEY `ix_room_id` (`id`),
  CONSTRAINT `room_ibfk_1` FOREIGN KEY (`room_type_id`) REFERENCES `room_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'H101','Con una terraza privada, la habitación básica combina comodidad y privacidad para los viajeros con un presupuesto limitado.',150,4,1,1,'2023-01-24 16:57:44','2023-02-13 19:20:27'),(2,'H102','Una estupenda elección para escapadas en familia. Con dos camas de 1 ½ plaza y una cama de 2 plazas, la habitación familiar da capacidad a 4 personas.',300,4,1,1,'2023-01-24 16:58:43','2023-01-24 16:58:43'),(3,'H104','Con una terraza privada, la habitación básica combina comodidad y privacidad para los viajeros con un presupuesto limitado.',150,2,1,3,'2023-01-24 16:59:08','2023-01-24 16:59:08'),(4,'H105','Con una terraza privada, la habitación básica combina comodidad y privacidad para los viajeros con un presupuesto limitado.',150,2,1,3,'2023-01-24 16:59:12','2023-01-24 16:59:12'),(5,'H106','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:00:48','2023-01-24 17:00:48'),(6,'H107','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:00:54','2023-01-24 17:00:54'),(7,'H108','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:00:59','2023-01-24 17:00:59'),(8,'H109','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:01:06','2023-01-24 17:01:06'),(9,'H110','Especialmente diseñadas para brindar un alto confort, las habitaciones superiores están ubicadas en el segundo nivel y tienen terraza privada .',200,2,1,5,'2023-01-24 17:02:05','2023-01-24 17:02:05'),(10,'H111','Especialmente diseñadas para brindar un alto confort, las habitaciones superiores están ubicadas en el segundo nivel y tienen terraza privada .',200,2,1,5,'2023-01-24 17:02:16','2023-03-01 16:53:15'),(11,'H112','Especialmente diseñadas para brindar un alto confort, las habitaciones superiores están ubicadas en el segundo nivel y tienen terraza privada .',200,2,1,5,'2023-01-24 17:02:20','2023-01-24 17:02:20'),(12,'H113','Especialmente diseñadas para brindar un alto confort, las habitaciones superiores están ubicadas en el segundo nivel y tienen terraza privada .',200,2,1,5,'2023-01-24 17:02:31','2023-01-24 17:02:31'),(13,'H114','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:02:56','2023-01-24 17:02:56'),(14,'H115','Las acogedoras habitaciones básicas superiores, están ubicadas en el segundo y tercer nivel. Adornadas con muebles clásicos artesanales, terraza privada o balcón con vista interior.',180,2,1,4,'2023-01-24 17:02:59','2023-01-24 17:02:59'),(15,'H116','Ubicadas en el tercer nivel del hotel, desde las habitaciones premium puedes observar el balneario de Huanchaco y disfrutar de su característico sunset en su balcón privado .',250,2,1,6,'2023-01-24 17:03:47','2023-01-24 17:03:47'),(16,'H117','Ubicadas en el tercer nivel del hotel, desde las habitaciones premium puedes observar el balneario de Huanchaco y disfrutar de su característico sunset en su balcón privado .',250,2,1,6,'2023-01-24 17:03:54','2023-01-24 17:03:54'),(17,'H118','Ubicadas en el tercer nivel del hotel, desde las habitaciones premium puedes observar el balneario de Huanchaco y disfrutar de su característico sunset en su balcón privado .',250,2,1,6,'2023-01-24 17:03:57','2023-01-24 17:03:57'),(18,'H119','Ubicadas en el tercer nivel del hotel, desde las habitaciones premium puedes observar el balneario de Huanchaco y disfrutar de su característico sunset en su balcón privado .',250,2,1,6,'2023-01-24 17:04:02','2023-01-24 17:04:02'),(19,'H120','Habitación triple con vista a la piscina. Ideal para amigos y familias pequeñas.',200,3,1,2,'2023-01-24 17:04:57','2023-01-24 17:04:57'),(20,'H121','Habitación triple con vista a la piscina. Ideal para amigos y familias pequeñas.',200,3,0,2,'2023-01-24 17:05:00','2023-02-13 19:25:41'),(21,'H122','Cuenta con una terraza y servicio de habitación gratis',150,2,1,3,'2023-02-18 15:24:54','2023-02-25 15:28:13'),(22,'H123','Habitación especial',500,3,3,6,'2023-02-25 15:49:44','2023-02-25 15:49:44'),(24,'H126','Habitacion especial de lujo',500,3,1,4,'2023-03-04 23:21:51','2023-03-04 23:22:04');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_type`
--

DROP TABLE IF EXISTS `room_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_room_type_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_type`
--

LOCK TABLES `room_type` WRITE;
/*!40000 ALTER TABLE `room_type` DISABLE KEYS */;
INSERT INTO `room_type` VALUES (1,'Familiar',1,'2023-01-24 16:37:57','2023-01-24 16:42:28'),(2,'Triples',1,'2023-01-24 16:40:05','2023-01-24 16:40:05'),(3,'Básica',1,'2023-01-24 16:40:10','2023-01-24 16:40:10'),(4,'Básica Superior',1,'2023-01-24 16:41:03','2023-01-24 16:41:03'),(5,'Superior',1,'2023-01-24 16:41:19','2023-01-24 16:41:19'),(6,'Premium',1,'2023-01-24 16:41:31','2023-01-24 16:41:31');
/*!40000 ALTER TABLE `room_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `firstname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `lastname` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` int DEFAULT NULL,
  `token` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  KEY `ix_user_id` (`id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin@hotelapp.com','Admin','Hotel','$2b$12$SuhCVForKp.PYJBhyOJJGOlsBOFVV7mc2Oyr6JseIUvIPJh5FjKDK',1,NULL,1,'2023-01-24 15:45:53','2023-01-24 15:45:53'),(2,'recepcionist@hotelapp.com','Recepcionist','Hotel','$2b$12$bbBlQ4ifROzfITJxkqnr.ec3MzqxMAaA778s6NakhEMc2CszAlJ2G',1,NULL,2,'2023-01-24 15:46:16','2023-01-24 15:46:16'),(3,'socio@hotelapp.com','Socio','Del hotel','$2b$12$x.aC/c9BM/gekikp/yRAm.Fhf.dUJ4iK.sIoatnmhkn55qNGwwHmu',3,NULL,1,'2023-03-04 02:31:48','2023-03-04 02:33:31'),(5,'soporte@gmail.com','Soporte','Del hotel','$2b$12$T/BsvW6ZzC3jjAHQU5.zr..qrXoDJSLRxjTeOmZ0Ym13vziLjHvVG',3,NULL,2,'2023-03-04 03:33:47','2023-03-04 16:16:42');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'hotelapp'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-10 20:11:42
