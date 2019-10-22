#!/bin/bash

cd /root/torfleet &&
echo "Starting Tor..." &&
service tor start &&
service polipo start &&
echo "Starting Torfleet..." &&
bash runfleet.sh &&
echo "Torfleet initialized. Wait ~1 minute before it starts running"