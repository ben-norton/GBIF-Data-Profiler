from PIL import Image
import os

# Source: https://blog.bytescrum.com/how-to-use-python-for-batch-image-resizing-and-compression

def resize_and_compress_images(input_dir, output_dir, max_width, max_height, quality):
    """
    Resize and compress images in the input directory and save them to the output directory.

    Parameters:
    - input_dir: Directory containing images to process.
    - output_dir: Directory to save processed images.
    - max_width: Maximum width for resizing.
    - max_height: Maximum height for resizing.
    - quality: Quality of the output image (1-100).
    """

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file path
        file_path = os.path.join(input_dir, filename)

        # Open the image file
        with Image.open(file_path) as img:
            # Resize the image
            img.thumbnail((max_width, max_height))

            # Save the compressed image to the output directory
            output_path = os.path.join(output_dir, filename)
            img.save(output_path, optimize=True, quality=quality)

            print(f"Processed {filename} -> {output_path}")

if __name__ == "__main__":
    input_directory = "images/input"   # Directory with original images
    output_directory = "images/output" # Directory for processed images
    max_width = 800                    # Max width for resizing
    max_height = 600                   # Max height for resizing
    quality = 85                       # Image quality (1-100)

    resize_and_compress_images(input_directory, output_directory, max_width, max_height, quality)
