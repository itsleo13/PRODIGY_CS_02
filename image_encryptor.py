from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    data = np.array(image)
    encrypted_data = (data + 50) % 256
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print("Image encrypted and saved to", output_path)

def decrypt_image(image_path, output_path):
    image = Image.open(image_path)
    data = np.array(image)
    decrypted_data = (data - 50) % 256
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print("Image decrypted and saved to", output_path)

# Example:
# encrypt_image("input.png", "encrypted.png")
# decrypt_image("encrypted.png", "decrypted.png")