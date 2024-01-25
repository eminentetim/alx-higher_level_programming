#!/bin/bash
# Bashscript that shows all HTTP methods that the serverallows
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
