#!/bin/bash

echo "Test Scenarios"
echo "---------------------------"

echo "h1 -> h2 should work"
echo "Expected: 0% packet loss"

echo "h3 -> h2 should fail"
echo "Expected: 100% packet loss"

echo "h1 -> h4 ICMP should fail"
echo "Expected: 100% packet loss"

echo "---------------------------"
echo "Run these commands inside Mininet CLI:"
echo "h1 ping -c 4 h2"
echo "h3 ping -c 4 h2"
echo "h1 ping -c 4 h4"
