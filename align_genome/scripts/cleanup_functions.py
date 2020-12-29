#!/usr/bin/env python

import os

def clear_dir(dirpath):

    """
    Clear all files in a directory.

    :param dirpath: Path to directory of interest.
    """

    all_files = os.listdir(dirpath)

    for file in all_files:
        full_path = f'{dirpath}/{file}'
        os.remove(full_path)

    assert len(os.listdir(dirpath)) == 0, "Problem with clean-up: \
                                          not all files removed."