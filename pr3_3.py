import os


def list_files_in_directory():
    try:
        directory_path = "projects"
        entries = os.listdir("projects")
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
        return files
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

list_files_in_directory()