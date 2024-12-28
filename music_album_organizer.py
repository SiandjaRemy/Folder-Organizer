import os
import shutil


# Specify the folder to organize

folder_to_organize = input("Please enter the path of the folder to organize: ")

folder_to_organize = folder_to_organize

# Define the categories and their respective file extensions
# Feel free to modify this dictionary or add the extenstions you want
categories = {
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.mpg', '.3gp', '.webm', '.ogv', '.m4v'],
    'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.swift', '.go', '.json', '.xml', '.sql'],
    'Executables': ['.exe', '.app', '.dmg', '.msi', '.bat', '.sh', '.bin'],
    'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
    'CAD': ['.dwg', '.dxf'],
    '3D Models': ['.obj', '.stl', '.fbx', '.blend']
}


def organize_album():

    # Create folders for each category if they do not exist
    for category in categories.keys():
        category_path = os.path.join(folder_to_organize, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Move files to the appropriate folders
    for filename in os.listdir(folder_to_organize):
        file_extension = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(folder_to_organize, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(source_file):
            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(folder_to_organize, category)
                    shutil.move(source_file, destination_folder)
                    print(f'Moved: {filename} to {category}/')
                    moved = True
                    break
            
            if not moved:
                print(f'File not categorized: {filename}')

    print("Organization complete.")


# Call the function to execute the organization
organize_album()

print(folder_to_organize)
