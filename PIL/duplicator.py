import os
from PIL import Image
import sys

# Print the name of the script
print('Converting:', sys.argv[1], 'to GIF')

# Open the WebP image using the Image.open() method
webp_image = Image.open(sys.argv[1])

# Extract the file name from the file path using os.path.basename()
file_name = os.path.basename(sys.argv[1])

# Get the file name without the extension using os.path.splitext()
file_name, _ = os.path.splitext(file_name)

# Save the image as a GIF using the save() method
webp_image.save(file_name + ".gif")

