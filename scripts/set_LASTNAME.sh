#!/bin/bash

# Define the key
KEY="LASTNAME"

# Path to the original script
ORIGINAL_SCRIPT="/workspaces/aoc24/scripts/update_bashrc.sh"

# Check if the user provided a value
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <VALUE>"
  exit 1
fi

# Call the original script with the predefined key and user-provided value
source "$ORIGINAL_SCRIPT" "$KEY" "$1"

# Kill the current shell session
echo "Restarting shell session..."
exec $SHELL