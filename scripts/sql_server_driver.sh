#!/bin/bash

# Enable debugging and exit on error
set -ex

# Set environment variables
export ACCEPT_EULA=Y
export DEBIAN_FRONTEND=noninteractive

# Determine Debian version
if command -v lsb_release > /dev/null; then
    OS_NAME=$(lsb_release -is)
    DEBIAN_VERSION=$(lsb_release -rs)
    DEBIAN_CODENAME=$(lsb_release -cs)
    OS_INFO=$(lsb_release -a)
else
    source /etc/os-release
    OS_NAME=$ID
    DEBIAN_VERSION=$VERSION_ID
    DEBIAN_CODENAME=$VERSION_CODENAME
    OS_INFO=$(cat /etc/os-release)
fi

# Check if the OS is Debian
if [ "$OS_NAME" != "debian" ]; then
    echo "This script is only supported on Debian."
    exit 1
fi

echo "Operating System Information:"
echo "$OS_INFO"
echo "Detected Debian version: $DEBIAN_VERSION ($DEBIAN_CODENAME)"

# Add Microsoft GPG key
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg

# Generate the repository URL based on Debian version
case $DEBIAN_VERSION in
    "9"*)
        REPO_URL="https://packages.microsoft.com/config/debian/9/prod.list"
        ;;
    "10"*)
        REPO_URL="https://packages.microsoft.com/config/debian/10/prod.list"
        ;;
    "11"*)
        REPO_URL="https://packages.microsoft.com/config/debian/11/prod.list"
        ;;
    "12"*)
        REPO_URL="https://packages.microsoft.com/config/debian/12/prod.list"
        ;;
    *)
        echo "Unsupported Debian version: $DEBIAN_VERSION"
        exit 1
        ;;
esac

# Add the Microsoft package repository
curl -fsSL $REPO_URL | tee /etc/apt/sources.list.d/mssql-release.list

# Update package lists
apt-get update

# Install the ODBC Driver
apt-get install -y msodbcsql18

# Optional: Install tools for bcp and sqlcmd
apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

# Optional: Install unixODBC development headers
apt-get install -y unixodbc-dev

# Optional: Install Kerberos library for slim distributions
apt-get install -y libgssapi-krb5-2

# Source .bashrc (only needed for interactive sessions)
# source ~/.bashrc