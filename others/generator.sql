SET @@global.sql_mode= '';

DROP DATABASE IF EXISTS `registrar`; CREATE DATABASE `registrar`; USE `registrar`; DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,`name` varchar(255) default NULL,  `phone` varchar(100) default NULL,  `email` varchar(255) default NULL,  `postal_zip` varchar(10) default NULL,  `country` varchar(100) default NULL,  `grade_letter` TEXT default NULL,  `grade_percent` mediumint default NULL,  PRIMARY KEY (`id`)) AUTO_INCREMENT=1;

INSERT INTO `students` (`students_name`,`students_phone`,`students_email`,`students_postal_zip`,`students_country`,`students_grade_letter`,`students_grade_percent`)
VALUES  ("Iona","(959) 862-2103","est.mauris@aenean.edu","57547","Mexico","B",68),  ("Raphael","1-465-663-9457","a.feugiat@ullamcorpernisl.co.uk","222349","Peru","B",16),  ("Dora","1-462-404-5502","erat@ipsum.com","855382","Canada","B",83),  ("Tad","(358) 818-0731","sem.eget@arcueu.ca","31329","United Kingdom","B",56),  ("Moses","1-851-695-6624","ac.turpis.egestas@blandit.org","25786","Ireland","B",2),  ("Brenda","(513) 177-5319","id.libero@mauris.ca","63614","Nigeria","A",84),  ("Carlos","1-969-747-7778","placerat.cras.dictum@bibendumsedest.com","7441","Pakistan","C",62),  ("Barrett","1-326-478-2262","placerat.orci@nibhvulputate.org","35687","Mexico","B",40),  ("Ariel","(668) 313-5375","odio.tristique@sagittisfelis.org","84455-58419","Austria","B",91),  ("Fiona","(751) 449-7282","rhoncus.donec@mi.ca","51208","Pakistan","A",60);

INSERT INTO `students` (`students_name`,`students_phone`,`students_email`,`students_postal_zip`,`students_country`,`students_grade_letter`,`students_grade_percent`)
VALUES ("Irene","1-281-229-7015","nulla.magna@magnasuspendisse.co.uk","12731","Vietnam","B",25), ("Emi","1-541-811-7164","scelerisque.dui@in.edu","78-430","Germany","A",57), ("Wylie","(358) 619-2564","semper.rutrum.fusce@auctormauris.org","6281","Austria","B",13), ("Ira","1-676-162-1323","cras@malesuadavel.ca","356100","Turkey","B",41), ("Hedy","(956) 888-5721","dui.semper@anteipsum.ca","4464","New Zealand","B",10), ("Lucius","1-564-582-2658","cum.sociis@odio.net","2229","Mexico","B",78), ("Derek","1-584-956-6583","at.iaculis@erosnectellus.net","97364","Turkey","C",47), ("Ignatius","1-365-323-7119","ligula.donec@nibhdonec.ca","NM1 9YB","United States","A",35), ("Clarke","(843) 142-8363","consectetuer@sodalesnisi.com","85138-88772","Pakistan","C",20), ("Carolyn","1-651-767-8767","vehicula.pellentesque.tincidunt@aliquam.co.uk","5103","Austria","B",3);