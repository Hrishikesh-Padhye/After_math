#version 0.0.1

import os
import platform
import zlib
import zipfile

if os.geteuid() != 0:
	exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

raw_path = "/root/Hrishikesh/My Github/After_math/"
path = "/var/log/"

file_names_deb = ["auth.log", "faillog", "syslog", "wtmp", "btmp"]
file_names_fedora = ["secure", "btmp", "wtmp", "cron" , "messages", "lastlog"]

if platform.dist()[0] == "fedora" :
	file_names = file_names_fedora
else :
	file_names = file_names_deb


def compress(file_names):
	# Select the compression mode ZIP_DEFLATED for compression
	# or zipfile.ZIP_STORED to just store the file
	compression = zipfile.ZIP_DEFLATED
	zip_file_name = "RAWs.zip"
	# create the zip file first parameter path/name, second mode
	zf = zipfile.ZipFile(zip_file_name, mode="w")
	try:
		for file_name in file_names:
		# Add file to the zip file
		# first parameter file to zip, second filename in zip
			zf.write(path + file_name, file_name, compress_type=compression)
	except OSError:
		pass
	finally:
		# Don't forget to close the file!
		zf.close()

compress(file_names)
