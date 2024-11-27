#!/bin/bash

set -ex

echo "Update package list and install dependencies"
apt-get update
apt-get install -y wget gnupg2 tar

echo "Download and install Maven 3.6.3"
wget -q -O /tmp/apache-maven-3.6.3-bin.tar.gz https://archive.apache.org/dist/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
tar -xzvf /tmp/apache-maven-3.6.3-bin.tar.gz -C /usr/share
mv /usr/share/apache-maven-3.6.3 /usr/share/maven
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

echo "Set environment variables for Maven"
echo "export MAVEN_HOME=/usr/share/maven" >> /etc/profile.d/maven.sh
echo "export MAVEN_CONFIG=/root/.m2" >> /etc/profile.d/maven.sh
source /etc/profile.d/maven.sh

# Clean up
rm -rf /tmp/apache-maven-3.6.3-bin.tar.gz /var/lib/apt/lists/*

echo "Download and install OpenJDK 11 from AdoptOpenJDK"
wget -q -O /tmp/OpenJDK11U-jdk_x64_linux_hotspot_11.0.11_9.tar.gz https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.11+9/OpenJDK11U-jdk_x64_linux_hotspot_11.0.11_9.tar.gz
mkdir -p /usr/lib/jvm
tar -xzf /tmp/OpenJDK11U-jdk_x64_linux_hotspot_11.0.11_9.tar.gz -C /usr/lib/jvm
mv /usr/lib/jvm/jdk-11.0.11+9 /usr/lib/jvm/java-11-openjdk-amd64

echo "Set environment variables for JAVA_HOME"
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" >> /etc/profile.d/java.sh
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> /etc/profile.d/java.sh
source /etc/profile.d/java.sh

# Clean up
rm -rf /var/lib/apt/lists/* /tmp/OpenJDK11U-jdk_x64_linux_hotspot_11.0.11_9.tar.gz
java -version
echo "Copleted Installation of openJDK"