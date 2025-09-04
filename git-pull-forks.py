#!/usr/bin/env python3

# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "click",
#   "requests",
# ]
# ///

from pathlib import Path
from typing import Dict, Any

import click
import requests


@click.command()
@click.option("-r", "--repo", required=True, type=str)
@click.option("-o", "--owner", required=True, type=str)
def main(repo: str, owner: str):
    def get_filepath(base: Path, result: Dict[str, Any]) -> str:
        project, user = result['name'], result['owner']['login']
        p = base.joinpath(*[project, user])
        return str(p)

    # No token is required to access public repos
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    response = requests.get(url, headers=headers)
    if not response.ok:
        print(response)
        return

    base = Path("~/workspace/forks/").expanduser()
    for result in response.json():
        print(f"# {'-' * 30}")
        pp = get_filepath(base, result)
        git_url = result['git_url']
        clone_cmd = f"git clone {git_url}"
        print(f"(mkdir -p '{pp}' && cd '{pp}' && {clone_cmd})")


if __name__ == '__main__':
    main()
