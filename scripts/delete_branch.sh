#!/bin/bash

# Function to display usage instructions
function usage() {
  echo "Usage: $0 <challenge_number>"
  echo "Example: $0 1"
  exit 1
}

# Check for the correct number of arguments
if [ "$#" -ne 1 ]; then
  usage
fi

# Extract username and task number from the arguments
STUDENT_DIRNAME=$LASTNAME
CHALLENGE_NUMBER=$1

# Validate that the task number is numeric
if ! [[ $CHALLENGE_NUMBER =~ ^[0-9]+$ ]]; then
  echo "Error: Challenge number must be a numeric value."
  usage
fi

# Construct the branch name
BRANCH_NAME="${STUDENT_DIRNAME}/day-${CHALLENGE_NUMBER}"

# Move to main
git checkout main
if git checkout main; then
  echo "Now on main"
else
  echo "Error: Failed to checkout main."
  exit 1
fi

# Delete branch
echo "Deleting branch: ${BRANCH_NAME}..."
if git branch -D "${BRANCH_NAME}"; then
  echo "Successfully deleted branch '${BRANCH_NAME}'."
else
  echo "Error: Failed to delete the branch. Please check for any conflicts or issues."
  exit 1
fi
