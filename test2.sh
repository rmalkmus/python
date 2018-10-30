#!/bin/bash

# The purpose of this script is to speed up the process of adding splunk to our servers new words for diff
#addin an new line for testing diff
host=`hostname`




word1
word2
word3

# Add splunk group and user
groupadd splunk
useradd -s /bin/sh -c "Splunk Server" -g splunk -d /opt/splunkforwarder splunk


# Change ownership of the splunkforwarder directory
chown -R splunk:splunk /opt/splunkforwarder


# Change hostname
sed -i "s/testname/$host/g" /opt/splunkforwarder/etc/system/local/server.conf
sed -i "s/testname/$host/g" /opt/splunkforwarder/etc/system/local/inputs.conf


# Create ini file
/opt/splunkforwarder/bin/splunk enable boot-start


# Start Splunk
/etc/init.d/splunk start

