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

# Get the current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD)

if [ "$current_branch" == "main" ]; then
  if check_for_changes; then
    if /workspaces/aoc24/scripts/get_updates.sh; then
      echo "Successfully pulled latest changes."
      exit 0
    else
        echo "Error: You have made changes on main branch! Ask for help."
        exit 1
    fi
  fi
fi

if check_for_changes; then
  git checkout main
  echo "Pulling latest changes into 'main'..."
  if /workspaces/aoc24/scripts/get_updates.sh; then
    echo "Successfully pulled latest changes."
    exit 0
  else
    echo "Error: Failed to pull changes."
    exit 1
  fi
fi



# Default boilerplate commit message
COMMIT_MESSAGE="quick save when switching to main"

# Function to display usage instructions
function usage() {
  echo "Usage: $0 [commit-message]"
  echo "Example: $0 'Added initial draft for feature X'"
  exit 1
}

# Check if a custom message is provided
if [ "$#" -gt 0 ]; then
  COMMIT_MESSAGE="$*"
fi

# Stage all changes
echo "Staging all changes..."
git add -A

# Commit changes
echo "Committing changes with message: \"$COMMIT_MESSAGE\""
if git commit -m "$COMMIT_MESSAGE"; then
  echo "Changes committed successfully."
else
  echo "No changes to commit or an error occurred."
  exit 1
fi

# Checkout the main branch
echo "Switching to the 'main' branch..."
if git checkout main; then
  echo "Switched to 'main'."
else
  echo "Error: Could not switch to 'main'. Please check your branch setup."
  exit 1
fi

# Call the pull-main script
echo "Pulling latest changes into 'main'..."
if /workspaces/aoc24/scripts/get_updates.sh; then
  echo "Successfully pulled latest changes."
else
  echo "Error: Failed to pull changes. Please check the pull-main script."
  exit 1
fi