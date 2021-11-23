# -*- coding: utf-8 -*-

import openslide
import tarfile
# from openslide import Image, ImageSlide, open_slide
import os

zipfile = "./test.tar.gz"

if __name__ == "__main__":
	print("hello world!")

	with tarfile.open(zipfile, 'r:gz') as t:
		t.extractall(path='./')
	filename = "./Tumor.ndpi"
	img = openslide.OpenSlide(filename)

	img = img.read_region((5000, 5000), 0, (1000, 1000))
	jpg = img.convert("RGB")
	jpg.save(filename.replace("ndpi", "jpg"))
