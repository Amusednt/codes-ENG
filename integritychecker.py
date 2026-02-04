import hashlib

def calculate_file_hash(file_path):
    """
    Generates a SHA-256 hash for a specific file.
    Useful for verifying file integrity after downloads or transfers.
    :param file_path: Path to the target file.
    """
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Read the file in 4KB chunks to efficiently handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        result = sha256_hash.hexdigest()
        print(f"File: {file_path}")
        print(f"SHA-256 Hash: {result}")
        return result
        
    except FileNotFoundError:
        print("❌ Error: The specified file was not found.")
        return None

# Example usage:
# calculate_file_hash("important_document.pdf")
