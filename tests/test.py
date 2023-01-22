#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, 2019-2023
Distributed under GNU General Public License v3.0

Test unv2ccx converter on examples
Ctrl+F5 to run in VSCode"""

import os
import sys
import time
import logging
import subprocess
import traceback

sys_path = os.path.abspath(__file__)
sys_path = os.path.dirname(sys_path)
sys_path = os.path.join(sys_path, '..')
sys_path = os.path.normpath(sys_path)
sys.path.insert(0, sys_path)

import unv2ccx
from unv2ccx import clean
from log import myHandler, print, read_and_log

# How many files to process
limit = 10000


# List all .ext-files here and in all subdirectories
def scan_all_files_in(start_folder, ext):
    all_files = []
    for f in os.scandir(start_folder):
        if f.is_dir():
            for ff in scan_all_files_in(f.path, ext):
                all_files.append(ff)
        elif f.is_file() and f.name.endswith(ext):
            ff = os.path.normpath(f.path)
            all_files.append(ff)
    return sorted(all_files)[:limit]


# Convert UNV files
def convert_unv_files_in(folder):
    print('CONVERTER TEST\n\n')
    counter = 0
    for file_name in scan_all_files_in(folder, '.unv'):
        counter += 1
        relpath = os.path.relpath(file_name, start=folder)
        print('\n{}\n{}: {}'.format('='*50, counter, relpath))
        try:
            unv2ccx.Converter(file_name).run()
        except:
            logging.error(traceback.format_exc())


# Convert calculation results with binaries
def test_binary_in(folder):
    print('CONVERTER TEST\n\n')
    counter = 0
    for file_name in scan_all_files_in(folder, '.unv'):
        counter += 1
        if os.name == 'nt':
            command = 'bin\\unv2ccx.exe'
        else:
            command = './bin/unv2ccx'
        relpath = os.path.relpath(file_name, start=folder)
        print('\n{}\n{}: {}'.format('='*50, counter, relpath))
        cmd = [command, file_name]
        try:
            process = subprocess.Popen(cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT)
            read_and_log(process.stdout)
        except:
            logging.error(traceback.format_exc())


# Run
if __name__ == '__main__':
    start = time.perf_counter()
    clean.screen()

    # Prepare logging
    logging.getLogger().addHandler(myHandler())
    logging.getLogger().setLevel(logging.DEBUG)

    folder = os.path.abspath(__file__)
    folder = os.path.dirname(folder)
    folder = os.path.join(folder, '..', 'examples')
    folder = os.path.normpath(folder)

    # Choose what we test
    convert_unv_files_in(folder)
    # test_binary_in(folder)

    print('\nTotal {:.1f} seconds'.format(time.perf_counter() - start))
    clean.cache()
