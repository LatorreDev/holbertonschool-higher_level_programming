#!/bin/bash
# Delete Request
curl -i -X "OPTIONS" "S1" | grep Allow | cut -d " " -f 2-8
