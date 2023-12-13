-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2023 at 03:22 PM
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
  `Departure_date` varchar(10) NOT NULL,
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
(1, 'spicejet', 'mumbai', 'delhi', 'SG815', 7200),
(2, 'spicejet', 'chennai', 'pune', 'SG773', 8100),
(3, 'spicejet', 'chennai', 'hyderabad', 'SG731', 5200),
(4, 'spicejet', 'goa', 'bengaluru', 'SG3720', 6500),
(5, 'spicejet', 'pune', 'bengaluru', 'SG493', 8500),
(6, 'VISTARA', 'new delhi', 'hyderabad', 'UK-879', 5000),
(7, 'VISTARA', 'new delhi', 'bengaluru', 'UK-811', 6528),
(8, 'VISTARA', 'mumbai', 'jaipur', 'UK-819', 4379),
(9, 'VISTARA', 'chennai', 'pune', 'UK-832', 6927),
(10, 'VISTARA', 'lucknow', 'goa', 'UK-835', 8552),
(11, 'GOAIR', 'mumbai', 'delhi', 'G8395', 5500),
(12, 'GOAIR', 'new delhi', 'chennai', 'G8461', 8500),
(13, 'GOAIR', 'aurangabad', 'delhi', 'G8492', 5200),
(14, 'GOAIR', 'ahemdabad', 'chandigarh', 'G8911', 8800),
(15, 'GOAIR', 'ahemdabad', 'jaipur', 'G8702', 4500),
(16, 'AIRINDIA', 'srinagar', 'hyderabad', 'AI-802', 9200),
(17, 'AIRINDIA', 'hyderabad', 'jaipur', 'AI-821', 7500),
(18, 'AIRINDIA', 'bengaluru', 'harayana', 'AI-815', 6300),
(19, 'AIRINDIA', 'mumbai', 'delhi', 'AI-573', 7800),
(20, 'AIRINDIA', 'lucknow', 'mumbai', 'AI-550', 7500),
(21, 'INDIGO', 'agra', 'bengaluru', '6E-5917', 6650),
(22, 'INDIGO', 'ahmedabad', 'lucknow', '6E-544', 8245),
(23, 'INDIGO', 'bangkok', 'delhi', '6E-0086', 8500),
(24, 'INDIGO', 'bengaluru', 'kolkata', '6E-0954', 5550),
(25, 'INDIGO', 'bhopal', 'surat', '6E-0745', 8500);

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
  `seat_remaining` int(20) NOT NULL,
  `Departure_Time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seat`
--

INSERT INTO `seat` (`Flight_no`, `seat count`, `seat_filled`, `seat_remaining`, `Departure_Time`) VALUES
('SG815', 30, 0, 30, '20:45'),
('SG773\r\n', 30, 0, 30, '18:00'),
('SG731\r\n', 30, 0, 30, '15:00'),
('SG3720', 30, 0, 30, '00:15'),
('SG493', 30, 0, 30, '03:15'),
('UK-879', 30, 0, 30, '13:05'),
('UK-811', 30, 0, 30, '20:45'),
('UK-819', 30, 0, 30, '10:45'),
('UK-832', 30, 0, 30, '7:13'),
('UK-835', 30, 0, 30, '03:15'),
('G8395', 30, 0, 30, '15:00'),
('G8461', 30, 0, 30, '18:00'),
('G8492', 30, 0, 30, '20:45'),
('G8911', 30, 0, 30, '13:05'),
('G8702', 30, 0, 30, '03:15'),
('AI-802', 30, 0, 30, '00:15'),
('AI-821', 30, 0, 30, '7:13'),
('AI-815', 30, 0, 30, '00:15'),
('AI-573', 30, 0, 30, '18:00'),
('AI-550', 30, 0, 30, '20:45'),
('6E-5917', 30, 0, 30, '03:15'),
('6E-544', 30, 0, 30, '7:13'),
('6E-0086', 30, 0, 30, '13:05'),
('6E-0954', 30, 0, 30, '18:00'),
('6E-0745', 30, 0, 30, '00:15');

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
