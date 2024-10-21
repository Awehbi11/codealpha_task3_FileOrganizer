
import os
import shutil

def organize_files(directory):

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Music': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar', '.tar']
    }


    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)

   
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
     
        if os.path.isfile(file_path):
            moved = False
            for folder_name, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder_name, filename))
                    moved = True
                    break

            if not moved:
                print(f"No category found for: {filename}")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
    print("Files organized successfully.")
