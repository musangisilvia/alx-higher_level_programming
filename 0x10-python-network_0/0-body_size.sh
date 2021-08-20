#!/bin/bash
# script to display resonse size
curl -s -w %{size_download} "$1";echo
