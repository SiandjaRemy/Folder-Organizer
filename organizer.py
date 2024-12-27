import os
import shutil


# Specify the folder to organize

# folder_to_organize = "C:/Users/ksrdrel/Desktop/DISTRACTIONS/series/4"
# folder_to_organize = r"C:\Users\ksrdrel\Desktop\DISTRACTIONS\series\4"

# C:\Users\ksrdrel\Desktop\DISTRACTIONS\series\1

folder_to_organize = input("Please enter the path of the folder to organize: ")

folder_to_organize = folder_to_organize

# Define the categories and their respective file extensions
categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']
}


def organize_files():

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
organize_files()

print(folder_to_organize)
