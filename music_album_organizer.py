import os
import shutil
from tinytag import TinyTag
import re

# Specify the folder to organize

folder_to_organize = input("Please enter the path of the folder to organize: ")

folder_to_organize = folder_to_organize


# Define an array of the file extensions accepted
accepted_file_types = ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.wma', '.m4a']


def sanitize_filename(filename):
    """Removes or replaces invalid characters from a filename."""
    return re.sub(r'[\\/*?"<>|:]', '', filename)

def organize_album():

    # Check music author and create a folder if it does not yet exist
    # Move files to the appropriate folders
    for filename in os.listdir(folder_to_organize):
        file_extension = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(folder_to_organize, filename)
        

        # Check if it's a file (not a directory)
        if os.path.isfile(source_file):
            try:
                audio = TinyTag.get(source_file) 

                # print("Title:" + audio.title) 
                # print("Artist: " + audio.artist) 
                # print("Genre:" + audio.genre) 
                # print("Year Released: " + audio.year) 
                # print("Bitrate:" + str(audio.bitrate) + " kBits/s") 
                # print("Composer: " + str(audio.composer)) 
                # print("Filesize: " + str(audio.filesize) + " bytes") 
                # print("AlbumArtist: " + str(audio.albumartist)) 
                # print("Album: " + str(audio.album))
                # print("Duration: " + str(audio.duration) + " seconds") 
                # print("TrackTotal: " + str(audio.track_total)) 
                # print("#######################################################") 
                moved = False
                for extensions in accepted_file_types:
                    
                    if file_extension in extensions:
                        try:
                            # Check if a folder with the artist name already exist in the current directory.
                            # If it does not, create it.
                            artist_folder_path = os.path.join(folder_to_organize, audio.artist)
                            artist_folder_path_for_creation = os.path.join(folder_to_organize, sanitize_filename(audio.artist))
                            if not os.path.exists(artist_folder_path):
                                os.makedirs(artist_folder_path_for_creation)
                            main_destination_folder = os.path.join(folder_to_organize, audio.artist)
                            
                            sub_folder_name = f"{sanitize_filename(audio.album)} - {audio.year}"
                            sub_folder_name = sub_folder_name.replace("?", " ")
                            sub_destination_folder = os.path.join(main_destination_folder, sub_folder_name)
                            
                            # Check if a folder with the sub_folder_name already exist in the directory that carries the artist name.
                            # If it does not, create it.
                            if not os.path.exists(sub_destination_folder):
                                os.makedirs(sub_destination_folder)
                                
                            shutil.move(source_file, sub_destination_folder)
                            print(f'Moved: {filename} to {audio.artist}/{sub_folder_name}')
                            moved = True
                            break
                        except Exception as e:
                            print(f"Failed due to: {e}")
                            break
                
                if not moved:
                    print(f'File not categorized: {filename}')
                    
            except Exception as e:
                print(f"Failed to get audio tags: {e}")

    print("Organization complete.")


# Call the function to execute the organization
organize_album()

print(folder_to_organize)
