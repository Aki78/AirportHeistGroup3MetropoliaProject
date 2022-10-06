load data local infile '../eu_airports_3rd_attempt.csv'
into table eu_airports
character set utf8
fields terminated by ','
optionally enclosed by '"'
lines terminated by '\n'
ignore 1 lines;
