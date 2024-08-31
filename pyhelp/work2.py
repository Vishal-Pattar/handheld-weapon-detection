import os
import shutil
import re

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files_to_directories(source_dir):
    for filename in os.listdir(source_dir):
        # Only process files (not directories)
        if os.path.isfile(os.path.join(source_dir, filename)):
            # Extract the alphabetic prefix
            match = re.match(r"([a-zA-Z]+)", filename)
            if match:
                prefix = match.group(1)
                # Create the target directory
                target_dir = os.path.join(source_dir, prefix)
                create_directory(target_dir)
                # Move the file to the target directory
                shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
                print(f"Moved {filename} to {target_dir}")

# Set the source directory
source_directory = 'Dataset'

# Call the function
move_files_to_directories(source_directory)
