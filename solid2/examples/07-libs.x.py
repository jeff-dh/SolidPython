#! /usr/bin/env python

from solid2 import *

# you can use OpenSCAD libraries in SolidPython. This examples needs the bosl
# library to be installed in the OpenSCAD library path
# (~.local/share/OpenSCAD/libraries)
#
# NOTE: you can import any *.scad file not only "libraries"

#import bosl.metric_screw
metric_screws = import_scad("BOSL/metric_screws.scad")

#use it to generate a metric screw
screw = metric_screws.metric_bolt(size=6, headtype='hex', l=20)

screw.save_as_scad()

#NOTE: BOSL2 see 07-libs-bosl2.py
