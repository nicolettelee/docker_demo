#!/usr/bin/env python

import os

def clear_dir(dirpath, keep_flag):

    """
    Clear all files in a directory.
    If keep_flag is True, keep the final files (sorted bam and index).

    :param dirpath: Path to directory of interest.
    """

    all_files = os.listdir(dirpath)

    if not keep_flag:
        for file in all_files:
            full_path = f'{dirpath}/{file}'
            os.remove(full_path)

        assert len(os.listdir(dirpath)) == 0, "Problem with clean-up: \
                                          not all files removed."
    else:
        for file in all_files:
            full_path = f'{dirpath}/{file}'
            if not "sorted" in full_path:
                os.remove(full_path)

        assert len(os.listdir(dirpath)) == 2, "Problem with clean-up: \
                                                final number of files different from desired."