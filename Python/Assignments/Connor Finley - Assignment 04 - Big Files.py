'''
Connor Finley
Advanced Python
Assignment 04 - Big Files
2017/09/28
'''

import os

MB = 2**20
SIZE = 100 * MB  # 100 MB

def bigfiles(basepth):
    """
    Search for files whose size exceeds 100 MB

    basepth: string of file path where to start searching (absolute or relative)

    return: list of files that exceed 100 MB in size
    """

    matches = []

    for root, dirs, files in os.walk(basepth):
        for f in files:
            absolute_path = os.path.join(os.path.abspath(root), f)
            if os.path.getsize(absolute_path) > SIZE:
                matches.append(absolute_path)

    return matches

p = input("Enter base path: ")
matched_files = bigfiles(p)
for f in matched_files:
    print(f)
