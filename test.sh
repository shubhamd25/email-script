#!/bin/bash

# Set the path to your Python script
python_script="/home/ganesh-py/htdocs/success.mycashflowhub.com/sender.py"

# Set the loop count
loop_count=10

# Loop to run the Python script
for ((i=1; i<=$loop_count; i++))
do
    echo "Running iteration $i"
    python3 "$python_script"
    sleep 1  # Adjust the sleep duration if needed
done
