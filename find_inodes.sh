#!/bin/bash

dir1="$1"
dir2="$2"

# Go to dir1 and get inode numbers and filenames
cd "$dir1"
inode_file1=$(ls -i | sort)
cd -

# Go to dir2 and get inode numbers and filenames
cd "$dir2"
inode_file2=$(ls -i | sort)
cd -

# Compare inode numbers and filenames
while read -r line1; do
  inode1=$(echo $line1 | awk '{print $1}')
  file1=$(echo $line1 | awk '{print $2}')
  while read -r line2; do
    inode2=$(echo $line2 | awk '{print $1}')
    file2=$(echo $line2 | awk '{print $2}')
    if [ "$inode1" == "$inode2" ]; then
      echo "Hardlinked files found: $file1 in $dir1 and $file2 in $dir2"
    fi
  done <<< "$inode_file2"
done <<< "$inode_file1"

