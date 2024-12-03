#!/bin/bash

# Function to check for unstaged or uncommitted changes
check_for_changes() {
  # Check for unstaged changes
  if ! git diff --quiet; then
    echo "Unstaged changes detected. Please stage or discard them before switching branches."
    return 1
  fi

  # Check for uncommitted changes
  if ! git diff --cached --quiet; then
    echo "Uncommitted changes detected. Please commit or stash them before switching branches."
    return 1
  fi

  echo "No unstaged or uncommitted changes detected."
  return 0
}

# Example: Switch branches if no changes are detected
switch_branch() {
  local target_branch=$1

  # Ensure a branch name is provided
  if [ -z "$target_branch" ]; then
    echo "Usage: $0 <branch_name>"
    exit 1
  fi

  # Check for changes
  if check_for_changes; then
    echo "Switching to branch '$target_branch'..."
    git checkout "$target_branch"
  else
    echo "Aborting branch switch."
    exit 1
  fi
}

# Call the function with the desired branch as an argument
switch_branch "$1"
