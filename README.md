# gmtools
GameMaker tools

# gmKtool.py

This tool convert wav audio data to ogg in the data and audiogroup files.

## requirements

This tool uses `oggenc` (available with the vorbis-tools package on ubuntu) to convert wav to ogg. You need to have `oggenc` installed on the system you are running `gmKtool.py`.

You also need Python 3.

## usage

```
./gmKtool.sh -h
usage: gmKtool.sh [-h] [-v] [-m MINSIZE] [-a [AUDIOGROUP]] [-b BITRATE] [-y] [-d DESTDIRPATH] infilepath

GameMaker K-dog tool: compress wav to ogg in Gamemaker data files

positional arguments:
  infilepath            Input file path (eg: data.win)

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose level (cumulative option)
  -m MINSIZE, --minsize MINSIZE
                        Minimum WAV size in bytes to target (default 1MB)
  -a [AUDIOGROUP], --audiogroup [AUDIOGROUP]
                        Audiogroup ID to process (option can repeat). By default any.
  -b BITRATE, --bitrate BITRATE
                        nominal bitrate (in kbps) to encode at (oggenc -b option). Default 128 kbps
  -y, --yes             Overwrite the files if already present without asking (DANGEROUS, use with caution)
  -d DESTDIRPATH, --destdirpath DESTDIRPATH
                        Destination directory path (default ./Ktool.out)
```

## example

`./gm-Ktool.py data.win -d ./repacked -a 0 -a 1 -m 524288` will compress all wav data > 512 KB in audiogroup 0 (`data.win`) and 1 (`audiogroup1.dat`). The updated files will be written in `./repacked`.

# readiffdata.py

This tool gives you details on data and audiogroup files. It also can extract audio data. It is not designed for usage in the production fields, more for troubleshooting.

## requirements

You need Python 3.

## usage

```
./readiffdata.py -h
usage: readiffdata.py [-h] [-e [EXTRACT]] [-m] filepath

Process IFF data file

positional arguments:
  filepath              Input file path

options:
  -h, --help            show this help message and exit
  -e [EXTRACT], --extract [EXTRACT]
                        Extract chunk (eg. AUDO)
  -m, --moreinfo        Get more info on chunks
  ```

  # example

  `./readiffdata.py -mm -e AUDO data.win` will gives details (level 2) on `data.win` and extract data from *AUDO* chunk into the `audo` folder.

# readsond.py

This tool gives extract audio metadata from a data file. It's in a draft state atm, you need to edit the offset and the filename in the script to get it working.

## requirements

You need Python 3.

## usage

```
./readsond.py
```