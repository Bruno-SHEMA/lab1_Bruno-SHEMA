#!/bin/bash


# Create archive directory if missing

if [ ! -d "archive" ]; then
    mkdir archive
fi


# Generate timestamp

timestamp=$(date +"%Y%m%d-%H%M%S")


original="grades.csv"
if [ ! -f "$original" ]; then
    touch grades.csv
fi

new_name="grades_${timestamp}.csv"


# Check if grades.csv exists

if [ -f "$original" ]; then


    # Move and rename file

    mv "$original" "archive/$new_name"

    # Logging

    echo "Timestamp: $timestamp | Original: $original | Archived: $new_name" >> organizer.log

    # creating a new eempty grades.csv
    touch grades.csv

fi
