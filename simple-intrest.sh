#!/bin/bash
# Simple Interest Calculator
# Calculates Simple Interest and Total Amount based on
# Principal, Rate of Interest, and Time.
#
# Formula:
#   Simple Interest (SI) = (P * R * T) / 100
#   Total Amount (A)     = P + SI

echo "=== Simple Interest Calculator ==="

read -p "Enter Principal amount: " principal
read -p "Enter Rate of Interest (%): " rate
read -p "Enter Time (in years): " time

# Calculate simple interest using bc for floating point math
interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
total=$(echo "scale=2; $principal + $interest" | bc)

echo ""
echo "--- Results ---"
echo "Principal Amount : $principal"
echo "Rate of Interest : $rate%"
echo "Time             : $time years"
echo "Simple Interest  : $interest"
echo "Total Amount     : $total"
