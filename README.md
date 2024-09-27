# gmtools
GameMaker tools

# gmKtool.py

This tool convert wav audio data to ogg and recompress ogg audio in the data and audiogroup files.

## requirements

This tool uses `oggenc` and `oggdec` (available with the vorbis-tools package on ubuntu) to convert wav to ogg. You need to have `oggenc` and `oggdec` installed on the system you are running `gmKtool.py`.

You also need Python 3.

## usage

```
./gmKtool.sh -h
usage: gmKtool.py [-h] [-v] [-m MINSIZE] [-a [AUDIOGROUP]] [-b BITRATE] [-r] [-y] [-d DESTDIRPATH] infilepath

GameMaker K-dog tool: compress wav to ogg, recompress ogg, in Gamemaker data files

positional arguments:
  infilepath            Input file path (eg: data.win)

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose level (cumulative option)
  -m MINSIZE, --minsize MINSIZE
                        Minimum WAV/OGG size in bytes to target (default 1MB)
  -a [AUDIOGROUP], --audiogroup [AUDIOGROUP]
                        Audiogroup ID to process (option can repeat). By default any.
  -b BITRATE, --bitrate BITRATE
                        nominal bitrate (in kbps) to encode at (oggenc -b option). 0 for auto (default)
  -r, --recompress      Allow ogg recompression
  -y, --yes             Overwrite the files if already present without asking (DANGEROUS, use with caution)
  -d DESTDIRPATH, --destdirpath DESTDIRPATH
                        Destination directory path (default ./Ktool.out)
```

## example

`./gmKtool.py -d ./repacked -a 0 -a 1 -m 524288 data.win` will compress all wav audio > 512 KB in audiogroup 0 (`data.win`) and 1 (`audiogroup1.dat`) with auto bitrate. The updated files will be written in `./repacked`.

`./gmKtool.py data.win` will compress all wav audio > 1MB (default) in all audiogroups with auto bitrate. The updated files will be written in `./Ktool.out`

`./gmKtool.py -vv -r -m 0 -b 64 data.win` will compress all wav audio, recompress all ogg audio, in all audiogroups with 64kbps bitrate. The updated files will be written in `./Ktool.out`

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
                        Extract chunk (eg. AUDO, SOND)
  -m, --moreinfo        Get more info on chunks
  ```

  # example

  `./readiffdata.py -mm -e AUDO data.win` will gives details (level 2) on `data.win` and extract data from *AUDO* chunk into the `audo` folder.