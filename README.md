# Ubuntu Background Changer

This is a fork of the [Mac OSX Background Changer](https://github.com/vegasbrianc/mac-background) made to work for ubuntu. It downloads random images from unsplash.

## How do I use it?

Before you can use this amazing script you will need to [Register with Unsplash](https://unsplash.com/developers) and then [create an application](https://unsplash.com/oauth/applications). Once you've created an application copy the application ID and insert it into the pyton script under the Application ID section.  

Make a directory and clone this project into this folder. To run the script:


    python background.py

Once you get the hang of the script you can easily add this to your crontab to run once or several times a day.

## What's it doing?

The script is calling the Unsplash API for a random picture and copies the picture to /tmp. 

