#!/usr/bin/python3

# Importing necessary packages
import requests
import sys

# Retrieve the repository name and owner name from command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Define the GitHub API URL for retrieving commits
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Send a GET request to retrieve the last 10 commits
response = requests.get(url)

# Parse the response as JSON
json_response = response.json()

# Display the last 10 commits in the specified format
for commit in json_response[:10]:
    sha = commit["sha"]  # Commit SHA
    author_name = commit["commit"]["author"]["name"]  # Commit author name
    print(f"{sha}: {author_name}")  # Display in '<sha>: <author name>' format
