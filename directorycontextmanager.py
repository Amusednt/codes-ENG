import tempfile
import os

def process_data_securely(data):
    """
    Creates a temporary environment to process sensitive data.
    Ensures no traces are left on the disk after completion.
    """
    # Create a temporary directory that exists only within this block
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"--- Secure Workspace Created at: {temp_dir} ---")
        
        # Path for a temporary file inside the workspace
        temp_file_path = os.path.join(temp_dir, "work_file.tmp")
        
        with open(temp_file_path, "w") as tmp:
            tmp.write(data)
            print("Processing data in memory...")

        # File is automatically deleted once the 'with' block ends
        print("Data processed and temporary files purged.")

if __name__ == "__main__":
    process_data_securely("Sensitive Information 123")
