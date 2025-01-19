import os

def sequential_rename(folder_path):
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    for filename in files:
        old_path = os.path.join(folder_path, filename)
        temp_path = os.path.join(folder_path, f"temp_{filename}")
        os.rename(old_path, temp_path)
    
    temp_files = sorted([f for f in os.listdir(folder_path) if f.startswith("temp_")])

    for index, filename in enumerate(temp_files, start=1):
        _, file_extension = os.path.splitext(filename)
        new_name = f"{index}{file_extension}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")

folder_path = r"E:\Programiranje\Projects\Fire Detection\data\images" 
sequential_rename(folder_path)
