# Pull the latest changes from the main branch
echo "Pulling the latest changes from 'main'..."
git checkout main
if git pull origin main; then
  echo "Successfully updated 'main'."
else
  echo "Error: Failed to pull changes. Please check your git setup."
  exit 1
fi
