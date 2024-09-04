#!/usr/bin/env python3

from struct import unpack
import os
from binascii import hexlify
import json

def read_str(fin,offset):
	if offset == 0x0:
		return ""
	cur_offset=fin.tell()
	fin.seek(offset-4)
	text=fin.read(unpack('<I',fin.read(4))[0]).decode('utf-8')
	fin.seek(cur_offset)
	return text

with open('gamedata/data.win','rb') as datafile:
		
	datafile.seek(0xad0) #SOND offset

	token = datafile.read(4)
	size = unpack('<I',datafile.read(4))
	
	nb_entries = unpack('<I',datafile.read(4))[0]

	offset_table = []
	for i in range(nb_entries):
		offset_table.append(unpack('<I',datafile.read(4))[0])

	sounds = {}

	for i,offset in enumerate(offset_table):
		datafile.seek(offset)

		name = read_str(datafile,unpack('<I',datafile.read(4))[0])
		flags = unpack('<I',datafile.read(4))[0]
		type = read_str(datafile,unpack('<I',datafile.read(4))[0])
		file = read_str(datafile,unpack('<I',datafile.read(4))[0])
		[ effect, volume, pitch, audiogroup, audiofile ] = \
			unpack('<IffII', datafile.read(20))
		
		sounds[f"{i:#04}"] = {
							"name" : name,
							"flags" : f"{flags:#4x}",
							"type" : type,
							"file" : file,
							"effect" : effect,
							"volume" : volume,
							"pitch" : pitch,
							"audiogroup" : audiogroup,
							"audiofile" : audiofile
						}
	


	print(json.dumps(sounds, indent=4))

	#print(hexlify(datafile.read(16)))
