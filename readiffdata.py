#!/usr/bin/env python3

import argparse
import os
from struct import unpack, pack
from pathlib import Path


CHUNK_W_ENTRIES = [ b'AUDO', \
                    b'TXTR', \
                    b'EXTN', \
                    b'SOND', \
                    b'SPRT', \
                    b'BGND', \
                    b'PATH', \
                    b'SCPT', \
                    b'SHDR', \
                    b'FONT', \
                    b'TMLN', \
                    b'OBJT', \
                    b'ROOM', \
                    b'TPAG', \
                    b'CODE', \
                    b'VARI', \
                    b'FUNC', \
                    b'STRG'
                  ]

AUDO_DIR=Path("./audo")

def pretty_size(size):

   units = ['B ','KB','MB','GB']
   
   n = size

   while n > 1024:
      n = n / 1024
      units = units[1:]
   
   return f"{int(n):#4} {units[0]}"

def read_chunk(fin,args):
    global CHUNK_W_ENTRIES

    chunk_offset = fin.tell()
    chunk_token = fin.read(4)
    chunk_size = unpack('<I',fin.read(4))[0]
    
    print(f"{chunk_token.decode('ascii')} size: {pretty_size(chunk_size)} ({chunk_size:#10x}) offset: {chunk_offset:#10x}")

    if args.extract and chunk_token.decode('ascii') in args.extract:
        read_chunk_entries(fin,chunk_token,chunk_size,args, True)

    elif chunk_token in CHUNK_W_ENTRIES and args.moreinfo > 0:
        read_chunk_entries(fin,chunk_token,chunk_size,args, False)

    elif chunk_token != b'FORM':
        # Go to the end of the chunk
        # We don't want to do this for FORM as we will
        # reach the end of the file without parsing
        # the embedded chunks
        fin.seek(chunk_size,1)

def read_chunk_entries(fin,token,size,args, extract):
    chunk_nbentries = unpack('<I',fin.read(4))[0]
    print(f"`-entries: {chunk_nbentries:#7} ({chunk_nbentries:#10x})")

    if args.moreinfo < 2 and not extract:
        fin.seek(size-4,1)

    elif token == b'AUDO':
        read_audo_entries(fin,size,chunk_nbentries,args, extract)

    else:
        fin.seek(size-4,1)
        return

def read_audo_entries(fin,size,nbentries,args , extract):
    global AUDO_DIR
    entry_table_offset = fin.tell()

    for n in range(nbentries):
        fin.seek(entry_table_offset + 4 * n)
        entry_offset = unpack('<I',fin.read(4))[0]
        fin.seek(entry_offset)
        entry_size = unpack('<I',fin.read(4))[0]
        entry_head = fin.read(4)
        print(f"   {n:#6} -> {entry_head.decode('ascii')} size: {pretty_size(entry_size)} ({entry_size:#10x}) offset: {entry_offset:#10x}")

        if extract:
            with open(AUDO_DIR / f"{n}.{get_data_extension(entry_head)}", 'wb+') as audiofile:
                fin.seek(-4,1)
                audiofile.write(fin.read(entry_size))
    
    # go at the end of the audio chunk
    fin.seek(entry_table_offset + size - 4)

def get_data_extension(head):
    extension = "raw"

    if head == b'RIFF':
        # WAV
        extension = "wav"

    elif head == b'OggS':
        # OGG
        extension = "ogg"
   
    return extension


def main():

    parser = argparse.ArgumentParser(description='Process IFF data file')
    parser.add_argument('-e','--extract', nargs='?', action='append', help='Extract chunk (eg. AUDO)')
    parser.add_argument('-m','--moreinfo', action='count', default=0, help='Get more info on chunks')

    parser.add_argument('filepath', help='Input file path')

    args = parser.parse_args()

    with open(args.filepath,'rb') as inputfile:

      inputfile.seek(0, os.SEEK_END)
      filesize = inputfile.tell()
      inputfile.seek(0)

      print(f"Processing: {args.filepath}")
      print(f"File size: {pretty_size(filesize)}")

      while ( inputfile.tell() < filesize):
         read_chunk(inputfile, args)

if __name__ == '__main__':
    main()