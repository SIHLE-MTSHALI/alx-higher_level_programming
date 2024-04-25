#!/bin/bash
# Script to display only the HTTP status code of a response
curl -s -o /dev/null -w "%{http_code}" "$1"
