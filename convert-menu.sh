#!/bin/sh
convert -density 600 "$1" -scale 3140 -background White -alpha remove -alpha off menu.png
