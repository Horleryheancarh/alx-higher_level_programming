#!/bin/bash
# Script that sends a POST req and display response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
