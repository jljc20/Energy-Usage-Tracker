CREATE DATABASE  IF NOT EXISTS `track` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `track`;
-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: track
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Dailyuse`
--

DROP TABLE IF EXISTS `Dailyuse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dailyuse` (
  `id` int(1) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `fridgeM` varchar(45) DEFAULT NULL,
  `fridgeP` varchar(45) DEFAULT NULL,
  `tvM` varchar(45) DEFAULT NULL,
  `tvP` varchar(45) DEFAULT NULL,
  `washingM` varchar(45) DEFAULT NULL,
  `washingP` varchar(45) DEFAULT NULL,
  `airconM` varchar(45) DEFAULT NULL,
  `airconP` varchar(45) DEFAULT NULL,
  `totalP` varchar(45) DEFAULT NULL,
  `totalE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `date_UNIQUE` (`date`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dailyuse`
--

LOCK TABLES `Dailyuse` WRITE;
/*!40000 ALTER TABLE `Dailyuse` DISABLE KEYS */;
INSERT INTO `Dailyuse` VALUES (1,'2022-02-13','1440','0.96','30','0.0','20','0.02','40','0.16','1.14','5.7');
/*!40000 ALTER TABLE `Dailyuse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Quantity`
--

DROP TABLE IF EXISTS `Quantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Quantity` (
  `id` int(1) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `fridgeQ` varchar(45) DEFAULT NULL,
  `fridgeT` varchar(45) DEFAULT NULL,
  `fridgeE` varchar(45) DEFAULT NULL,
  `tvQ` varchar(45) DEFAULT NULL,
  `tvT` varchar(45) DEFAULT NULL,
  `tvE` varchar(45) DEFAULT NULL,
  `washingQ` varchar(45) DEFAULT NULL,
  `washingT` varchar(45) DEFAULT NULL,
  `washingE` varchar(45) DEFAULT NULL,
  `airconQ` varchar(45) DEFAULT NULL,
  `airconT` varchar(45) DEFAULT NULL,
  `airconE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Quantity`
--

LOCK TABLES `Quantity` WRITE;
/*!40000 ALTER TABLE `Quantity` DISABLE KEYS */;
INSERT INTO `Quantity` VALUES (1,'2','3','0.1','0','0','0','3','5','0.1','2','4','0.3');
/*!40000 ALTER TABLE `Quantity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Unit`
--

DROP TABLE IF EXISTS `Unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Unit` (
  `id` int(1) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `electricity` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Unit`
--

LOCK TABLES `Unit` WRITE;
/*!40000 ALTER TABLE `Unit` DISABLE KEYS */;
INSERT INTO `Unit` VALUES (1,'0.2');
/*!40000 ALTER TABLE `Unit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-13  2:14:05
