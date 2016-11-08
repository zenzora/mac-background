# background.py
# Author Brian.Christner@gmail.com
# www.brianchristner.io
#
# Adapted for ubuntu 16.04 by Jake Berkowsky
# www.zenzora.com

# Unsplash Application ID
api_key = 'Insert Unsplash Application ID key here'

############################################################################
import subprocess
import urllib
import urllib2
import json
#########################################################################

# build the usplash URL

# Grab random picture from unsplash
url = 'https://api.unsplash.com/photos/random?client_id=' + api_key

# Change the Background script
cmd = """/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///tmp/bg.jpg"""

# Iterrate through the URL and json

try:
        f = urllib2.urlopen(url)
        json_string = f.read()
        f.close()
        parsed_json = json.loads(json_string)
        photo = parsed_json['urls']['full']
        urllib.urlretrieve(photo, "/tmp/bg.jpg") # Location where we download the image to.
        subprocess.Popen(cmd, shell=True)
except KeyboardInterrupt:
        print "The Computer says NO!"
