drop database if exists flight_game;

create database flight_game;
use flight_game;

set foreign_key_checks=0;

create table airport(
id int,
ident varchar(200),
type varchar(200) default null,
name varchar(200),
latitude_deg float(53),
longitude_deg float(53),
elevation_ft int,
continent varchar(200),
iso_country varchar(200) not null,
iso_region varchar(200),
municipality varchar(200),
scheduled_service varchar(200),
gps_code varchar(200),
iata_code varchar(200),
local_code varchar(200),
home_link varchar(200),
wikipedia_link varchar(200),
keywords varchar(200),
primary key (ident)
);

create table goal(
id int not null,
name varchar(200),
description varchar(200),
icon varchar(200),
target varchar(200),
target_minvalue float(53),
target_maxvalue float(53),
target_text varchar(200),
primary key (id)
);

create table game(
id int not null,
co2_consumed float(53),
co2_budget float(53),
screen_name varchar(200),
location varchar(200),
primary key (id)
);

create table goal_reached(
goal_id int not null,
game_id int not null,
primary key (goal_id, game_id),
-- primary key (goal_id),
foreign key (goal_id) references goal(id),
foreign key (game_id) references game(id)

);

create table country(
id int not null,
code varchar(200),
name varchar(200),
continent varchar(200),
wikipedia_link varchar(200),
keywords varchar(200)
);

load data local infile './airports.csv'
into table airport
character set utf8
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;

load data local infile './countries.csv'
into table airport
character set utf8
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;

alter table country
drop column id;
alter table country
change code iso_country varchar(200);
alter table country
add primary key(iso_country);

alter table airport
add foreign key (iso_country) references country (iso_country);

alter table game
add foreign key (location)
references airport (ident);

insert into game (id, co2_consumed, co2_budget, screen_name, location)
values (1, 2000, 10000, 'Heini', 'EFHK'),
(2, 3000, 10000, 'Vesa', 'EGCC' ),
(3, 8000, 10000, 'Ilkka', 'EGKK');

insert into goal_reached(goal_id, game_id)
values (1,4),
(1,7),
(2,4),
(3,7);
