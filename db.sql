-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 19, 2021 at 07:29 AM
-- Server version: 10.6.4-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_akses_menu`
--

CREATE TABLE IF NOT EXISTS `tb_akses_menu` (
  `id_akses_menu` int(11) NOT NULL AUTO_INCREMENT,
  `id_level` int(11) NOT NULL,
  `id_menu` int(11) NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_akses_menu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_berita`
--

CREATE TABLE IF NOT EXISTS `tb_berita` (
  `id_berita` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isi` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `gambar` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_kategori` int(11) NOT NULL,
  `slug` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tag` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `keyword` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  `status` enum('aktif','tidak aktif') COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_berita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_caleg`
--

CREATE TABLE IF NOT EXISTS `tb_caleg` (
  `id_caleg` int(11) NOT NULL AUTO_INCREMENT,
  `no_urut` varchar(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_user` int(11) NOT NULL,
  `image` varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_provinsi` int(11) NOT NULL,
  `id_jeniskandidat` int(11) NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_caleg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_desa`
--

CREATE TABLE IF NOT EXISTS `tb_desa` (
  `id_desa` int(11) NOT NULL AUTO_INCREMENT,
  `id_kecamatan` int(11) NOT NULL,
  `nama` varchar(111) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_desa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_ikon`
--

CREATE TABLE IF NOT EXISTS `tb_ikon` (
  `id_ikon` int(11) NOT NULL AUTO_INCREMENT,
  `ikon` int(155) NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  `status` enum('aktif','tidak aktif') COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_ikon`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_jeniskandidat`
--

CREATE TABLE IF NOT EXISTS `tb_jeniskandidat` (
  `id_jeniskandidat` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_jeniskandidat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_kabupaten`
--

CREATE TABLE IF NOT EXISTS `tb_kabupaten` (
  `id_kabupaten` int(11) NOT NULL AUTO_INCREMENT,
  `id_provinsi` int(11) NOT NULL,
  `nama` int(111) NOT NULL,
  PRIMARY KEY (`id_kabupaten`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_kategori`
--

CREATE TABLE IF NOT EXISTS `tb_kategori` (
  `id_kategori` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` mediumint(9) NOT NULL,
  `status` enum('aktif','tidak aktif') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'tidak aktif',
  PRIMARY KEY (`id_kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_kecamatan`
--

CREATE TABLE IF NOT EXISTS `tb_kecamatan` (
  `id_kecamatan` int(11) NOT NULL AUTO_INCREMENT,
  `id_kabupaten` int(11) NOT NULL,
  `nama` varchar(111) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_kecamatan`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_level`
--

CREATE TABLE IF NOT EXISTS `tb_level` (
  `id_level` int(11) NOT NULL AUTO_INCREMENT,
  `nama_level` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` enum('aktif','tidak aktif') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'tidak aktif',
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_level`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_log_histori`
--

CREATE TABLE IF NOT EXISTS `tb_log_histori` (
  `id_log_history` int(11) NOT NULL AUTO_INCREMENT,
  `data` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `keterangan` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_user` int(11) NOT NULL,
  `date_create` datetime NOT NULL,
  PRIMARY KEY (`id_log_history`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_masalah`
--

CREATE TABLE IF NOT EXISTS `tb_masalah` (
  `id_masalah` int(11) NOT NULL,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_kategori` int(11) NOT NULL,
  `deskirpsi` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_update` datetime NOT NULL,
  `date_create` datetime NOT NULL,
  `id_tps` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_menu`
--

CREATE TABLE IF NOT EXISTS `tb_menu` (
  `di_menu` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_ikon` int(11) NOT NULL,
  `date_update` datetime NOT NULL,
  `date_create` datetime NOT NULL,
  `url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`di_menu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_partai`
--

CREATE TABLE IF NOT EXISTS `tb_partai` (
  `id_partai` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_partai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_pemilu_setting`
--

CREATE TABLE IF NOT EXISTS `tb_pemilu_setting` (
  `id_pemilu_setting` int(11) NOT NULL,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_jeniskandidat` int(11) NOT NULL,
  `id_provinsi` int(11) NOT NULL,
  `id_kabupaten` int(11) NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_provinsi`
--

CREATE TABLE IF NOT EXISTS `tb_provinsi` (
  `id_provinsi` int(11) NOT NULL AUTO_INCREMENT,
  `nama` int(111) NOT NULL,
  PRIMARY KEY (`id_provinsi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_sub_menu`
--

CREATE TABLE IF NOT EXISTS `tb_sub_menu` (
  `id_sub_menu` int(11) NOT NULL AUTO_INCREMENT,
  `id_menu` int(11) NOT NULL,
  `id_ikon` int(11) NOT NULL,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  `sub_url` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_sub_menu`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_tps`
--

CREATE TABLE IF NOT EXISTS `tb_tps` (
  `id_tps` int(11) NOT NULL AUTO_INCREMENT,
  `tps_no` int(5) NOT NULL,
  `nama` varchar(155) COLLATE utf8mb4_unicode_ci NOT NULL,
  `keterangan` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL,
  PRIMARY KEY (`id_tps`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi_`
--

CREATE TABLE IF NOT EXISTS `tb_transaksi_` (
  `id_pemilu_setting` int(11) NOT NULL,
  `nama` int(155) NOT NULL,
  `id_jeniskandidat` int(11) NOT NULL,
  `id_provinsi` int(11) NOT NULL,
  `id_kabupaten` int(11) NOT NULL,
  `date_create` datetime NOT NULL,
  `date_update` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
