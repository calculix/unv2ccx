#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, 2019-2020
Distributed under GNU General Public License v3.0

Converts UNV file from Salome to CalculiX INP mesh:
python3 ./unv2ccx/__init__.py ./examples/116.unv

Reads UNV_file, creates an internal FEM object,
then writes the INP_file. """

import os
import sys
import argparse
import logging

sys_path = os.path.abspath(__file__)
sys_path = os.path.dirname(sys_path)
sys.path.insert(0, sys_path)
import clean
import reader
import writer


class Converter:

    def __init__(self, unv_file_name):
        self.unv_file_name = os.path.normpath(unv_file_name)
        self.inp_file_name = self.unv_file_name[:-4]+'.inp'

    def run(self):

        # Read UNV file
        base_name = os.path.basename(self.unv_file_name)
        logging.info('Reading ' + base_name)
        fem = reader.UNV(self.unv_file_name).read()

        # Write INP file
        base_name = os.path.basename(self.inp_file_name)
        logging.info('Writing ' + base_name)
        writer.write(fem, self.inp_file_name)


if __name__ == '__main__':
    clean.screen()

    # Configure logging
    logging.basicConfig(level=logging.INFO,
        format='%(levelname)s: %(message)s')

    # Command line parameters
    ap = argparse.ArgumentParser()
    ap.add_argument('filename', type=str,
        help='UNV file name with extension')
    args = ap.parse_args()

    # Create converter and run it
    unv2ccx = Converter(args.filename)
    unv2ccx.run()

    clean.cache()
