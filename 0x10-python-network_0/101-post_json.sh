#!/bin/bash
# Delete Request
curl -sd "@$2" -H "Content-Type: application/json" -X POST "$1"
