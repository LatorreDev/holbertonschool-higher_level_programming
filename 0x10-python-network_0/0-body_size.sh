#!/bin/bash
# body size with curl
curl -sI $1 | grep Content-Length | cut -d " " -f2
