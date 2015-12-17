#!/usr/bin/python2 -O

# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2014-2015  Wojtek Porczyk <woju@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import argparse
import os
import sys

import qubesimgconverter
import qubesimgconverter.imggen

_parser = argparse.ArgumentParser()
_parser.add_argument('-s', '--size', type=int,
    help='Size in pixels')
_parser.add_argument('-c', '--colour', '--color',
    help='Set padlock colour')
_parser.add_argument('-D', '--dispvm', action='store_true',
    help='Generate icon for Disposable VM')
_parser.add_argument('file', metavar='FILE.png',
    help='Destination filename (PNG)')
_parser.set_defaults(
    size=qubesimgconverter.ICON_MAXSIZE,
    colour='0x3465a4',
    dispvm=False
)

def main():
    args = _parser.parse_args()
    qubesimgconverter.imggen.make_padlock(
        args.file, args.colour, size=args.size, disp=args.dispvm)

if __name__ == '__main__':
    main()

# vim: ft=python sw=4 ts=4 et
