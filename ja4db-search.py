#!/usr/bin/python3
import json
import sys

# Check if both arguments were provided
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <ja4_db.json> <ja4_fingerprint>")
    sys.exit(1)

json_file = sys.argv[1]
ja4_fingerprint_input = sys.argv[2]

# Load JSON data from file
try:
    with open(json_file, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{json_file}' not found.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: File '{json_file}' is not valid JSON.")
    sys.exit(1)

def find_user_agent(ja4_fingerprint: str):
    for entry in data:
        if entry.get("ja4_fingerprint") == ja4_fingerprint:
            print("Ja4 Fingeprint:", entry.get("ja4_fingerprint"))
            print("  Application:", entry.get("application"))
            print("  User-Agent:", entry.get("user_agent_string"))
            return
    print("No matching ja4_fingerprint found.")

# Call the function with the command-line argument
find_user_agent(ja4_fingerprint_input)
