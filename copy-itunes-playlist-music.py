#!/usr/local/bin/python3
###########
## 
## This script copies music files from an iTunes playlist to another location
## 
## argument 1 - the itunes playlist file
## argument 2 - the location to copy music to
## 
###############

import sys
import os
import csv
from shutil import copyfile

def makeUniqueFile(path):
    origName, origExt = os.path.splitext(path)
    counter = 1
    while True:
        if os.path.exists(path):
            path = origName + '_' + str(counter) + origExt
            counter += 1
        else:
            return path

debug = False

if len(sys.argv) < 3:
    print("usage: " + sys.argv[0] + " <itunes-playlist-export-txt-file> <copy-destination>")
    exit(1)

destinationFolder = sys.argv[2]

if not os.access(destinationFolder, os.W_OK):
    print("Destination folder may not exist or allow us to write files")
    exit(1)

with open(sys.argv[1], newline='', encoding='utf-16') as f:
    next(f)
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        musicFile = row[-1]
        if musicFile == "":
            print(f'Could not find {row[1]}')
            continue
        musicFile = musicFile[musicFile.find('/'):]
        print(f'musicfile: {musicFile}')
        destFile = os.path.split(musicFile)[1]
        destination = os.path.join(destinationFolder, destFile)
        print(f'Destination: {destination}')
        if os.access(musicFile, os.R_OK):
            if debug:
                destination = makeUniqueFile(destination)
                print(f'would have copied {musicFile} to {destination}')
            else:
                destination = makeUniqueFile(destination)
                print(f'copying {musicFile} to {destination}')
                copyfile(musicFile, destination)
        elif debug:
            print(f"could not locate {musicFile}")
            print("debug ---row---")
            print(row)
