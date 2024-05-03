#!/usr/bin/env python3

from PIL import Image
from os.path import join
import os
import sys

path = "./images/"
new_path = "./opt/icons/"
new_size = (128,128)
rotation = 90

if not os.path.exists(new_path):
  #create the directory
  os.makedirs(new_path)
# iterate through all the files at the given directory
for infile in sys.argv[1:]:
  #get the path of the destination and only take the filename, not the path
  filename = infile[7:]
  outfile = new_path + filename #+ os.path.splitext(infile)[1]
  #print(outfile)
  try:
    with Image.open(infile) as im:
      im.rotate(rotation).resize(new_size).save(outfile, "JPEG")
  except Exception as e:
    print("Error: ", e)
    
    

