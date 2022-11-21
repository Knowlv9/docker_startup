# -*- coding: utf-8 -*-

import openslide
import tarfile
# from openslide import Image, ImageSlide, open_slide
import os

zipfile = "./test.tar.gz"

if __name__ == "__main__":
	print("hello world!")

	with tarfile.open(zipfile, 'r:gz') as t:
def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(t, path="./")
	filename = "./Tumor.ndpi"
	img = openslide.OpenSlide(filename)

	img = img.read_region((5000, 5000), 0, (1000, 1000))
	jpg = img.convert("RGB")
	jpg.save(filename.replace("ndpi", "jpg"))
