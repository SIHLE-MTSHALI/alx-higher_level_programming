#!/bin/bash
# Script to send a specific request that causes a custom response
curl -s -X PUT -L -H "You-will-never-catch-me: true" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
