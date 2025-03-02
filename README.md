Project Overview

This project analyzes a provided log file to extract structured tables, converts the data into an Excel file with proper formatting, and documents the entire process. The extracted data is then uploaded to a public GitHub repository for submission.

Steps Followed

Step 1: Log File Analysis

Identified START and END markers to define structured tables.

Step 2: Writing Prompts for ChatGPT

Created structured prompts to extract data efficiently from START to END blocks.

Refined prompts to handle missing or extra columns dynamically.

Example prompt:

Extract all rows between "ALARM STATUS START" and "ALARM STATUS END".
Convert them into a structured JSON format with columns: Date_Time, Severity, Object, Problem.
Ignore any unnecessary headers and descriptions.

Step 3: Extracting Data & Converting to Excel

Developed a Python script to extract data from the log file.

