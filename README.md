# Folder-Organizer

A simple script that enables the rapid organisation of the different type of files in a folder

## How to use

- Run the script.
- You'll be prompted to enter the path to the folder you want to organize.
- Go to that folder and copy the path to the folder.
- Paste the path to the folder and press enter.

## What it does 

- The script will try creating 3 folders (If they do not exist yet).
- The folders are: 
    - A Document folder.
    - An Image folder.
    - A Video folder.
- The script will iterate throught the main folder and read the extensions of the files  in the folder.
- If an extension corresponds to the a value in the categories dictionary, that file is sent to the folder whose name is the same as the key to which that extension belongs.