from PIL import Image

def strip_exif_data(image_path, output_path):
    """
    Removes EXIF metadata from an image by creating a clean copy.
    :param image_path: Original image with metadata.
    :param output_path: Clean image destination.
    """
    try:
        img = Image.open(image_path)
        
        # Create a new data object without the metadata (info)
        data = list(img.getdata())
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)
        
        # Save the clean version
        clean_img.save(output_path)
        print(f"🛡️ Privacy Check: EXIF data removed. Saved as: {output_path}")
        
    except Exception as e:
        print(f"❌ Error processing image: {e}")

# Example usage:
# strip_exif_data("vacation_photo.jpg", "safe_photo.jpg")
