import base64

# Open the image file in binary mode
with open('your_image.jpg', 'rb') as image_file:
    # Read the binary data of the image
    binary_data = image_file.read()

# Encode the binary data into Base64
base64_encoded = base64.b64encode(binary_data)

# Convert the result to a string (if needed)
base64_encoded_str = base64_encoded.decode('utf-8')

# Now, base64_encoded_str contains the Base64-encoded image data
