CREATE TABLE user_score (
username VARCHAR(40),
score INT(100)
);
ALTER TABLE user_score ENGINE=InnoDB;
ALTER TABLE user_score
	CHANGE COLUMN `username` `username` VARCHAR(40) NOT NULL COLLATE 'utf8mb3_general_ci' FIRST;
ALTER TABLE `user_score`
	ADD CONSTRAINT `FK_user_score_users` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON UPDATE CASCADE ON DELETE CASCADE;
UPDATE users t1
INNER JOIN user_score t2 ON t1.username = t2.username
SET t1.username = t2.username;


