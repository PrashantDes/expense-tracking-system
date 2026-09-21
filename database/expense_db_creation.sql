CREATE DATABASE  IF NOT EXISTS `expense_manager` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `expense_manager`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: expense_manager
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `expense_date` date NOT NULL,
  `amount` float NOT NULL,
  `category` varchar(255) NOT NULL,
  `notes` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (3,'2024-08-02',50,'Entertainment','Movie tickets'),(4,'2024-08-02',150,'Shopping','New shoes'),(5,'2024-08-03',100,'Food','Dinner at a restaurant'),(11,'2024-08-02',400,'Food','Groceries for the week'),(12,'2024-08-02',80,'Entertainment','Concert tickets'),(13,'2024-08-02',100,'Shopping','Clothes'),(14,'2024-08-02',50,'Other','Gasoline'),(15,'2024-08-03',60,'Food','Dinner at a restaurant'),(16,'2024-08-03',20,'Entertainment','Video rental'),(17,'2024-08-03',120,'Shopping','Gadgets'),(18,'2024-08-03',15,'Other','Coffee'),(19,'2024-08-04',25,'Food','Lunch'),(20,'2024-08-04',200,'Shopping','Home supplies'),(21,'2024-08-04',10,'Other','Parking'),(22,'2024-08-05',350,'Rent','Shared rent payment'),(23,'2024-08-05',40,'Food','Snacks'),(24,'2024-08-05',75,'Entertainment','Theater tickets'),(25,'2024-08-05',100,'Shopping','Books'),(26,'2024-08-05',15,'Other','Miscellaneous'),(27,'2024-08-06',30,'Food','Breakfast'),(28,'2024-08-06',100,'Shopping','Shoes'),(29,'2024-08-06',80,'Entertainment','Movies'),(30,'2024-08-06',15,'Other','Public transport'),(31,'2024-09-01',1200,'Rent','Monthly rent payment'),(32,'2024-09-01',300,'Food','Groceries for the week'),(33,'2024-09-01',50,'Entertainment','Movie tickets'),(34,'2024-09-01',150,'Shopping','New shoes'),(35,'2024-09-01',20,'Other','Bus fare'),(36,'2024-09-02',400,'Food','Groceries for the week'),(37,'2024-09-02',80,'Entertainment','Concert tickets'),(38,'2024-09-02',100,'Shopping','Clothes'),(39,'2024-09-02',50,'Other','Gasoline'),(40,'2024-09-03',60,'Food','Dinner at a restaurant'),(41,'2024-09-03',20,'Entertainment','Video rental'),(42,'2024-09-03',120,'Shopping','Gadgets'),(43,'2024-09-03',15,'Other','Coffee'),(44,'2024-09-04',25,'Food','Lunch'),(45,'2024-09-04',200,'Shopping','Home supplies'),(46,'2024-09-04',10,'Other','Parking'),(47,'2024-09-05',350,'Rent','Shared rent payment'),(48,'2024-09-05',40,'Food','Snacks'),(49,'2024-09-05',75,'Entertainment','Theater tickets'),(50,'2024-09-05',100,'Shopping','Books'),(51,'2024-09-05',15,'Other','Miscellaneous'),(52,'2024-09-30',1000,'Rent','Monthly rent payment'),(53,'2024-09-30',250,'Food','Groceries for the week'),(54,'2024-09-30',40,'Entertainment','Cinema tickets'),(55,'2024-09-30',100,'Shopping','Clothes'),(56,'2024-09-30',20,'Other','Public transport'),(62,'2024-08-15',10,'Shopping','Bought potatoes'),(63,'2024-08-01',1227,'Rent','Monthly rent payment'),(64,'2024-08-01',300,'Food','Groceries for the week'),(65,'2024-08-01',1200,'Rent','Monthly rent payment'),(66,'2024-08-01',300,'Food','Groceries for the week');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-26 15:01:53