-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 28, 2025 at 12:51 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `autism_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `hasil_form`
--

CREATE TABLE `hasil_form` (
  `id` int NOT NULL COMMENT 'Id setiap entri',
  `data_json` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT 'Jawaban JSON',
  `created_` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'waktu pengiriman'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `hasil_form`
--

INSERT INTO `hasil_form` (`id`, `data_json`, `created_`) VALUES
(1, '{\"Q1\": \"Ya\", \"Q2\": \"Tidak\", \"Q3\": \"Ya\", \"Q4\": \"Tidak\"}', '2025-09-20 05:23:30'),
(2, '{\"Q1\": \"\", \"Q2\": \"\", \"Q3\": \"\", \"Q4\": \"\"}', '2025-09-20 08:26:41'),
(3, '{\"Q1\": \"\", \"Q2\": \"\", \"Q3\": \"\", \"Q4\": \"\"}', '2025-09-20 08:26:41'),
(4, '{\"Q1\": \"Ya\", \"Q2\": \"\", \"Q3\": \"Tidak\", \"Q4\": \"\"}', '2025-09-20 09:55:38');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hasil_form`
--
ALTER TABLE `hasil_form`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hasil_form`
--
ALTER TABLE `hasil_form`
  MODIFY `id` int NOT NULL AUTO_INCREMENT COMMENT 'Id setiap entri', AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
