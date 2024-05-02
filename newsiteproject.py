# Import the module that allows changes to the os
import os
# Import the module to allow arguments
import sys

# Check is the folder name was passed as a command-line arguments
if len(sys.argv) < 2:
    print("Usage: python newsiteproject.py <folder_name>")
    sys.exit(1) # exit the script if no argument is given


# Specify the directory where the new folder must be created
parent_directory = "/home/shelldon/Site_Projects"

# Name the new folder
folder_name = sys.argv[1] # the second argument is the folder name

# Full path of the new folder
folder_path = os.path.join(parent_directory, folder_name)

# Check that the directory already exists to avoid overwriting
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Directory '{folder_path}' created.")
    
# Create the img subfolder
img_folder_path = os.path.join(folder_path, "img")
if not os.path.exists(img_folder_path):
    os.makedirs(img_folder_path)
    print(f"Subdirectory 'img' created in {folder_path}")
    
# Set the permissions for the directory
try:
    os.chmod(folder_path, 0o770)  # Full access for user and group, none for others
    os.chmod(img_folder_path, 0o770) # full access for user and group, none for others
except PermissionError:
    print("Failed to set directory permissions, run script with appropriate privileges.")
    
# Paths for the files to be created
html_file_path = os.path.join(folder_path, "index.html")
css_file_path = os.path.join(folder_path, "style.css")



# HTML content
html_content = """

    <!DOCTYPE html>
    <html lang="en-za" />
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        
        <title> </title>
        
        <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css" />
        <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    
    <body>
    
    </body>
    </html>

"""

# CSS Content
css_content = """

    * {box-sizing: border-box;}

"""



# Create and write to index.html
with open(html_file_path, 'w') as file:
    file.write(html_content)
    
# Create and write to style.css_content
with open(css_file_path, 'w') as file:
    file.write(css_content)
    
    
# Print success message
print(f"Directory and files created at {folder_path}")







