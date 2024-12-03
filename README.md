# Advent of Code 2024 - Northridge Prep

Advent of Code [web page](https://adventofcode.com/2024). You'll need to sign in with your GitHub credentials.

## One-time setup

1. Run `set-lastname` + your last name (needs to match your directory, e.g. `kruckenberg`)

## Troubleshooting

If you get errors about missing commands, try running `source /workspaces/aoc24/.bashrc`

## Typical Workflow

1. Run `go-to-main`. This will switch you to the `main` branch (committing any uncommitted changes on your current branch) and pull any updates into your Codespace.
2. Run `create-branch` + the number of the day's challenge. You'll see that you're on a new branch and a few empty files have been created:
  - two `.py` files in your directory with the challenge number
  - a `.txt` file in your `input` folder
3. Go to the Advent of Code challenge for the day. Get the input and copy it into the just-created `.txt` file.
4. Read the challenge and try writing code to solve it. Use `utils` -- that's what they're there for.
5. To run your code, type `py` + the name of the file you want to run (minus the `.py` extension). For example, if you have a script called `01a.py`, you'd type `py 01a`.
6. When you have a solution, try submitting it. If it wasn't correct, keep trying.
7. When you're finished with both parts, create a PR. (More instructions coming soon.)