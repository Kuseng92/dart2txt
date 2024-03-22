import os

def convert_dart_files_in_folder(source_folder, destination_folder):
    """
    Convert all .dart files found in a source folder to .txt files and save them to the destination folder.
    
    Parameters:
    - source_folder: The path to the folder containing the .dart files.
    - destination_folder: The path to the folder where the .txt files will be stored.
    """
    # Ensure the destination folder exists, if not, create it.
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Loop through all files in the source folder
    for file in os.listdir(source_folder):
        if file.endswith(".dart"):
            # Construct full file path
            dart_file_path = os.path.join(source_folder, file)
            # Construct new file name with .txt extension and full path
            new_file_name = os.path.splitext(file)[0] + '.txt'
            new_file_path = os.path.join(destination_folder, new_file_name)
            
            # Read the .dart file content
            with open(dart_file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
            
            # Write the contents to the new .txt file
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(contents)
            print(f"Converted {dart_file_path} to {new_file_path}")

# Example usage
source_folder = '/path/to/your/source/folder'  # Update this with the path to your .dart files
destination_folder = '/path/to/your/destination/folder'  # Update this with your desired destination
convert_dart_files_in_folder(source_folder, destination_folder)
