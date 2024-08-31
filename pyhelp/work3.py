import os
import shutil

def move_files_to_parent_directory(parent_dir):
    for root, dirs, files in os.walk(parent_dir, topdown=False):
        # Move all files in subdirectories to the parent directory
        for name in files:
            file_path = os.path.join(root, name)
            shutil.move(file_path, parent_dir)
            print(f"Moved {file_path} to {parent_dir}")
        # Remove the empty subdirectories
        for name in dirs:
            dir_path = os.path.join(root, name)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)
                print(f"Removed directory {dir_path}")

# Set the parent directory
parent_directory = 'Dataset'

# Call the function
move_files_to_parent_directory(parent_directory)
