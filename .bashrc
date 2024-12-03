export PYTHONPATH=/workspaces/aoc24

# One-time setup
alias set-lastname='bash /workspaces/aoc24/scripts/set_LASTNAME.sh'

# Recurring
alias create-branch='bash /workspaces/aoc24/scripts/create_branch.sh'
alias delete-branch='bash /workspaces/aoc24/scripts/delete_branch.sh'
alias get-updates='bash /workspaces/aoc24/scripts/get_updates.sh'
alias go-to-main='bash /workspaces/aoc24/scripts/go_to_main.sh'
# alias create-pr='bash /workspaces/aoc24/scripts/create_pr.sh'

# Simplify running a Python script
py() {
    # Ensure the LASTNAME environment variable is set
    if [ -z "${LASTNAME+x}" ]; then
        echo "Error: run set-lastname first."
        return 1
    fi

    # Ensure an argument is provided
    if [ -z "$1" ]; then
        echo "Usage: py <script_name>"
        return 1
    fi

    local script_path="/workspaces/aoc24/src/$LASTNAME/$1.py"
 
    # Check if the script exists
    if [ ! -f "$script_path" ]; then
        echo "Error: Script not found at $script_path"
        return 1
    fi

    python3 "$script_path"
}