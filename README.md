Project Overview

This project analyzes a provided log file to extract structured tables, converts the data into an Excel file with proper formatting, and documents the entire process. The extracted data is then uploaded to a public GitHub repository for submission.

Steps Followed

Step 1: Log File Analysis

Identified START and END markers to define structured tables.

Determined the number of tables and their column structures.

Tables found in the log file:

ALARM STATUS

AVG PRB BRANCH RSSI

AVG PER BRANCH RSSI

RFBRANCH STATUS

BASIC DETAIL

HARDWARE INVENTORY

Column Titles Identified:

ALARM STATUS: Date_Time, Severity, Object, Problem

AVG PRB BRANCH RSSI: Cell, SECTOR_Branch_X, PRBGroup1-10, PRBGroup11-20, ..., PRBGrp90-

AVG PER BRANCH RSSI: CELL, SC, FRU, BOARD, PUSCH, PUCCH, A, B, C, D, DELTA

RFBRANCH STATUS: MO, auPortRef, rfPortRef, Attenuation, TrafficDelay, reservedBy, tmaRef

BASIC DETAIL: Proxy, Adm State, Op. State, MO

HARDWARE INVENTORY: FDD, RRU, FRU, SE, AG, NIOT

Step 2: Writing Prompts for ChatGPT

Created structured prompts to extract data efficiently from START to END blocks.

Refined prompts to handle missing or extra columns dynamically.

Example prompt:

Extract all rows between "ALARM STATUS START" and "ALARM STATUS END".
Convert them into a structured JSON format with columns: Date_Time, Severity, Object, Problem.
Ignore any unnecessary headers and descriptions.

Step 3: Extracting Data & Converting to Excel

Developed a Python script to extract data from the log file.

Handled dynamic column mismatches to prevent errors.

Stored extracted tables in an Excel file with separate sheets for each table.

Step 4: Documenting the Extraction Process

README.md includes:

How START/END blocks were identified.

Number of tables found and their structure.

Code logic for extraction and formatting.

Explanation of prompt refinement for better accuracy.

Step 5: GitHub Upload & Submission

Created a public GitHub repository with the following structure:

📁 integer-coding-test
│── 📄 log_file.txt           # Provided log file
│── 📄 extracted_data.xlsx    # Extracted tables in Excel
│── 📄 README.md              # Documentation (process, patterns, tables)
│── 📄 main.py                # Python script for extraction

Submitted the GitHub link for evaluation.

Evaluation Criteria & Compliance

✅ Pattern Identification – Successfully identified six tables.
✅ Prompt Quality – Created precise ChatGPT prompts for extraction.
✅ Data Extraction Accuracy – Ensured structured tables with correct headers.
✅ Excel Organization – Stored tables in separate Excel sheets.
✅ Documentation Clarity – README explains the process step-by-step.
✅ GitHub Usage – Code and files uploaded for easy access.
