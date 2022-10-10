# Airport Heist


<p align="center">
    <img src="./hud.gif">
</p>


## Contents
#### [Introduction](#introduction)

#### [Vision](#vision)

[Backstory](#backstory)
    -Setting

[Functional Requirements](#functional-requirements)

    -How the game works
    -Block diagram
    -Functions
    -Project diagram

[Quality Requirements](#quality_requirements)

    -Preliminary requirements
    -Final requirements

[Learning Tools And Information](#learning-tools-and-information)

    -Run
    -Useful git commands
    -Useful bash commands
    -Project information
    -Unrelated English project

## Introduction
This document specifies the design for the gameplay of Airport Heist.
The key developers are Aki Morooka, Khai cao, Kiana Aghajani and Francesco Natanni.

## Vision
The Purpose of Airport Heist is to produce a fun and interactive game, 
that satisfies the guidelines provided by software1.

#### Backstory
You are a master thief, captured by the Finnish authorities on the minor charge of jaywalking.
They have no idea of your genius though and neglect to watch over you properly.
You make a daring, yet surprisingly easy escape from Jokela Prison and are now on the run! 
You need to get out of Finland A.S.A.P though as the finnish authorities will stop at nothing to bring you to justice. 

Due to your expert skills you are able to steal 10,000€ from the Alepa at Helsinki Airport. 
The police, however, have been alerted of your activities and are hot on your tail.
Time to make your next move before interpol gets you!

#### Setting
Airport Heist is set in present-day Europe.

## Functional Requirements
### How the game works
Airport Heist is a single player game, where the main character aims to make it to the final destination airport, before they are captured or their stamina or money runs out.

#### Travel

Players start in Helsinki, Finland and must end up in the destination airport provided by the game. This airport is generated at random. Travel is possible with the purchase of a flight ticket.
Players are also restricted to airports with-in a certain distance from their current location and all airports are wih-in the EU. The ristricted travel distance is dependent on the game's difficulty selected. Players are shown a list of countries with-in their travel range.

#### Evading Capture

Players can see in which city interpol is but not exactly where interpol will be at next.
Players will see a list of possible airports interpol will be at next.
Interpol moves from airport to airport at random. Interpol only move each time the player makes a decision. 

#### Stamina

Players start with a set amount of stamina at the beginning of the game. Each time the player travels they use up stamina. How much stamina they use is dependant and the length of the flight. Stamina does not regenerate, so you must make it to your final destination before it runs out completely.

#### Stealing

The player starts with a set amount of money, which is again dependant on the game's difficulty selected.If the player needs more money to buy flight tickets players steal. There is, however, a chance of getting caught. Players are informed of the odds of capture before they attempt a heist and can abort if they feel the risks are too great. Players have 5 attempts to steal. 
If they use all 5 attempts before escaping, they will be caught and the game is over. The players stolen earnings are based on gauss' theory with two different expectation values,
depending on the game's difficulty selected.


The game is over when the player is either caught by interpol, run out of money or run out of stamina. 

[Back to top](#airport-heist)

### Block Diagram
 The decision tree below show all possible decisions the player can make and the benefits of each. 


<p align="center">
    <img src="./block_diagram2.png">
</p>

The user is able to do two things: 

    -choose where they travel to
    -choose if they wish to rob the airport they are currently in.

### Functions
Listed below are all the funtctions that were created for the game:
#### core_test Functions
    -init_state
    -run_game

#### Helper Functions
    -feet_to_meters
    -meters_to_kilometers
    -get_distances
    -get_possible_flights
    -print_possible_flights
    -print_flight_details
    -deg_to_xy
    -get_min_max_distance

#### Database Functions
    -get_new_coordinates
    -get_geo_sirport_info
    -get_airport_name
    -get_coordinates
    -get_datalist

#### Decisions
    -mode
    -heist_decision
    -money_heist
    -escape
    -player_airport_selection

#### Game Functions
    -theft_success_earnings_gauss
    -theft_success_rate
    -get_ticket_price
    -get_stamina_consumptions
    -interpol_index
    -update_player

#### Interpol
    -interpol_position_and_movement
    -update

#### Prints
    -print_start
    -print_instructions
    -print_settings
    -print_credits
    -print_player_position
    -print_mainmenu
    -steal_rate_and_decision(the be changed)

#### Tests
    -test_feet_to_meters
    -test_meters_to_km
    -test_get_distances

### Project Diagram
This diagram shoes how our different python files interact with each other to make our game work.

<p align="center">
    <img src="./project_diagram.png">
</p>

[Back to top](#airport-heist)

## Quality Requirements
#### Preliminary Requirements
All helper functions created were ran through pytest to ensure proper working order.
The database was cut down, to remove a lot of unnecessary information and to make calling upon the database faster.

#### Final Requirements
The visuals for the user experience must be pleasing and the animated motion must be smooth. Loading time must not excede more than a couple seconds on a typical laptop computer. The game should never freeze. The game must run on at least 30 fps. The final product must be accesible online.

[Back to top](#airport-heist)

## Learning Tools And information
### Run
If you are using Mac/Linux run
```bash
python3 connect_py.py
```

If you are using Windows run
```bash
py -3 connect_py.py
```

Make sure your local user name and password are root and root.
Make sure the sql database name and table names match exactly.

### Useful Git Commands

```bash
git pull (saves from github)

git add . (all files)
git commit -m "discription of changes" (add your changes to local git history)
git push (pushs to the repository)

git rm file_name (removes file_name)

git stash (restore everythiing to last commit)

git status (shows your current git state)

git clone repo_name (when you want to copy a repo and add it your computer)
```

### Useful Bash Commands
```bash
pwd                               takes you to curent directory
cd [name of directory]            change directory
cd ~ 		                  takes you home
cd mouseless	                  takes the path to mouseless if its directly under your home (~this symbol is the same as writing c:/user/murph)
ls 			          list directory and files in the directory
mkdir [name of directory]         makes a directory
touch [name of file]	          creates a file in the current directory 
mv file.txt mouseless	          move file to somewhere
mv file.txt file.py	          renames file from txt to py
cd ..			          .. means back one directory

DANGER COMMANDS
rm file.py		          removes file named (only for files not directory)
rmdir			          removes and empty directory only
rm -r [name of directory] removes directory and everything in it
rm -rf name		          remove recurssive force name of directoty
rm *				  this will delete all files only! so make sure youre in the right directory
rm -r * 			  deletes everything in directory including other directories
rm -r *4*			  deletes everything that has a 4 in it
find . -name "*3*.py"	          find files with 3 and .py in it
find . -name "*3*.py" -delete	  find files with 3 and .py in it and then deletes it
cat main.py						  will print out whats inside the file

control-c			  stop command
py -3 filename.py		  runs python program that is in the file in your terminal (windows only)
python3 filename.py		  runs python program that is in the file in your terminal (linux/Mac)

grep -r [expression]              finds the file where the expression exists
```

### Project Info
https://github.com/vesavvo/Python_Ohjelmistoteema/tree/main/English/Project

### Unrelated English Presentation on Tesla
https://docs.google.com/presentation/d/1TpIigIBr3PJndSA2aOSsjrBivZLBFT9-3XDx2xj_RbI/edit#slide=id.p

[Back to top](#airport-heist)