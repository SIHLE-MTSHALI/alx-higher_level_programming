#!/usr/bin/python3

import requests
import sys

def fetch_latest_commits(repo_name, owner_name):
    """
    Retrieves the last 10 commits from a specified GitHub repository and displays 
    them in the format `<sha>: <author name>`.

    Parameters:
    - repo_name (str): The name of the GitHub repository.
    - owner_name (str): The owner of the GitHub repository.
    """
    # Define the target URL for retrieving commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Send a GET request to fetch the commits
    response = requests.get(url)

    # Get the JSON content from the response
    json_response = response.json()

    # Display the last 10 commits with their SHA and author names
    for commit in json_response[:10]:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    # Read the repository name and owner name from the command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Fetch and display the last 10 commits from the specified repository
    fetch_latest_commits(repo_name, owner_name)
