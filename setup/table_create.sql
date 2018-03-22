

CREATE TABLE `device_map` (
  `device_id` int(11) DEFAULT NULL,
  `device_name` text,
  `device_topic` varchar(50) NOT NULL DEFAULT '',
  UNIQUE KEY `device_id` (`device_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `device_map` (`device_id`, `device_name`, `device_topic`)
VALUES
	(1, 'Bathroom', 'lights.bathroom'),
	(2, 'Steps', 'lights.steps'),
	(3, 'Kitchen', 'lights.kitchen');


CREATE TABLE `device_settings` (
  `device_id` int(11) DEFAULT NULL,
  `on_time` time DEFAULT NULL,
  `off_time` time DEFAULT NULL,
  `low` int(11) DEFAULT NULL,
  `high` int(11) DEFAULT NULL,
  `manual` int(11) DEFAULT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `low_time` time DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
