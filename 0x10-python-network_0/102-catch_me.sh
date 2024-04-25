#!/bin/bash
# Script to send a specific request that causes a custom response
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me
