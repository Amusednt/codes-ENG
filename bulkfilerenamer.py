import os

def bulk_rename(folder_path, prefix="", suffix="", include_counter=True):
    """
    Renames all files within a specific folder using a custom pattern.
    :param folder_path: The directory containing the files.
    :param prefix: Text to add before the original filename.
    :param suffix: Text to add after the original filename.
    :param include_counter: If True, adds (1), (2), etc., to the name.
    """
    try:
        # List all items in the directory
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        for index, filename in enumerate(files, start=1):
            # Split filename and extension
            name, ext = os.path.splitext(filename)
            
            # Construct the new name
            counter_str = f"_{index}" if include_counter else ""
            new_name = f"{prefix}{name}{suffix}{counter_str}{ext}"
            
            # Perform the rename operation
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_name)
            )
            print(f"Renamed: {filename} -> {new_name}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# bulk_rename("./assets/icons", prefix="icon_")
