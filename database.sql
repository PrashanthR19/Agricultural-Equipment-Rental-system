/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - farmers
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`farmers` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `farmers`;

/*Table structure for table `farmerreg` */

DROP TABLE IF EXISTS `farmerreg`;

CREATE TABLE `farmerreg` (
  `id` int(200) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `fcontact` varchar(200) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `farmerreg` */

insert  into `farmerreg`(`id`,`name`,`email`,`password`,`fcontact`,`address`,`status`) values (1,'farmer','farmer@gmail.com','1234','9874563210','Guntoor','accepted'),(2,'vish','vish@gmail.com','1234','9874563210','bangalore','accepted');

/*Table structure for table `machinery` */

DROP TABLE IF EXISTS `machinery`;

CREATE TABLE `machinery` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `machineryname` varchar(200) DEFAULT NULL,
  `costwithdriver` varchar(200) DEFAULT NULL,
  `costwithoutdriver` varchar(200) DEFAULT NULL,
  `purpose` varchar(200) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `semail` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `machinery` */

insert  into `machinery`(`id`,`machineryname`,`costwithdriver`,`costwithoutdriver`,`purpose`,`image`,`semail`) values (1,'SPRAYER','3000','2500','Chemical sprayer','Sprayer.jpg','preeti@gmail.com'),(2,'Cultivator','3000','2000','Heavy Duty Loader for land','ripper machine.jpg','preeti@gmail.com'),(3,'Baler','3500','2500','Carrey grass','Baler.jpg','jaya@gmail.com'),(4,'Cultivator','3500','2000','Heavy Duty Loader for land','plough.jpg','jaya@gmail.com');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `Email` varchar(200) DEFAULT NULL,
  `smail` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `cardname` varchar(200) DEFAULT NULL,
  `cardnumber` varchar(200) DEFAULT NULL,
  `expmonth` varchar(200) DEFAULT NULL,
  `cvv` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`id`,`name`,`Email`,`smail`,`amount`,`cardname`,`cardnumber`,`expmonth`,`cvv`,`status`) values (1,'farmer','farmer@gmail.com','preeti@gmail.com','3000','sbi','9632587412365478','2023-07','963','pending'),(2,'farmer','farmer@gmail.com','jaya@gmail.com','2000','canara','6547896547896547','2023-07','258','pending');

/*Table structure for table `reg` */

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `shopename` varchar(200) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `request` varchar(200) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `reg` */

insert  into `reg`(`id`,`name`,`email`,`password`,`contact`,`shopename`,`address`,`request`) values (1,'preeti desai','preeti@gmail.com','1234','4356345765','1234services','bangalore','accepted'),(2,'jaya','jaya@gmail.com','1234','8978978968','kiran machinery','Guntoor','accepted');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `mname` varchar(200) DEFAULT NULL,
  `withdriver` varchar(200) DEFAULT NULL,
  `withoutdriver` varchar(200) DEFAULT NULL,
  `purpose` varchar(200) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `semail` varchar(200) DEFAULT NULL,
  `f_email` varchar(200) DEFAULT NULL,
  `status` varchar(100) DEFAULT 'pending',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`mname`,`withdriver`,`withoutdriver`,`purpose`,`image`,`semail`,`f_email`,`status`) values (1,'SPRAYER','3000','2500','Chemical sprayer','Sprayer.jpg','preeti@gmail.com','farmer@gmail.com','accepted'),(2,'Cultivator','3500','2000','Heavy Duty Loader for land','plough.jpg','jaya@gmail.com','farmer@gmail.com','accepted'),(3,'Cultivator','3500','2000','Heavy Duty Loader for land','plough.jpg','jaya@gmail.com','vish@gmail.com','accepted'),(4,'Cultivator','3000','2000','Heavy Duty Loader for land','ripper machine.jpg','preeti@gmail.com','farmer@gmail.com','accepted'),(5,'Cultivator','3500','2000','Heavy Duty Loader for land','plough.jpg','jaya@gmail.com','farmer@gmail.com','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
