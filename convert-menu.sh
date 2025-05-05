#!/bin/sh
convert -density 600 $1 -scale 1920 -background White -alpha remove -alpha off menu.png
