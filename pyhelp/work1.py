import os

def list_files_in_directory(directory, output_file):
    # Get a list of all files in the given directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Write the list of files to the output file
    with open(output_file, 'w') as file:
        for f in files:
            file.write(f + '\n')

# Example usage
directory = './Weapon-Detection-Dataset/'  # Replace with the path to your directory
output_file = 'output.txt'  # Replace with the desired output file name
list_files_in_directory(directory, output_file)
