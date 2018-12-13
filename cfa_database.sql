-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 13, 2018 at 05:28 PM
-- Server version: 5.7.24-0ubuntu0.16.04.1
-- PHP Version: 7.0.32-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cfa`
--

-- --------------------------------------------------------

--
-- Table structure for table `Applicants`
--

CREATE TABLE `Applicants` (
  `Name` varchar(40) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Password` varchar(32) NOT NULL,
  `isFarmer` int(1) NOT NULL,
  `Address` varchar(60) NOT NULL,
  `State` varchar(40) NOT NULL,
  `City` varchar(40) NOT NULL,
  `ZipCode` int(5) NOT NULL,
  `ApplicantID` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Farmers`
--

CREATE TABLE `Farmers` (
  `farmer_ID` int(11) NOT NULL,
  `terms` varchar(100) NOT NULL,
  `amt_tillable` int(255) NOT NULL,
  `amt_pasture` int(255) NOT NULL,
  `organic` int(1) NOT NULL,
  `housing_desc` text NOT NULL,
  `eq_storage` int(1) NOT NULL,
  `livestock_barn` int(1) NOT NULL,
  `stables` int(1) NOT NULL,
  `greenhouse` int(1) NOT NULL,
  `desc_equip` text NOT NULL,
  `irrigation` int(1) NOT NULL,
  `education` varchar(100) NOT NULL,
  `veg_horticulture` int(1) NOT NULL,
  `cattle_beef` int(1) NOT NULL,
  `dairy` int(1) NOT NULL,
  `poultry` int(1) NOT NULL,
  `hogs` int(1) NOT NULL,
  `goats` int(1) NOT NULL,
  `sheep` int(1) NOT NULL,
  `horses` int(1) NOT NULL,
  `aqua` int(1) NOT NULL,
  `tobacco` int(1) NOT NULL,
  `row_crops` int(1) NOT NULL,
  `rent_lease` varchar(100) NOT NULL,
  `purchase` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `goals` text NOT NULL,
  `where_farming` text NOT NULL,
  `how_sell` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `Landowners`
--

CREATE TABLE `Landowners` (
  `owner_ID` int(11) NOT NULL,
  `terms` varchar(100) NOT NULL,
  `other_desc` text NOT NULL,
  `street` varchar(200) NOT NULL,
  `city` varchar(100) NOT NULL,
  `zip` int(5) NOT NULL,
  `region` varchar(100) NOT NULL,
  `acres` int(255) NOT NULL,
  `pasture` int(255) NOT NULL,
  `tillable` int(255) NOT NULL,
  `woodland` int(255) NOT NULL,
  `housing_desc` text NOT NULL,
  `goals` text NOT NULL,
  `veg_hort` int(1) NOT NULL,
  `beef` int(1) NOT NULL,
  `dairy` int(1) NOT NULL,
  `poultry` int(1) NOT NULL,
  `hogs` int(1) NOT NULL,
  `goats` int(1) NOT NULL,
  `sheep` int(1) NOT NULL,
  `horses` int(1) NOT NULL,
  `aqua` int(1) NOT NULL,
  `tobacco` int(1) NOT NULL,
  `row` int(1) NOT NULL,
  `rent_lease` varchar(200) NOT NULL,
  `purchase` varchar(200) NOT NULL,
  `equipment_desc` text NOT NULL,
  `irrigation` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `photos`
--

CREATE TABLE `photos` (
  `file_location` varchar(600) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `quest` varchar(100) NOT NULL,
  `file_ID` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Applicants`
--
ALTER TABLE `Applicants`
  ADD PRIMARY KEY (`ApplicantID`);

--
-- Indexes for table `Farmers`
--
ALTER TABLE `Farmers`
  ADD PRIMARY KEY (`farmer_ID`),
  ADD KEY `farmer_ID` (`farmer_ID`);

--
-- Indexes for table `Landowners`
--
ALTER TABLE `Landowners`
  ADD PRIMARY KEY (`owner_ID`);

--
-- Indexes for table `photos`
--
ALTER TABLE `photos`
  ADD PRIMARY KEY (`file_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Applicants`
--
ALTER TABLE `Applicants`
  MODIFY `ApplicantID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;
--
-- AUTO_INCREMENT for table `Farmers`
--
ALTER TABLE `Farmers`
  MODIFY `farmer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `Landowners`
--
ALTER TABLE `Landowners`
  MODIFY `owner_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `photos`
--
ALTER TABLE `photos`
  MODIFY `file_ID` int(255) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
