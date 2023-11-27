# Importing necessary libraries
import os
import shutil

# Get user input for the directory path
path = input("Enter path: ")

# List all files in the specified directory
files = os.listdir(path)

# Iterate through each file in the directory
for file in files:
    # Split the filename and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension

    # Check if a directory with the extension exists
    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        # Create the directory if it doesn't exist
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# Print a success message
print("Files organized successfully!")

