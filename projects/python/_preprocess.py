'''
This script is for getting the directory contains .txt exported from labspec and add the meta data to the file.
The meta data is extracted from the filename.
Be sure to name the file following this format "%target_$gating_ %laser_%exposition_%accumulation_%date_%time.txt"

Then this will also perform the spectrum limit according to the given upper_bound and lower_bound
'''

import os
from utils.data import add_meta_to_text, limite_spectrum_range
from glob import glob 
import sys

def _main(directory:str, upper_bound:float, lower_bound:float):
    path_list:list[str] = glob(os.path.join(directory,'*'))
    count = 0
    error = 0
    path_error:list[str] = []
    for path in path_list:
        try:
            add_meta_to_text(path=path) 
            limite_spectrum_range(path=path, upper_bound=upper_bound, lower_bound=lower_bound)
            count = count + 1
        except AssertionError as e:
            print(f"error={e}")
            error = error + 1
            path_error.append(path)
    print(f"Total add meta={count}")
    print(f"Total    error={error}")
    print(f"Error={path_error}")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", type=str, required=False)
    parser.add_argument("--upper_bound", type=float, required=True)
    parser.add_argument("--lower_bound", type=float, required=True)
    args = parser.parse_args()

    directory:str = args.dir if args.dir is not None else input("The directory you want to fill in the meta data: ")
    upper_bound:float = float(args.upper_bound)
    lower_bound:float = float(args.lower_bound)
    _main(directory=directory, upper_bound=upper_bound, lower_bound=lower_bound)