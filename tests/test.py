#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, July 2020
Distributed under GNU General Public License v3.0

Test UNV converter on examples
Ctrl+F5 from VSCode to run """

import os
import sys
import time
import logging
import subprocess

sys_path = os.path.abspath(__file__)
sys_path = os.path.dirname(sys_path)
sys_path = os.path.join(sys_path, '..')
sys_path = os.path.normpath(sys_path)
sys.path.append(sys_path)

import unv2ccx
from unv2ccx import clean
from log import myHandler, print

# How many files to process
limit = 100

# List all .ext-files here and in all subdirectories
def scan_all_files_in(start_folder, ext):
    start_folder = os.path.normpath(start_folder)
    all_files = []
    for f in os.scandir(start_folder):
        if f.is_dir():
            for ff in scan_all_files_in(f.path, ext):
                all_files.append(ff)
        elif f.is_file() and f.name.endswith(ext):
            all_files.append(f.path)
    return sorted(all_files)[:limit]

# Convert UNV files
def convert_unv_files_in(folder):
    print('UNV CONVERTER TEST\n\n')
    start = time.perf_counter() # start time
    for file_name in scan_all_files_in(folder, '.unv'):
        print('\n' + '='*50)
        unv2ccx.Converter(file_name).run()
    print('\nTotal {:.1f} seconds'.format(time.perf_counter() - start))

# Convert calculation results with binaries
def test_binary_in(folder):
    print('UNV CONVERTER TEST\n\n')
    start = time.perf_counter() # start time
    for file_name in scan_all_files_in(folder, '.unv'):
        if os.name == 'nt':
            command = 'bin\\unv2ccx.exe'
        else:
            command = './bin/unv2ccx'
        print('\n' + '='*50)
        subprocess.run([command, file_name])
    print('\nTotal {:.1f} seconds'.format(time.perf_counter() - start))

if (__name__ == '__main__'):
    clean.screen()

    # Prepare logging
    logging.getLogger().addHandler(myHandler())
    logging.getLogger().setLevel(logging.INFO)

    folder = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(folder, '..', 'examples')
    # test_binary_in(folder)
    convert_unv_files_in(folder)

    clean.cache()
