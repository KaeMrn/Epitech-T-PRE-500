import os

# Start from the current directory
current_directory = os.getcwd()

# Recursively list all files and directories
for root, dirs, files in os.walk(current_directory):
    for name in dirs:
        print(f"Directory: {os.path.join(root, name)}")
    for name in files:
        print(f"File: {os.path.join(root, name)}")
