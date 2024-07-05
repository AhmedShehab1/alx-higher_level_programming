#!/bin/bash
# Size in Bytes Of the response
curl -s -o /dev/null -w "%{size_download}\n" $1
