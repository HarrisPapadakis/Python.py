import os
import shutil

# Define categories and corresponding file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []  # Anything that doesn't match the above
}

def organize_files(folder_path):
    """Organizes files in the given folder into categorized subfolders."""
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return
    
    # Create subfolders if they don't exist
    for category in CATEGORIES.keys():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)
    
    # Move files to corresponding subfolders
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine file category
        file_extension = os.path.splitext(file_name)[1].lower()
        category_found = False
        for category, extensions in CATEGORIES.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(folder_path, category, file_name))
                category_found = True
                break
        
        # If file doesn't match any category, move to 'Others'
        if not category_found:
            shutil.move(file_path, os.path.join(folder_path, "Others", file_name))
    
    print("Files organized successfully!")

# Example usage
if __name__ == "__main__":
    folder_to_organize = input("Enter the path of the folder to organize: ")
    organize_files(folder_to_organize)