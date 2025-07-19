#!/usr/bin/env python

# slideshow.py - given the name of a study carrel, create a slideshow of its figures

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# November 1, 2024 - fun!


# configure
HEADERS   = { 'accept':'text/xml' }
HOST      = 'http://carrels.distantreader.org'
FIGURES   = 'figures'
SLIDESHOW = './slideshow-template-slideshow.txt'
SIDE      = './slideshow-template-slide.txt'
HTML      = './slideshow.html'

# require
from lxml       import etree as parser
from requests   import get
from subprocess import call
import os        
from sys        import argv, exit

# get input
if len( argv ) != 2 : exit( "Usage: " + argv[ 0 ] + " <carrel>" )
carrel = argv[ 1 ]

# request the carrel's xml representation
response = get( HOST + '/' + carrel, headers=HEADERS )

# sanity check
if not response.ok : exit( 'Error (' + str( response.status_code ) + ')' + ' - ' + response.reason )

# manifest the... manifest
manifest = parser.fromstring( response.text )

# get and process each file in the figures directory of the manifest; create a list of urls
urls  = []
files = manifest.xpath( "//directory[@name='" + FIGURES + "']/file" )
for file in files: urls.append( '/'.join( [ HOST, carrel, FIGURES, file.xpath( './@name' )[ 0 ] ] ) )
urls = sorted( urls )

# process each url; create a set of slides
slides = ''
count  = str( len( urls ) )
with open( SIDE ) as handle : template = handle.read()
for index, url in enumerate( urls ) : 

	# parse, replace, and update
	caption = url.split( '/' )[ -1 ]
	slide   = template.replace( '##INDEX##', str( index + 1 ) )
	slide   = slide.replace( '##COUNT##', count )
	slide   = slide.replace( '##URL##', url )
	slide   = slide.replace( '##CAPTION##', caption )
	slides  = slides + slide

# open, build, and save the html
with open( SLIDESHOW ) as handle : html = handle.read().replace( '##SLIDES##', slides )
with open( HTML, 'w' ) as handle : handle.write( html )

# open the html
try : os.startfile( HTML )
except AttributeError :

    try    : call( [ 'open', HTML ] )
    except : exit( 'Could not open URL' )

# done
exit()
