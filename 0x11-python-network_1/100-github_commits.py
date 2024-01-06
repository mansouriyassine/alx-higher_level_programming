#!/usr/bin/python3
"""
This script lists 10 commits (from the most recent to oldest)
of a repository by a user using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    api_url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    response = requests.get(api_url)

    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to fetch commits. Status code: {response.status_code}")
