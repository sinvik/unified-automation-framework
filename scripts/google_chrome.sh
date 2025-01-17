#!/bin/bash

set -e

# Install necessary packages
apt-get update && apt-get install -y wget unzip

# Install Google Chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
apt-get update && apt-get install -y google-chrome-stable
