import os

try:
    modified_files = []
    folders = os.listdir('.')
    for folder in folders:
      if not (os.path.isdir(folder)):
        continue

      files = os.listdir(folder)
      actual_path = os.path.join(os.getcwd(), folder)
      filtered_files = [file for file in files if "DISABLED" in file]

      for file in filtered_files:
        if (os.path.splitext(file)[1] != ".ini"):
            continue

        new_name = file.replace("DISABLED", "")
        old_file_path = os.path.join(actual_path, file)
        new_file_path = os.path.join(actual_path, new_name)

        os.rename(old_file_path, new_file_path)
        modified_files.append(f"{old_file_path} -> {new_file_path}")

    with open("modified_files.txt", "w") as txt_file:
      txt_file.write("\n".join(modified_files))

except FileNotFoundError:
    print("Specified path not found. Please check if the path is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
