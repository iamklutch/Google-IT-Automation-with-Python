#!/usr/bin/env python3

from PIL import Image
from os.path import join
import os
import sys

path = "./images/"
new_path = "./updated"
dir = os.listdir(path)
new_size = (128,128)

for infile in sys.argv[1:]:
  outfile = os.path.splitext(infile)[0] + ".JPEG"
  try:
    with Image.open(infile) as im:
      #print(infile, im.format, f"{im.size}x{im.mode}")
      im.rotate(90).resize(new_size).save(outfile, "JPEG")
  except Exception as e:
    print("Error: ", e)
    

'''
for file in dir:
  try:
    with Image.open(file) as im:
      im.rotate(90).resize((128,128)).save(dir,  "JPEG")
      print(file)
  except Exception as e:
    print("Error: ", e)
'''
    

