import os
import sys

def compare_inodes(dir1, dir2):
    inode_dict = {}
    for root, dirs, files in os.walk(dir1):
        for f in files:
            inode = os.stat(os.path.join(root, f)).st_ino
            inode_dict[inode] = os.path.join(root, f)
    
    for root, dirs, files in os.walk(dir2):
        for f in files:
            inode = os.stat(os.path.join(root, f)).st_ino
            if inode in inode_dict:
                print(f"Hard link found: {inode_dict[inode]} <--> {os.path.join(root, f)}")

