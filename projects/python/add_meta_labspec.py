'''
This script is for getting the directory contains .txt exported from labspec and add the meta data to the file.
The meta data is extracted from the filename.
Be sure to name the file following this format "%target_$gating_ %laser_%exposition_%accumulation_%date_%time.txt"
'''

import os
from utils.data import add_meta_to_text
from glob import glob 
import sys

def _main(directory:str):
    path_list:list[str] = glob(os.path.join(directory,'*'))
    count = 0
    error = 0
    for path in path_list:
        try:
            add_meta_to_text(path=path) 
            count = count + 1
        except AssertionError as e:
            print(f"error={e}")
            error = error + 1
    print(f"Total add meta={count}")
    print(f"Total    error={error}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, required=False)
    args = parser.parse_args()

    directory:str = args.dir if args.dir is not None else input("The directory you want to fill in the meta data: ")
    _main(directory=directory)