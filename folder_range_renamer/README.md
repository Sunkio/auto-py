 run it from the command line with the required parameters:

```
python3 rename_folders.py AG00032 AG00034 _new
```

This example would rename folders AG00032, AG00033, and AG00034 by appending "_new" to their names if they exist in the same directory as the script.


you can run the script with the `-s` or `--source` flag to specify the source directory:

```
python3 rename_folders.py AG00032 AG00034 _new -s /path/to/source/directory
```

If the `-s` or `--source` flag is not used, the script will default to the current directory.