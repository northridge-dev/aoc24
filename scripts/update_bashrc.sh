#!/bin/bash

# Function to append to .bashrc and source it
update_bashrc() {
  local key="$1"
  local value="$2"
  local rc_file="$HOME/.bashrc"

  # Check if the key already exists in .bashrc
  if grep -q "^export $key=" "$rc_file"; then
    echo "Updating existing entry for $key in $rc_file"
    sed -i "s/^export $key=.*/export $key=\"$value\"/" "$rc_file"
  else
    echo "Adding new entry for $key to $rc_file"
    echo "export $key=\"$value\"" >> "$rc_file"
  fi
}

# Check if script has two arguments
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <VARIABLE_NAME> <VALUE>"
  exit 1
fi

# Call the function with user inputs
update_bashrc "$1" "$2"
