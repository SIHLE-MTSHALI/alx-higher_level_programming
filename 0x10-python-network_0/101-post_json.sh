#!/bin/bash
# Script to send a POST request with a JSON file in the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
