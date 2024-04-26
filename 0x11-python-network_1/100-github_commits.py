#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of the repository "rails" by the user "rails"

Usage: ./100-github_commits.py <repository_name> <owner_name>
"""
import requests
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    # Get the repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the GitHub API URL
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repo_name)

    # Send a GET request to the GitHub API
    r = requests.get(url)

    # Parse the JSON response
    commits = r.json()

    try:
        # Iterate over the first 10 commits (or fewer if available)
        for i in range(10):
            # Get the SHA and author name of the commit
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')

            # Print the commit information in the required format
            print('{}: {}'.format(sha, author_name))
    except IndexError:
        # Handle the case when there are fewer than 10 commits
        pass
