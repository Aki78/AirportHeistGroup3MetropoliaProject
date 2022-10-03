# Airport Heist
## Introduction
This document specifies a design for the gameplay of Airport Heist.
The key developers of this game are Aki Morooka, Khai cao, Kiana Aghajani and Francesco Natanni.

## Specification
Airport Heist is a single player game, where the main character aims to avoid capture as they make their way across europe.
Players are limited by their budget but can steal their way to fortune or be ruined!
Players start in Helsinki, Finland and the game ends when you are either caught by interpol or run our of money.

## Story
### Backstory
You are a master thief, captured by the Finnish authorities on a minor charge.
They have no idea of your genius though and neglect to watch over you properly.
You make a daring, yet surprisingly easy escape from Jokela Prison and are now on the run! 
You need to get out of Finland fast though as the finnish authorities will stop at nothing to save face. 
Due to your expert skills you are able to steal 1000€ from the Alepa at Helsinki Airport without being noticed.
Time to make your next move before interpol gets you!

### Setting
Airport Heist is set in present day Earth.

###

## Task Stack
 | Task                                          | Name               | 
 |-----------------------------------------------|--------------------|
 | write report                                  | Frank              |
 | make a diagram                                | Kiana              |
 | game rules                                    | Kiana              |

## Run
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

## Useful Git Commands

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

## Project Info
https://github.com/vesavvo/Python_Ohjelmistoteema/tree/main/English/Project

## Unrelated Presentation
https://docs.google.com/presentation/d/1TpIigIBr3PJndSA2aOSsjrBivZLBFT9-3XDx2xj_RbI/edit#slide=id.p


## Useful Bash Commands

```bash
pwd 					takes you to curent directory
cd [name of directory] 				change directory
cd ~ 					takes you home
cd mouseless			takes the path to mouseless if its directly under your home (~this symbol is the same as writing c:/user/murph)
ls 						list directory and files in the directory
mkdir [name of directory] 			makes a directory
touch [name of file]			creates a file in the current directory 
mv file.txt mouseless	move file to somewhere
mv file.txt file.py		renames file from txt to py
cd ..					.. means back one directory

(danger commands)
rm file.py							removes file named (only for files not directory)
rmdir								removes and empty directory only
rm -r [name of directory]							removes directory and everything in it
rm -rf name							remove recurssive force name of directoty
rm *								this will delete all files only! so make sure youre in the right directory
rm -r * 							deletes everything in directory including other directories
rm -r *4*							deletes everything that has a 4 in it
find . -name "*3*.py"				find files with 3 and .py in it
find . -name "*3*.py" -delete		find files with 3 and .py in it and then deletes it
cat main.py							will print out whats inside the file

control-c							stop command
py -3 filename.py					runs python program that is in the file in your terminal (windows only)
python3 filename.py					runs python program that is in the file in your terminal (linux/Mac)

grep -r [expression]                            finds the file where the expression exists
```
