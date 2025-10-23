import os
import shutil

TYPES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif", ".bmp"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"]
}

def main():
    folder = input("Enter folder path to organize (default: current): ").strip() or os.getcwd()
    print(f"Organizing files in: {folder}")
    count = organize_folder(folder)
    print(f"Done! {count} files moved.")

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, exts in TYPES.items():
        if ext in exts:
            return category
    return "Others"

def move_file(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    filename = os.path.basename(src)
    target = os.path.join(dest_dir, filename)
    i = 1
    while os.path.exists(target):
        name, ext = os.path.splitext(filename)
        target = os.path.join(dest_dir, f"{name}_{i}{ext}")
        i += 1
    shutil.move(src, target)

def organize_folder(folder):
    count = 0
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            category = get_category(filename)
            target_dir = os.path.join(folder, category)
            move_file(path, target_dir)
            print(f"Moved '{filename}' to '{category}'")
            count += 1
    return count

if __name__ == "__main__":
    main()
