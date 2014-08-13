CREATE TABLE `firstnames` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      `firstname` varchar(255) default NULL,
      `sex` varchar(10) default NULL
);

CREATE TABLE `lastnames` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      `lastname` varchar(255) default NULL,
      `sex` varchar(10) default NULL
);

CREATE TABLE `fathersname` (
      `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      `fathersname` varchar(255) default NULL,
      `sex` varchar(10) default NULL
);
