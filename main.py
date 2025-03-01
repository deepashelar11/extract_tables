import pandas as pd
import re

# Read the log file
log_file_path = "log_file.txt"
with open(log_file_path, "r") as file:
    log_data = file.read()


# Function to extract data between markers
def extract_data(start_marker, end_marker, log_data):
    pattern = rf"{start_marker}\n(.*?){end_marker}"
    match = re.search(pattern, log_data, re.DOTALL)
    if match:
        extracted = match.group(1).strip()
        if extracted:
            return extracted
    return None  # Explicitly return None if no data is found


# Function to process structured tables
def process_table(data):
    if not data:
        return pd.DataFrame()  # Return empty DataFrame if no data

    lines = data.split("\n")
    table_data = [line.split(";") for line in lines if ";" in line]

    if len(table_data) < 2:  # Ensure at least a header + 1 row
        return pd.DataFrame()  # Return empty DataFrame if structure is invalid

    headers = table_data[0]  # First row as headers
    rows = table_data[1:]  # Remaining rows

    # Handle inconsistent row lengths
    max_cols = max(len(row) for row in rows)

    # Adjust headers dynamically if row count exceeds headers
    if len(headers) < max_cols:
        headers += [f"Column_{i}" for i in range(len(headers) + 1, max_cols + 1)]
    elif len(headers) > max_cols:
        headers = headers[:max_cols]  # Trim headers if needed

    # Pad missing values in rows
    cleaned_rows = [row + [""] * (max_cols - len(row)) for row in rows]

    return pd.DataFrame(cleaned_rows, columns=headers)


# Extract tables
tables = {
    "ALARM STATUS": extract_data("ALARM STATUS START", "ALARM STATUS END", log_data),
    "AVG PRB BRANCH RSSI": extract_data("AVG PRB BRANCH RSSI START", "AVG PRB BRANCH RSSI END", log_data),
    "AVG PER BRANCH RSSI": extract_data("AVG PER BRANCH RSSI START", "AVG PER BRANCH RSSI END", log_data),
    "RFBRANCH STATUS": extract_data("RFBRANCH STATUS START", "RFBRANCH STATUS END", log_data),
    "BASIC DETAIL": extract_data("BASIC DETAIL START", "BASIC DETAIL END", log_data),
    "HARDWARE INVENTORY": extract_data("HARDWARE INVENTORY START", "HARDWARE INVENTORY END", log_data),
}

# Create an Excel file
excel_path = "extracted_data.xlsx"
with pd.ExcelWriter(excel_path) as writer:
    sheet_added = False  # Ensure at least one valid sheet exists

    for name, data in tables.items():
        if data:  # Ensure extraction wasn't empty
            print(f"Processing {name}...")
            df = process_table(data)
            if not df.empty:
                df.to_excel(writer, sheet_name=name, index=False)
                sheet_added = True
            else:
                print(f"Warning: {name} is empty and will not be added.")

    if not sheet_added:
        raise IndexError("No valid sheets available, at least one sheet must be visible.")

print(f"Data extracted and saved to {excel_path}")
