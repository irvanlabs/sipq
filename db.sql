-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: user
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `user`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `user` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `user`;

--
-- Table structure for table `berita`
--

DROP TABLE IF EXISTS `berita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `berita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(2555) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isi` mediumtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `slug` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tag` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `keyword` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` enum('1','0') COLLATE utf8mb4_unicode_ci DEFAULT '0',
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NOT NULL DEFAULT current_timestamp(),
  `kategori` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `kategori` (`kategori`),
  CONSTRAINT `berita_ibfk_1` FOREIGN KEY (`kategori`) REFERENCES `kategori` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `berita`
--

LOCK TABLES `berita` WRITE;
/*!40000 ALTER TABLE `berita` DISABLE KEYS */;
/*!40000 ALTER TABLE `berita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caleg`
--

DROP TABLE IF EXISTS `caleg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `caleg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_urut` int(11) NOT NULL,
  `daerah_pemilihan` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NOT NULL DEFAULT current_timestamp(),
  `data_diri` int(11) NOT NULL,
  `pemilu_setting` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user` (`data_diri`,`pemilu_setting`),
  KEY `pemilu_setting` (`pemilu_setting`),
  CONSTRAINT `caleg_ibfk_1` FOREIGN KEY (`pemilu_setting`) REFERENCES `pemilu_setting` (`id`),
  CONSTRAINT `caleg_ibfk_2` FOREIGN KEY (`data_diri`) REFERENCES `data_diri` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caleg`
--

LOCK TABLES `caleg` WRITE;
/*!40000 ALTER TABLE `caleg` DISABLE KEYS */;
/*!40000 ALTER TABLE `caleg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_diri`
--

DROP TABLE IF EXISTS `data_diri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_diri` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nik` varchar(16) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nama_lengkap` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ttl` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jenis_kelamin` enum('P','L') COLLATE utf8mb4_unicode_ci NOT NULL,
  `status_perkawinan` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pekerjaan` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pendidikan_terakhir` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alamat_lengkap` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `sosial_media` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NOT NULL DEFAULT current_timestamp(),
  `level` int(1) NOT NULL,
  `hash` char(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hash` (`hash`),
  KEY `level` (`level`),
  CONSTRAINT `data_diri_ibfk_1` FOREIGN KEY (`level`) REFERENCES `level` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_diri`
--

LOCK TABLES `data_diri` WRITE;
/*!40000 ALTER TABLE `data_diri` DISABLE KEYS */;
INSERT INTO `data_diri` VALUES (2,'string','string','%s, %d %s %d','P','string','string','string','string','string','2021-10-23 05:00:00','2021-10-23 05:00:00',7,'a hash value'),(3,'string','string','string, 5 Februari 2001','P','string','string','string','string','string','2021-10-23 05:41:20','2021-10-23 05:41:20',7,'bf356b6031e8f3737f9885d73c4c62a374dad3b9007e6b9a5b7e62d0666c0ffeca82b6c16a532b01432c6cf9e1a758a77fd799027a71eec4029ab9edcaa784e1');
/*!40000 ALTER TABLE `data_diri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jenis_kandidat`
--

DROP TABLE IF EXISTS `jenis_kandidat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jenis_kandidat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jenis_kandidat`
--

LOCK TABLES `jenis_kandidat` WRITE;
/*!40000 ALTER TABLE `jenis_kandidat` DISABLE KEYS */;
/*!40000 ALTER TABLE `jenis_kandidat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kategori`
--

DROP TABLE IF EXISTS `kategori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kategori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategori`
--

LOCK TABLES `kategori` WRITE;
/*!40000 ALTER TABLE `kategori` DISABLE KEYS */;
/*!40000 ALTER TABLE `kategori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `level`
--

DROP TABLE IF EXISTS `level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `level` (
  `id` int(1) NOT NULL AUTO_INCREMENT,
  `nama` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level`
--

LOCK TABLES `level` WRITE;
/*!40000 ALTER TABLE `level` DISABLE KEYS */;
INSERT INTO `level` VALUES (1,'administrator'),(2,'admin_pusat'),(3,'admin_provinsi'),(4,'admin_kabupaten'),(5,'caleg'),(6,'saksi'),(7,'anggota');
/*!40000 ALTER TABLE `level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masalah`
--

DROP TABLE IF EXISTS `masalah`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `masalah` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `deskripsi` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `tps` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tps` (`tps`),
  CONSTRAINT `masalah_ibfk_1` FOREIGN KEY (`tps`) REFERENCES `tps` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masalah`
--

LOCK TABLES `masalah` WRITE;
/*!40000 ALTER TABLE `masalah` DISABLE KEYS */;
/*!40000 ALTER TABLE `masalah` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pemilu_setting`
--

DROP TABLE IF EXISTS `pemilu_setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pemilu_setting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tanggal` datetime NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NOT NULL DEFAULT current_timestamp(),
  `jenis_kandidat` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jenis_kandidat` (`jenis_kandidat`),
  CONSTRAINT `pemilu_setting_ibfk_1` FOREIGN KEY (`jenis_kandidat`) REFERENCES `jenis_kandidat` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pemilu_setting`
--

LOCK TABLES `pemilu_setting` WRITE;
/*!40000 ALTER TABLE `pemilu_setting` DISABLE KEYS */;
/*!40000 ALTER TABLE `pemilu_setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quickcount`
--

DROP TABLE IF EXISTS `quickcount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quickcount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jumlah_suara` int(11) NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp(),
  `date_updated` timestamp NOT NULL DEFAULT current_timestamp(),
  `caleg` int(11) NOT NULL,
  `tps` int(11) NOT NULL,
  `pemilu_setting` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `caleg` (`caleg`,`tps`,`pemilu_setting`),
  KEY `tps` (`tps`),
  KEY `pemilu_setting` (`pemilu_setting`),
  CONSTRAINT `quickcount_ibfk_1` FOREIGN KEY (`tps`) REFERENCES `tps` (`id`),
  CONSTRAINT `quickcount_ibfk_2` FOREIGN KEY (`pemilu_setting`) REFERENCES `pemilu_setting` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quickcount`
--

LOCK TABLES `quickcount` WRITE;
/*!40000 ALTER TABLE `quickcount` DISABLE KEYS */;
/*!40000 ALTER TABLE `quickcount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tps`
--

DROP TABLE IF EXISTS `tps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no_tps` int(11) NOT NULL,
  `latlong` point NOT NULL,
  `provinsi` int(11) NOT NULL,
  `kabupaten` int(11) NOT NULL,
  `kecamatan` int(11) NOT NULL,
  `desa` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `provinsi` (`provinsi`,`kabupaten`,`kecamatan`,`desa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tps`
--

LOCK TABLES `tps` WRITE;
/*!40000 ALTER TABLE `tps` DISABLE KEYS */;
/*!40000 ALTER TABLE `tps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-23 12:45:09
