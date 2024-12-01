#!/bin/bash

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
