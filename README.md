# gmtools
GameMaker tools

# gmKtool.py

This tool convert wav audio data to ogg and recompress ogg audio in the data and audiogroup files.

## requirements

This tool uses `oggenc` and `oggdec` (available with the vorbis-tools package on ubuntu) to convert wav to ogg and ogg to wav. You need to have `oggenc` and `oggdec` installed on the system you are running `gmKtool.py`.

You also need Python 3.

## usage

```
./gmKtool.py -h
usage: gmKtool.py [-h] [-v] [-m MINSIZE] [-a [AUDIOGROUP]] [-N [NO_WRITE]] [-O [ONLY_WRITE]] [-b BITRATE] [-D] [-R RESAMPLE] [-B] [-r] [-y] [-d DESTDIRPATH] infilepath

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
  -N [NO_WRITE], --no-write [NO_WRITE]
                        Don't write the updated file for this audiogroup number (option can repeat). By default none.
  -O [ONLY_WRITE], --only-write [ONLY_WRITE]
                        Only write the updated file for this audiogroup number (option can repeat). By default write all.
  -b BITRATE, --bitrate BITRATE
                        nominal bitrate (in kbps) to encode at (oggenc -b option). 0 for auto (default)
  -D, --downmix         Downmix stereo to mono (oggenc --downmix option)
  -R RESAMPLE, --resample RESAMPLE
                        Resample input data to sampling rate n (Hz) (oggenc --resample option). Supported values: 8000, 11025, 22050, 32000, 44100, 48000
  -B, --buffered        Don't flush stdout after each line (incompatible with the patcher screen)
  -r, --recompress      Allow ogg recompression
  -y, --yes             Overwrite the files if already present without asking (DANGEROUS, use with caution)
  -d DESTDIRPATH, --destdirpath DESTDIRPATH
                        Destination directory path (default ./Ktool.out)
```

## example

`./gmKtool.py -d ./repacked -a 0 -a 1 -m 524288 data.win` will compress all wav audio > 512 KB in audiogroup 0 (`data.win`) and 1 (`audiogroup1.dat`) with auto bitrate. The updated files will be written in `./repacked`.

`./gmKtool.py data.win` will compress all wav audio > 1MB (default) in all audiogroups with auto bitrate. The updated files will be written in `./Ktool.out`

`./gmKtool.py -vv -r -m 0 -b 64 data.win` will compress all wav audio, recompress all ogg audio, in all audiogroups with 64kbps bitrate. The updated files will be written in `./Ktool.out`. The verbose level will be 2.

`./gmKtool.py -vv -O 0 -O 1 -m 0 -b 64 data.win` will do the same as in the previous example but it will only write the updated `data.win` (SOND entries, and if present AUDO entries from audiogroup 0), all linked `audiogroupN.dat` won't be written. This might be useful when debugging, testing as you don't want to perform the ogg compression for each test run. Note that `-O` and `-N` can not be used together.

`./gmKtool.py -vv -D -R 22050 -m 0 -r -b 32 data.win` will downmix to mono and resample to 22kHz all audio (including ogg, no minimum file size limit) and will use a 32 kbps bitrate.

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