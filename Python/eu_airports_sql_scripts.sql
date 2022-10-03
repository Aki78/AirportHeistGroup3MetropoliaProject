/*code used to create new database*/
create database eu_flight_game;
use eu_flight_game;

create table eu_airports (
id int(11) not NULL,
ident varchar(40) DEFAULT NULL,
name varchar(40) DEFAULT NULL,
country_name VARCHAR(40) DEFAULT NULL,
iso_country varchar(40) DEFAULT NULL,
latitude_deg double DEFAULT NULL,
longitude_deg double DEFAULT NULL,
elevation_ft int(11) DEFAULT NULL,
municipality varchar(40) DEFAULT NULL,
PRIMARY KEY (ident));

select *
from airport
WHERE airport.continent = 'EU' AND scheduled_service = 'yes' AND TYPE = 'large_airport'
group BY iso_country
order BY id asc