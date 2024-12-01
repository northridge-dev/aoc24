#!/bin/bash

# Function to display usage instructions
function usage() {
  echo "Usage: $0 <lastname> <challenge_number>"
  echo "Example: $0 kruckenberg 1"
  exit 1
}

# Check for the correct number of arguments
if [ "$#" -ne 2 ]; then
  usage
fi

# Extract username and task number from the arguments
LASTNAME=$1
CHALLENGE_NUMBER=$2

# Validate that the task number is numeric
if ! [[ $CHALLENGE_NUMBER =~ ^[0-9]+$ ]]; then
  echo "Error: Challenge number must be a numeric value."
  usage
fi

# Construct the branch name
BRANCH_NAME="${LASTNAME}/day-${CHALLENGE_NUMBER}"

# Pull the latest changes from the main branch
echo "Pulling the latest changes from 'main'..."
git checkout main
if git pull origin main; then
  echo "Successfully updated 'main'."
else
  echo "Error: Failed to pull changes. Please check your git setup."
  exit 1
fi

# Create a new branch
echo "Creating a new branch: ${BRANCH_NAME}..."
if git checkout -b "${BRANCH_NAME}"; then
  echo "Successfully created and switched to branch '${BRANCH_NAME}'."
else
  echo "Error: Failed to create the branch. Please check for any conflicts or issues."
  exit 1
fi

# Final message
echo "Branch '${BRANCH_NAME}' is ready. Start making your changes!"
