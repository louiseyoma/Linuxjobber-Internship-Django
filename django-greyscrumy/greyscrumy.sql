-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 26, 2018 at 10:13 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `greyscrumy`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add scrumy user', 1, 'add_scrumyuser'),
(2, 'Can change scrumy user', 1, 'change_scrumyuser'),
(3, 'Can delete scrumy user', 1, 'delete_scrumyuser'),
(4, 'Can add goal status', 2, 'add_goalstatus'),
(5, 'Can change goal status', 2, 'change_goalstatus'),
(6, 'Can delete goal status', 2, 'delete_goalstatus'),
(7, 'Can add scrumy goals', 3, 'add_scrumygoals'),
(8, 'Can change scrumy goals', 3, 'change_scrumygoals'),
(9, 'Can delete scrumy goals', 3, 'delete_scrumygoals'),
(10, 'Can add log entry', 4, 'add_logentry'),
(11, 'Can change log entry', 4, 'change_logentry'),
(12, 'Can delete log entry', 4, 'delete_logentry'),
(13, 'Can add permission', 5, 'add_permission'),
(14, 'Can change permission', 5, 'change_permission'),
(15, 'Can delete permission', 5, 'delete_permission'),
(16, 'Can add group', 6, 'add_group'),
(17, 'Can change group', 6, 'change_group'),
(18, 'Can delete group', 6, 'delete_group'),
(19, 'Can add user', 7, 'add_user'),
(20, 'Can change user', 7, 'change_user'),
(21, 'Can delete user', 7, 'delete_user'),
(22, 'Can add content type', 8, 'add_contenttype'),
(23, 'Can change content type', 8, 'change_contenttype'),
(24, 'Can delete content type', 8, 'delete_contenttype'),
(25, 'Can add session', 9, 'add_session'),
(26, 'Can change session', 9, 'change_session'),
(27, 'Can delete session', 9, 'delete_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$KwMjtWZBQA57$QU5mpDTOHAigoVAgeRFLLwQ6AQberU67zs8NbQ3WjuY=', '2018-04-25 20:57:31.246804', 1, 'grey', '', '', 'soguazu@gmail.com', 1, 1, '2018-04-25 07:23:10.807948');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-04-25 07:50:41.824443', '2', 'ScrumyGoals object (2)', 1, '[{\"added\": {}}]', 3, 1),
(2, '2018-04-25 07:50:59.732483', '3', 'ScrumyGoals object (3)', 1, '[{\"added\": {}}]', 3, 1),
(3, '2018-04-26 07:35:56.105763', '4', 'ScrumyUser object (4)', 2, '[{\"changed\": {\"fields\": [\"fullname\"]}}]', 1, 1),
(4, '2018-04-26 07:39:05.203932', '5', 'ScrumyUser object (5)', 3, '', 1, 1),
(5, '2018-04-26 07:46:57.669452', '8', 'ScrumyUser object (8)', 3, '', 1, 1),
(6, '2018-04-26 07:47:12.558018', '7', 'ScrumyUser object (7)', 3, '', 1, 1),
(7, '2018-04-26 07:47:12.609201', '6', 'ScrumyUser object (6)', 3, '', 1, 1),
(8, '2018-04-26 07:47:17.724892', '4', 'ScrumyUser object (4)', 3, '', 1, 1),
(9, '2018-04-26 08:10:36.260100', '14', 'ScrumyUser object (14)', 3, '', 1, 1),
(10, '2018-04-26 08:10:36.356502', '13', 'ScrumyUser object (13)', 3, '', 1, 1),
(11, '2018-04-26 08:10:36.381237', '12', 'ScrumyUser object (12)', 3, '', 1, 1),
(12, '2018-04-26 08:10:36.431646', '11', 'ScrumyUser object (11)', 3, '', 1, 1),
(13, '2018-04-26 08:10:36.615240', '10', 'ScrumyUser object (10)', 3, '', 1, 1),
(14, '2018-04-26 08:10:36.665673', '9', 'ScrumyUser object (9)', 3, '', 1, 1),
(15, '2018-04-26 12:19:30.390599', '26', 'ScrumyUser object (26)', 3, '', 1, 1),
(16, '2018-04-26 12:19:30.468267', '25', 'ScrumyUser object (25)', 3, '', 1, 1),
(17, '2018-04-26 12:19:30.493773', '24', 'ScrumyUser object (24)', 3, '', 1, 1),
(18, '2018-04-26 12:19:30.561403', '23', 'ScrumyUser object (23)', 3, '', 1, 1),
(19, '2018-04-26 12:19:30.643896', '22', 'ScrumyUser object (22)', 3, '', 1, 1),
(20, '2018-04-26 12:19:30.668823', '21', 'ScrumyUser object (21)', 3, '', 1, 1),
(21, '2018-04-26 12:19:30.693972', '20', 'ScrumyUser object (20)', 3, '', 1, 1),
(22, '2018-04-26 12:19:30.719887', '19', 'ScrumyUser object (19)', 3, '', 1, 1),
(23, '2018-04-26 12:19:30.752873', '18', 'ScrumyUser object (18)', 3, '', 1, 1),
(24, '2018-04-26 12:19:30.786219', '17', 'ScrumyUser object (17)', 3, '', 1, 1),
(25, '2018-04-26 12:19:30.811975', '16', 'ScrumyUser object (16)', 3, '', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(4, 'admin', 'logentry'),
(6, 'auth', 'group'),
(5, 'auth', 'permission'),
(7, 'auth', 'user'),
(8, 'contenttypes', 'contenttype'),
(2, 'greyscrumy', 'goalstatus'),
(3, 'greyscrumy', 'scrumygoals'),
(1, 'greyscrumy', 'scrumyuser'),
(9, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-04-25 07:21:06.624829'),
(2, 'auth', '0001_initial', '2018-04-25 07:21:13.464407'),
(3, 'admin', '0001_initial', '2018-04-25 07:21:15.082783'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-04-25 07:21:15.160105'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-04-25 07:21:16.157427'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-04-25 07:21:16.710603'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-04-25 07:21:17.357367'),
(8, 'auth', '0004_alter_user_username_opts', '2018-04-25 07:21:17.409312'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-04-25 07:21:18.027814'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-04-25 07:21:18.078021'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-04-25 07:21:18.130107'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-04-25 07:21:19.253395'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-04-25 07:21:20.300978'),
(14, 'greyscrumy', '0001_initial', '2018-04-25 07:21:23.749393'),
(15, 'greyscrumy', '0002_auto_20180422_2124', '2018-04-25 07:21:24.126798'),
(16, 'sessions', '0001_initial', '2018-04-25 07:21:24.572580'),
(17, 'greyscrumy', '0003_auto_20180425_0821', '2018-04-25 07:22:32.551988');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('supk3ukh4o8n35t9ik8j7usex34z20hn', 'YzUwYzA4ZGQ3MWIwOTRhNGQxNWI5MDA4NGQ2OWQ0ZTZlY2UxMjhjMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTc1NWEzZTU0ZmRkNmNkMmFiMjdmNzljYTI2M2E3MzlkNTE3Mjc0MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-05-09 20:57:31.322104'),
('xka0ja3bb8ltcftzgiosjzkg6lqcnq9s', 'ZjRhNzkxOTg5YTFjZjMwZDMzM2MxNGZhNzBhMTc5NDZlZjVjYWNhMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjU3NTVhM2U1NGZkZDZjZDJhYjI3Zjc5Y2EyNjNhNzM5ZDUxNzI3NDAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-05-09 07:41:17.225222');

-- --------------------------------------------------------

--
-- Table structure for table `greyscrumy_goalstatus`
--

CREATE TABLE `greyscrumy_goalstatus` (
  `id` int(11) NOT NULL,
  `status` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `greyscrumy_goalstatus`
--

INSERT INTO `greyscrumy_goalstatus` (`id`, `status`) VALUES
(1, 'P'),
(2, 'D'),
(3, 'V'),
(4, '');

-- --------------------------------------------------------

--
-- Table structure for table `greyscrumy_scrumygoals`
--

CREATE TABLE `greyscrumy_scrumygoals` (
  `id` int(11) NOT NULL,
  `goal_type` varchar(2) NOT NULL,
  `goal_description` longtext NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_updated` datetime(6) DEFAULT NULL,
  `user_id_id` int(11) NOT NULL,
  `status_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `greyscrumy_scrumygoals`
--

INSERT INTO `greyscrumy_scrumygoals` (`id`, `goal_type`, `goal_description`, `date_created`, `date_updated`, `user_id_id`, `status_id_id`) VALUES
(1, 'WG', 'Testing1', '2018-04-25 07:49:20.989168', '2018-04-25 07:49:34.138393', 1, 1),
(2, 'WG', 'testing2', '2018-04-25 07:50:33.000000', '2018-04-25 11:00:00.000000', 2, 2),
(3, 'DT', 'tesing3', '2018-04-25 07:50:55.000000', '2018-04-25 07:50:58.000000', 3, 3);

-- --------------------------------------------------------

--
-- Table structure for table `greyscrumy_scrumyuser`
--

CREATE TABLE `greyscrumy_scrumyuser` (
  `id` int(11) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `role` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `greyscrumy_scrumyuser`
--

INSERT INTO `greyscrumy_scrumyuser` (`id`, `fullname`, `role`) VALUES
(1, 'Grey White', 'D'),
(2, 'Tobi Alex', 'D'),
(3, 'Kumuri Kushimuri', 'A'),
(15, 'Banky Wale', 'Q');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `greyscrumy_goalstatus`
--
ALTER TABLE `greyscrumy_goalstatus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `greyscrumy_scrumygoals`
--
ALTER TABLE `greyscrumy_scrumygoals`
  ADD PRIMARY KEY (`id`),
  ADD KEY `greyscrumy_scrumygoa_user_id_id_55907669_fk_greyscrum` (`user_id_id`),
  ADD KEY `greyscrumy_scrumygoa_status_id_id_66ac2a7b_fk_greyscrum` (`status_id_id`);

--
-- Indexes for table `greyscrumy_scrumyuser`
--
ALTER TABLE `greyscrumy_scrumyuser`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `greyscrumy_goalstatus`
--
ALTER TABLE `greyscrumy_goalstatus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `greyscrumy_scrumygoals`
--
ALTER TABLE `greyscrumy_scrumygoals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `greyscrumy_scrumyuser`
--
ALTER TABLE `greyscrumy_scrumyuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `greyscrumy_scrumygoals`
--
ALTER TABLE `greyscrumy_scrumygoals`
  ADD CONSTRAINT `greyscrumy_scrumygoa_status_id_id_66ac2a7b_fk_greyscrum` FOREIGN KEY (`status_id_id`) REFERENCES `greyscrumy_goalstatus` (`id`),
  ADD CONSTRAINT `greyscrumy_scrumygoa_user_id_id_55907669_fk_greyscrum` FOREIGN KEY (`user_id_id`) REFERENCES `greyscrumy_scrumyuser` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
