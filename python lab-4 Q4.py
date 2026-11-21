# JSON Log File Analyzer

import json

logs = [
    {"message": "Application started", "level": "INFO"},
    {"message": "User logged in", "level": "INFO"},
    {"message": "File not found", "level": "ERROR"},
    {"message": "Application closed", "level": "INFO"}
]

with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

with open("logs.json", "r") as file:
    data = json.load(file)

info = 0
error = 0

for log in data:
    print(log["message"], "-", log["level"])

    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "ERROR":
        error += 1

print("\nTotal INFO:", info)
print("Total ERROR:", error)
