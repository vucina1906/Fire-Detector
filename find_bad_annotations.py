import os

folder_path = r"E:\Programiranje\Projects\Fire Detection\labels2\train"

def find_invalid_labels(folder_path):
    print("🔍 Script started...")

    if not os.path.isdir(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print(f"📂 Folder found: {folder_path}\n")
    invalid_files = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            print(f"🔎 Checking file: {filename}")

            try:
                if os.path.getsize(file_path) == 0:
                    print(f"⚠️ Empty file detected: {filename}")
                    invalid_files.append(filename)
                    continue  

                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for i, line in enumerate(lines):
                        line = line.strip()  
                        if not line:
                            continue 
                        
                        parts = line.split()
                        if not parts:
                            continue  
                        
                        if not parts[0].isdigit() or int(parts[0]) not in [0, 1]:
                            print(f"⚠️ Invalid label '{parts[0]}' found in {filename} at line {i + 1}: {line}")
                            invalid_files.append(filename)
                            break  

            except Exception as e:
                print(f"❗ Error reading {filename}: {e}")
                invalid_files.append(filename)

    if invalid_files:
        print("\n🚨 Files with invalid or empty labels:")
        for file in invalid_files:
            print(f"❗ {file}")
    else:
        print("✅ All label files are correct.")

find_invalid_labels(folder_path)
