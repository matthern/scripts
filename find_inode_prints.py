import os
import sys

def compare_inodes(dir1, dir2):
    dir1 = os.path.abspath(dir1.encode(sys.getfilesystemencoding()).decode('utf-8'))
    dir2 = os.path.abspath(dir2.encode(sys.getfilesystemencoding()).decode('utf-8'))

    if not os.path.exists(dir1):
        print(f"Error: Directory {dir1} does not exist")
        return

    inode_dict = {}
    for root, dirs, files in os.walk(dir1):
        if not files:
            print(f"Error: No files found in directory {dir1}")
            return
        for f in files:
            try:
                inode = os.stat(os.path.join(root, f)).st_ino
                inode_dict[inode] = os.path.join(root, f)
            except Exception as e:
                print(f"Error processing file {os.path.join(root, f)}: {e}")
    print(f"Inode dictionary: {inode_dict}")
    
    for root, dirs, files in os.walk(dir2):
        for f in files:
            inode = os.stat(os.path.join(root, f)).st_ino
            if inode in inode_dict:
                print(f"Hard link found: {inode_dict[inode]} <--> {os.path.join(root, f)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Error: Not enough arguments provided")
        print("Usage: python3 script.py /path/to/dir1 /path/to/dir2")
        sys.exit(1)
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    compare_inodes(dir1, dir2)

