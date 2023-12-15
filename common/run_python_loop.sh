#!/bin/bash

# The path to the Python script
PYTHON_SCRIPT="../2023/days/day12.py"

# Get the last modification time
LAST_MODIFICATION=`stat -c %Y $PYTHON_SCRIPT`

while true; do
    # Check if the file was modified
    NEW_MODIFICATION=`stat -c %Y $PYTHON_SCRIPT`
    if [ "$LAST_MODIFICATION" != "$NEW_MODIFICATION" ]; then
        # Update the modification time
        LAST_MODIFICATION=$NEW_MODIFICATION
        
        # Run the Python script
        clear
        python $PYTHON_SCRIPT
    fi
    sleep 2
done
