#!/bin/bash
# script to display response size for URL passed to script
curl -s $1 -w %{size_download}"\n"
