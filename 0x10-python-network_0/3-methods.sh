#!/bin/bash
# Delete Request
curl -sI "S1" | grep Allow: | cut -d ":" -f2 | sed 's/ //'
