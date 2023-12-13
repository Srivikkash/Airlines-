-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2023 at 01:20 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airlines`
--

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

CREATE TABLE `flights` (
  `s_no` int(11) NOT NULL,
  `AIRLINES_NAME` varchar(100) DEFAULT NULL,
  `DEPARTURE` varchar(100) DEFAULT NULL,
  `DESTINATION` varchar(100) DEFAULT NULL,
  `FLIGHT_NO` varchar(50) DEFAULT NULL,
  `TIME_OF_DEPARTURE` varchar(50) DEFAULT NULL,
  `TIME_OF_ARRIVAL` varchar(50) DEFAULT NULL,
  `CHARGES` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`s_no`, `AIRLINES_NAME`, `DEPARTURE`, `DESTINATION`, `FLIGHT_NO`, `TIME_OF_DEPARTURE`, `TIME_OF_ARRIVAL`, `CHARGES`) VALUES
(1, 'spicejet', 'MUMBAI', 'delhi', 'SG815', '07:20:00', '09:35:00', 7200),
(2, 'spicejet', 'chennai', 'pune', 'SG773', '13:35:00', '15:15:00', 8100),
(3, 'spicejet', 'chennai', 'hyderabad', 'SG731', '06:20:00', '07:30:00', 5200),
(4, 'spicejet', 'goa', 'bengaluru', 'SG3720', '08:10:00', '09:55:00', 6500),
(5, 'spicejet', 'pune', 'bengaluru', 'SG493', '17:25:00', '19:55:00', 8500),
(6, 'VISTARA', 'NEW DELHI', 'HYDERABAD', 'UK-879', '17:40:00', '19:50:00', 5000),
(7, 'VISTARA', 'NEW DELHI', 'BENGALURU', 'UK-811', '06:15:00', '09:00:00', 6528),
(8, 'VISTARA', 'MUMBAI', 'JAIPUR', 'UK-819', '20:00:OO', '06:45:00', 4379),
(9, 'VISTARA', 'CHENNAI', 'PUNE', 'UK-832', '07:05:00', '19:55:00', 6927),
(10, 'VISTARA', 'LUCKNOW', 'GOA', 'UK-835', '17:50:00', '13:50:00', 8552),
(11, 'GOAIR', 'MUMBAI', 'DELHI', 'G8395', '01:45:00', '03:30:00', 5500),
(12, 'GOAIR', 'NEW DELHI', 'CHENNAI', 'G8461', '07:45:00', '22:20:00', 8500),
(13, 'GOAIR', 'AURANGABAD', 'DELHI', 'G8492', '08:00:00', '23:00:00', 5200),
(14, 'GOAIR', 'AHEMDABAD', 'CHANDIGARH', 'G8911', '09:00:00', '10:00:00', 8800),
(15, 'GOAIR', 'AHEMDABAD', 'JAIPUR', 'G8702', '16:30:00', '17:55:00', 4500),
(16, 'AIRINDIA', 'SRINAGAR', 'HYDERABAD', 'AI-802', '14:40:00', '20:00:00', 9200),
(17, 'AIRINDIA', 'HYDERABAD', 'JAIPUR', 'AI-821', '06:15:00', '12:00:00', 7500),
(18, 'AIRINDIA', 'BENGALURU', 'HARAYANA', 'AI-815', '07:00:00', '07:30:00', 6300),
(19, 'AIRINDIA', 'MUMBAI', 'DELHI', 'AI-573', '12:45:00', '01:20:00', 7800),
(20, 'AIRINDIA', 'LUCKNOW', 'MUMBAI', 'AI-550', '23:45:00', '00:00:00', 7500),
(21, 'INDIGO', 'AGRA', 'BENGALURU', '6E-5917', '18:00:00', '18:30:00', 6650),
(22, 'INDIGO', 'AHMEDABAD', 'LUCKNOW', '6E-544', '03:50:00', '04:10:00', 8245),
(23, 'INDIGO', 'BANGKOK', 'DELHI', '6E-0086', '12:35:00', '01:00:00', 8500),
(24, 'INDIGO', 'BENGALURU', 'KOLKATA', '6E-0954', '04:25:00', '04:55:00', 5550),
(25, 'INDIGO', 'BHOPAL', 'SURAT', '6E-0745', '15:30:00', '16:00:00', 8500);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `uname` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `gender` int(1) NOT NULL,
  `age` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `password`, `email`, `gender`, `age`) VALUES
('ardra', '342', 'ardra@gmail.com', 2, 23),
('mohan', '123', 'mohan@gmail.com', 1, 20),
('Nirmal', '123', 'nirmal@gmail.com', 1, 22),
('sri', '9283', 'vikkash@gmail.com', 1, 20),
('srivikkash', '123', 'vikkassri@gmail.com', 1, 20);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`s_no`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`uname`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
