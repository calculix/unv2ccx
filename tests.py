# -*- coding: utf-8 -*-

"""
    © Ihor Mirzov, April 2019
    Distributed under GNU General Public License v3.0

    Usage:
        python3 tests.py
"""

import subprocess, os, clean


# List all .ext-files here and in all subdirectories
def listAllFiles(startFolder, ext):
    all_files = []
    for f in os.listdir(startFolder): # iterate over files and folders in current directory
        f = os.path.abspath(startFolder + '/' + f)
        if os.path.isdir(f): # if folder
            for ff in listAllFiles(f, ext):
                all_files.append(ff)
        elif f.endswith(ext):
            all_files.append(f) # with extension
    return all_files


if (__name__ == '__main__'):
    clean.screen()
    extension = ('.exe' if os.name=='nt' else '') # file extension in OS

    # Convert calculation results
    for filename in listAllFiles('./tests', '.unv'):
        subprocess.run('python3 unv2ccx.py ' + filename, shell=True)
        # if os.name == 'nt':
        #     subprocess.run('unv2ccx.exe ' + filename, shell=True)
        # else:
        #     subprocess.run('./unv2ccx ' + filename, shell=True)
        # break # one file only

    clean.cache()
    clean.files('.')
