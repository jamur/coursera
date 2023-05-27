#!/usr/bin/env python3

import os
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
dir_path_result = "/opt/icons/"
arqs = [f for f in os.listdir(dir_path) if not f.startswith(".")]

for arq in arqs:
    Image.open(dir_path + arq).rotate(90).resize((128,128)).convert("RGB").save(dir_path_result + arq, format="JPEG")

# test
arqs = os.listdir(dir_path_result)
ok = True
for arq in arqs:
    img = Image.open(dir_path_result + arq)
    if img.format != "JPEG" or img.size != (128,128):
        ok = False
        print("Error!")

if ok:
    print("Success!")
