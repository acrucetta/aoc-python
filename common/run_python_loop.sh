#!/bin/bash
set -e

# The path to the Python script
cd /Users/andrescru/Library/CloudStorage/OneDrive-WaltzHealth/Documents/Github/aoc-python
PYTHON_SCRIPT="2023/day12.py"

# Get the last modification time
LAST_MODIFICATION=$(stat -f "%m" $PYTHON_SCRIPT)

while true; do
	# Check if the file was modified
	NEW_MODIFICATION=$(stat -f "%m" $PYTHON_SCRIPT)
	if [ "$LAST_MODIFICATION" != "$NEW_MODIFICATION" ]; then
		# Update the modification time
		LAST_MODIFICATION=$NEW_MODIFICATION

		# Run the Python script
		clear
		python3 $PYTHON_SCRIPT
	fi
	sleep 2
done

