# Description
Pull all of the repositories that were forked from a common repository and place them in a tree in local storage.

Default location is: `~/workspace/forks/`

Each fork of the common repository will be in its own folder: `~/workspace/forks/<project>/<user>/<project>`

# Operation
The python script generates a bash script that can be reviewed and then pipped into bash for execution.

# Example
```
> uv run ./git-pull-forks.py -r live-bootcamp-project -o letsgetrusty > examples/live-bootcamp-project.sh
> head -4 examples/live-bootcamp-project.sh
# ------------------------------
(mkdir -p '/Users/hughbrown/workspace/forks/live-bootcamp-project/aldass' && cd '/Users/hughbrown/workspace/forks/live-bootcamp-project/aldass' && git clone https://github.com/aldass/live-bootcamp-project.git)
# ------------------------------
(mkdir -p '/Users/hughbrown/workspace/forks/live-bootcamp-project/paragoner1' && cd '/Users/hughbrown/workspace/forks/live-bootcamp-project/paragoner1' && git clone https://github.com/paragoner1/live-bootcamp-project.git)
> bash examples/live-bootcamp-project.sh
```
