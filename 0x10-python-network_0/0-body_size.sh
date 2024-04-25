#!/bin/bash
# Script to fetch the body size of a URL
curl -s "$1" | wc -c
