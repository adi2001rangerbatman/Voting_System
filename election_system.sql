-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 14, 2023 at 11:30 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `election system`
--

-- --------------------------------------------------------

--
-- Table structure for table `candidate`
--

CREATE TABLE `candidate` (
  `nic` int(12) NOT NULL,
  `c_name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `province` varchar(20) NOT NULL,
  `list_no` int(100) NOT NULL,
  `ppid` int(10) NOT NULL,
  `vote_count` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `candidate`
--

INSERT INTO `candidate` (`nic`, `c_name`, `age`, `qualification`, `province`, `list_no`, `ppid`, `vote_count`) VALUES
(2001, 'Adithya', 24, 'Passed A/L', 'North', 1, 2, 0),
(2002, 'Nawodi', 24, 'A/l,O/l', 'Central', 2, 3, 0),
(2003, 'Dinuka', 45, 'BA.Law Univercity of Colombo', 'Uva', 3, 3, 0),
(2004, 'Gayanuka ', 28, 'A/l', 'North', 4, 1, 6),
(2005, 'Hiruni', 26, 'Undergraduate', 'North', 5, 2, 6),
(2006, 'Ravi', 33, 'O/L', 'Western', 6, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `citizen`
--

CREATE TABLE `citizen` (
  `nic` int(12) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(10) NOT NULL,
  `province` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `citizen`
--

INSERT INTO `citizen` (`nic`, `name`, `age`, `province`) VALUES
(2001, 'Nawo', 24, 'North'),
(2002, 'Adithya', 25, 'North'),
(2003, 'Dinuka', 45, 'Uva'),
(2004, 'Gayanuka', 28, 'North'),
(2005, 'Hiruni', 26, 'North'),
(2006, 'Ravi', 23, 'Western');

-- --------------------------------------------------------

--
-- Table structure for table `political_parties`
--

CREATE TABLE `political_parties` (
  `ppid` int(10) NOT NULL,
  `p_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `political_parties`
--

INSERT INTO `political_parties` (`ppid`, `p_name`) VALUES
(1, 'JVP'),
(2, 'SLNP'),
(3, 'SLJP'),
(4, 'UNP');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`nic`),
  ADD KEY `FK_CandidateParty` (`ppid`);

--
-- Indexes for table `citizen`
--
ALTER TABLE `citizen`
  ADD PRIMARY KEY (`nic`);

--
-- Indexes for table `political_parties`
--
ALTER TABLE `political_parties`
  ADD PRIMARY KEY (`ppid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `candidate`
--
ALTER TABLE `candidate`
  MODIFY `nic` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2007;

--
-- AUTO_INCREMENT for table `citizen`
--
ALTER TABLE `citizen`
  MODIFY `nic` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2007;

--
-- AUTO_INCREMENT for table `political_parties`
--
ALTER TABLE `political_parties`
  MODIFY `ppid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `candidate`
--
ALTER TABLE `candidate`
  ADD CONSTRAINT `FK_CandidateParty` FOREIGN KEY (`ppid`) REFERENCES `political_parties` (`ppid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
