#!/bin/bash
# Script to check if the website is reachable
URL="https://google.com" # Потім заміниш на свій S3-сайт
STATUS=$(curl -o /dev/null -s -w "%{http_code}" $URL)

if [ $STATUS -eq 200 ]; then
  echo "Success: Site is UP (Status $STATUS)"
else
  echo "Alert: Site is DOWN or unreachable (Status $STATUS)"
fi
