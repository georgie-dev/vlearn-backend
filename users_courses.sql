-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 04, 2023 at 09:06 PM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vlearn`
--

-- --------------------------------------------------------

--
-- Table structure for table `users_courses`
--

DROP TABLE IF EXISTS `users_courses`;
CREATE TABLE IF NOT EXISTS `users_courses` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `courseCode` varchar(10) NOT NULL,
  `courseStatus` varchar(2) NOT NULL,
  `courseTitle` varchar(100) NOT NULL,
  `courseUnit` int NOT NULL,
  `semester` varchar(100) NOT NULL,
  `level` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_courses_courseCode_48cd732c_uniq` (`courseCode`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users_courses`
--

INSERT INTO `users_courses` (`id`, `courseCode`, `courseStatus`, `courseTitle`, `courseUnit`, `semester`, `level`, `department`) VALUES
(1, 'CHM 101', 'C', 'General Chemistry I', 3, 'First Semester', '100 Level', 'Software Engineering'),
(2, 'BIO 101', 'C', 'General Biology I', 3, 'First Semester', '100 Level', 'Software Engineering'),
(3, 'MTH 101', 'C', 'Elementary Mathematics I', 3, 'First Semester', '100 Level', 'Software Engineering'),
(4, 'GST 103', 'R', 'Library Study and ICT Skills', 2, 'First Semester', '100 Level', 'Software Engineering'),
(5, 'GST 105', 'R', 'Philosophy and Logic', 2, 'First Semester', '100 Level', 'Software Engineering'),
(6, 'GST 101', 'R', 'Use of English 1', 2, 'First Semester', '100 Level', 'Software Engineering'),
(7, 'CSC 101', 'C', 'Introduction to Computer Science', 3, 'First Semester', '100 Level', 'Software Engineering'),
(8, 'MTH 103', 'C', 'General Mathematics II', 3, 'First Semester', '100 Level', 'Software Engineering'),
(9, 'PHY 101', 'C', 'General Physics I', 3, 'First Semester', '100 Level', 'Software Engineering'),
(10, 'PHY 107', 'C', 'General Physics Laboratory I', 1, 'First Semester', '100 Level', 'Software Engineering'),
(11, 'CSC 102', 'C', 'Programming Logic & Design', 2, 'Second Semester', '100 Level', 'Software Engineering'),
(12, 'CYB 102', 'C', 'Introduction to Software Applications and Cyber security', 2, 'Second Semester', '100 Level', 'Software Engineering'),
(13, 'GST 102', 'C', 'Use of English II', 2, 'Second Semester', '100 Level', 'Software Engineering'),
(14, 'GST 104', 'C', 'Nigerian Peoples and Culture', 2, 'Second Semester', '100 Level', 'Software Engineering'),
(15, 'GST 108', 'C', 'History & Philosophy of Science', 2, 'Second Semester', '100 Level', 'Software Engineering'),
(16, 'MTH 102', 'C', 'Elementary Mathematics 3 (Calculus)', 3, 'Second Semester', '100 Level', 'Software Engineering'),
(17, 'PHY 102', 'C', 'General Physics II', 3, 'Second Semester', '100 Level', 'Software Engineering'),
(18, 'PHY 108', 'C', 'General Physics Laboratory II', 1, 'Second Semester', '100 Level', 'Software Engineering'),
(19, 'STA 102', 'C', 'Statistics & Probability', 2, 'Second Semester', '100 Level', 'Software Engineering');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
