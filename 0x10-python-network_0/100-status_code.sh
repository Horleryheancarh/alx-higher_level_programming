#!/bin/bash
# Script that sends request to url
curl -so /dev/null -w "%{http_code}" "$1"
