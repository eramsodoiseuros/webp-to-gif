import os
import sys
import imageio

# Print the name of the script
print('Converting:', sys.argv[1], 'to GIF')

# Open the WebP image using the imageio.imread() method
webp_image = imageio.imread(sys.argv[1])

# Extract the file name from the file path using os.path.basename()
file_name = os.path.basename(sys.argv[1])

# Get the file name without the extension using os.path.splitext()
file_name, _ = os.path.splitext(file_name)

# Save the image as a GIF using the imageio.imwrite() method
imageio.imwrite(file_name + ".gif", webp_image)
