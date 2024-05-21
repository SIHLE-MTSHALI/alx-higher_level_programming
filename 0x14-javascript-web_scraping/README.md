# JavaScript - Web Scraping

## Overview
This project demonstrates various web scraping techniques using JavaScript. It involves reading and writing files, making HTTP requests, and processing JSON data.

## Files

- `0-readme.js`: Reads and prints the content of a file.
- `1-writeme.js`: Writes a string to a file.
- `2-statuscode.js`: Displays the status code of a GET request.
- `3-starwars_title.js`: Prints the title of a Star Wars movie by episode number.
- `4-starwars_count.js`: Prints the number of movies where the character "Wedge Antilles" is present.
- `5-request_store.js`: Gets the contents of a webpage and stores it in a file.
- `6-completed_tasks.js`: Computes the number of tasks completed by user ID.
- `100-starwars_characters.js`: Prints all characters of a Star Wars movie.
- `101-starwars_characters.js`: Prints all characters of a Star Wars movie in the order of the list "characters" in the /films/ response.

## Requirements
- Node.js (version 14.x)
- semistandard
- request module

## Installation
```sh
# Install Node 14
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semistandard
sudo npm install semistandard --global

# Install request module
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
