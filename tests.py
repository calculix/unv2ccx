# -*- coding: utf-8 -*-

"""
    © Ihor Mirzov, April 2019
    Distributed under GNU General Public License, version 3.

    python3 tests.py
"""

import subprocess, os, clean


# List all .inp-files here and in all subdirectories
def listAllFiles(startFolder, fmt):
    all_files = []
    for f in os.listdir(startFolder): # iterate over files and folders in current directory
        f = os.path.abspath(startFolder + '/' + f)
        if os.path.isdir(f): # if folder
            for ff in listAllFiles(f, fmt):
                all_files.append(ff)
        elif f[-4:] == fmt:
            all_files.append(f[:-4])
    return all_files


if (__name__ == '__main__'):
    clean.screen()

    # Convert calculation results
    for modelname in listAllFiles('./tests-elements', '.unv'):
        subprocess.run('python3 unv2ccx.py {0}.unv {0}.inp'.format(modelname), shell=True)
        # break # one file only

    clean.cache()
    clean.files('.')
