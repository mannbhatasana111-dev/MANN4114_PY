import zipfile
import os

def zip_files(zip_name, files_to_zip):
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in files_to_zip:
                if os.path.exists(file):
                    zipf.write(file)
                    print(f"Added {file}")
        print(f"{zip_name} created.")
    except Exception as e:
        print(f"Error: {e}")

def unzip_file(zip_name, extract_to):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall(extract_to)
            print(f"Extracted to {extract_to}")
    except Exception as e:
        print(f"Error: {e}")

my_files = ["calc.py", "students.txt"]
zip_files("my_archive.zip", my_files)
unzip_file("my_archive.zip", "extracted_data")