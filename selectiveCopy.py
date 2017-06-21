#! /usr/bin/env python3
# selectiveCopy.py - Searches for files with a certain file extension
# and copies them in to a new folder

import shutil, os, re

folder = input('Path to the folder: ')
extension = input('Extension starting with a dot:')

def selectiveCopy(folder, extension):
    folder = os.path.abspath(folder)
    newfolder = 'copies of ' + extension[1:] + ' files by Python'
    os.makedirs(newfolder)
    newfolder = os.path.abspath(newfolder)
    print('Copying all files with the extension %s in to \'%s\'...' % (extension, newfolder))

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('_copy' + extension):
                continue
            if filename.endswith(extension): 
                regex = re.compile(r'(.*)(%s$)' % extension)
                mo = regex.search(filename)
                currentFile = foldername + '/' + filename
                newfileName = newfolder + '/' + mo.group(1) + '_copy' + extension
                shutil.copy(currentFile, newfileName)

selectiveCopy(folder, extension)
