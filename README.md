# xyz-to-neb.py

Linearly interpolates n number of structures from 2 .xyz files for use in CP2K.

To use this script, make sure to pip install argparse and pandas.

The script generally works as follows (command):

```
python -i xyz-to-neb.py -in <INPUT_STRUCTURE_FILE_NAME> -fin <FINAL_STRUCTURE_FILE_NAME> -rep <NUMBER_OF_INTERPOLATED_REPLICAS>
```
