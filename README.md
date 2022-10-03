# Airport Heist
## Contents
    -Introduction
    -Vision
    -Story
    -Functional Requirements
    -Task Stack
    -Learning Tools And Information

## Introduction
This document specifies the design for the gameplay of Airport Heist.
The key developers are Aki Morooka, Khai cao, Kiana Aghajani and Francesco Natanni.

## Vision
Airport Heist is a single player game, where the main character aims to avoid capture as they make their way across europe.
Players are limited by their budget but can steal their way to fortune or to ruin!
Players start in Helsinki, Finland and the game ends when they are either caught by interpol or run out of money.


The Purpose of Airport Heist is to produce a fun and interactive game, 
that satisfies the guidelines provided by software1.

What does this mean?

    -The vision can be presented also as a figure that is supported by a written description. 
    -Here you must explain the main idea of the game in your own words: 
    -how does the game proceed and what stages must the player go through?

As the game progresses the player take chances by stealing money to increase their wealth
and then making strategic moves to avoid arrest.

## Story
### Backstory
You are a master thief, captured by the Finnish authorities on the minor charge of jaywalking.
They have no idea of your genius though and neglect to watch over you properly.
You make a daring, yet surprisingly easy escape from Jokela Prison and are now on the run! 
You need to get out of Finland A.S.A.P though as the finnish authorities will stop at nothing to bring you to justice. 
Due to your expert skills you are able to steal 1000€ from the Alepa at Helsinki Airport. 
The police, however, have been alerted of your activities and are hot on your tail.
Time to make your next move before interpol gets you!

### Setting
Airport Heist is set in present day Europe.

## Functional Requirements
Chapter 3 (Functional requirements) discusses everything the user can do with the game. 
The functional requirements are typically presented as user stories with a role (who), 
action (what), and benefit (why). 
An example of a user story would be "As a player I can choose the next airport from the cities showing on the map, 
so that my electric airplane will move there.". 
The example user story contains a role (player), an action (selecting the next city) 
and a benefit the user can gain by completing the action (moving to the new location). 
There are enough user stories when they together describe all functionality of the game. 
For the flight simulator this probably means dozens of user stories. 
Each user story must be unambiguous and concrete. 
It must be possible to look back at the user stories later to determine whether each planned functionality has been implemented in the software.

The user is able to do two things: choose where they travel to and if they wish to rob the airport they are currently in.
Where they travel to is limited by budget and distance.
Thievery is down to luck.

### Core Functions
    -Print main menu
    -Print settings
    -Print instructions
    -Print credits
    -Run game

### Helper Functions
    -Convert feet to meters
    -Convert meters to kilometers
    -Get the distance between two lat and long co-ordinates
    -Returns all the possible flights from a given airport
    -Convert lat and long degrees to x and y co-ordinates
    -Compares every airport against every airport and return a max and min distance

### Other Game Functions
    -Uses Gauss theory to predict theft success earnings
    -Random generator to determine if the theft is successful
    -A function that uses distance to calculate the cost of a flight

## Task Stack
 | Task                                          | Name               | 
 |-----------------------------------------------|--------------------|
 | write report                                  | Frank              |
 | make a diagram                                | Kiana              |
 | game rules                                    | Kiana              |

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
git pull (saves to github)

git add . (all files)
git commit -m "discription of changes" (add your changes to local git history)
git push (pushs to the repository)

git rm file_name (removes file_name)

git stash (restore everythiing to last commit)

git status (shows your current git state)

git clone repo_name (when you want to copy a repo and add it your computer)
```

### Project Info
https://github.com/vesavvo/Python_Ohjelmistoteema/tree/main/English/Project

### English Presentation on Tesla
https://docs.google.com/presentation/d/1TpIigIBr3PJndSA2aOSsjrBivZLBFT9-3XDx2xj_RbI/edit#slide=id.p


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
