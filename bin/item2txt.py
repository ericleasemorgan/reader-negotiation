#!/usr/bin/env python

# configure
TXT       = './txt'
EXTENSION = '.txt'
ITEM      = 'chapter_057-anger'

# require
from pathlib import Path

# initialize
file = Path( TXT )/( ITEM + EXTENSION )

# read the computed file
with open( file ) as handle : text = handle.read()

# output and done
print( text )
exit()