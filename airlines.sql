-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2023 at 02:11 PM
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
-- Table structure for table `addons`
--

CREATE TABLE `addons` (
  `Ticket_NO` int(10) NOT NULL,
  `Food` varchar(20) NOT NULL,
  `Need_assis` varchar(5) NOT NULL,
  `Drink` varchar(5) NOT NULL,
  `cab` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `Ticket_NO` int(10) NOT NULL,
  `User` varchar(20) NOT NULL,
  `Passenger_name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `PhNo` int(10) NOT NULL,
  `Flight_no` varchar(20) NOT NULL,
  `Class` int(1) NOT NULL,
  `Fee` int(10) NOT NULL,
  `Payment_status` tinyint(1) NOT NULL,
  `booking_sts` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `CHARGES` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`s_no`, `AIRLINES_NAME`, `DEPARTURE`, `DESTINATION`, `FLIGHT_NO`, `CHARGES`) VALUES
(1, 'spicejet', 'MUMBAI', 'delhi', 'SG815', 7200),
(2, 'spicejet', 'chennai', 'pune', 'SG773', 8100),
(3, 'spicejet', 'chennai', 'hyderabad', 'SG731', 5200),
(4, 'spicejet', 'goa', 'bengaluru', 'SG3720', 6500),
(5, 'spicejet', 'pune', 'bengaluru', 'SG493', 8500),
(6, 'VISTARA', 'NEW DELHI', 'HYDERABAD', 'UK-879', 5000),
(7, 'VISTARA', 'NEW DELHI', 'BENGALURU', 'UK-811', 6528),
(8, 'VISTARA', 'MUMBAI', 'JAIPUR', 'UK-819', 4379),
(9, 'VISTARA', 'CHENNAI', 'PUNE', 'UK-832', 6927),
(10, 'VISTARA', 'LUCKNOW', 'GOA', 'UK-835', 8552),
(11, 'GOAIR', 'MUMBAI', 'DELHI', 'G8395', 5500),
(12, 'GOAIR', 'NEW DELHI', 'CHENNAI', 'G8461', 8500),
(13, 'GOAIR', 'AURANGABAD', 'DELHI', 'G8492', 5200),
(14, 'GOAIR', 'AHEMDABAD', 'CHANDIGARH', 'G8911', 8800),
(15, 'GOAIR', 'AHEMDABAD', 'JAIPUR', 'G8702', 4500),
(16, 'AIRINDIA', 'SRINAGAR', 'HYDERABAD', 'AI-802', 9200),
(17, 'AIRINDIA', 'HYDERABAD', 'JAIPUR', 'AI-821', 7500),
(18, 'AIRINDIA', 'BENGALURU', 'HARAYANA', 'AI-815', 6300),
(19, 'AIRINDIA', 'MUMBAI', 'DELHI', 'AI-573', 7800),
(20, 'AIRINDIA', 'LUCKNOW', 'MUMBAI', 'AI-550', 7500),
(21, 'INDIGO', 'AGRA', 'BENGALURU', '6E-5917', 6650),
(22, 'INDIGO', 'AHMEDABAD', 'LUCKNOW', '6E-544', 8245),
(23, 'INDIGO', 'BANGKOK', 'DELHI', '6E-0086', 8500),
(24, 'INDIGO', 'BENGALURU', 'KOLKATA', '6E-0954', 5550),
(25, 'INDIGO', 'BHOPAL', 'SURAT', '6E-0745', 8500);

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
('srivikkash', '123', 'vikkassri@gmail.com', 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `seat`
--

CREATE TABLE `seat` (
  `Flight_no` varchar(20) NOT NULL,
  `seat count` int(20) NOT NULL,
  `seat_filled` int(20) NOT NULL,
  `seat_remaining` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`Ticket_NO`);

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
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `Ticket_NO` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `flights`
--
ALTER TABLE `flights`
  MODIFY `s_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
