# counter.py: Counts "error" and "warning" in a log file and saves results
import os

filename = input("Enter filename (e.g., log.txt): ")  # Prompt for file
print(f"Current directory: {os.getcwd()}")  # Debug: Show directory
print(f"Looking for file: {filename}")  # Debug: Confirm filename

try:
    with open(filename, 'r') as file:  # Open file in read mode
        content = file.read()  # Read content
        error_count = content.lower().count("error")  # Count "error"
        warning_count = content.lower().count("warning")  # Count "warning"
        print(f"Error count: {error_count}")  # Debug: Show error count
        print(f"Warning count: {warning_count}")  # Debug: Show warning count
    with open("error_count.txt", 'w') as output:  # Open file in write mode
        output.write(f"Found {error_count} errors and {warning_count} warnings.")  # Write both counts
    print("Result saved to error_count.txt")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found! Ensure it's in the same folder.")
except Exception as e:
    print(f"Error: {e}")