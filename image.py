import cv2
import numpy as np
import os


def encrypt_image(image_path, key):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error loading image. Ensure the image file is valid and accessible.")

    encrypted_image = image.copy()
    rows, cols, channels = image.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                encrypted_image[i, j, k] = image[i, j, k] ^ key  # XOR operation

    encrypted_path = "encrypted_image.png"
    cv2.imwrite(encrypted_path, encrypted_image)
    print(f"Encrypted image saved as {encrypted_path}")
    return encrypted_path


def decrypt_image(encrypted_path, key):
    if not os.path.exists(encrypted_path):
        raise FileNotFoundError(f"Encrypted image file '{encrypted_path}' not found.")

    encrypted_image = cv2.imread(encrypted_path)
    if encrypted_image is None:
        raise ValueError("Error loading encrypted image. Ensure the file is valid and accessible.")

    decrypted_image = encrypted_image.copy()
    rows, cols, channels = encrypted_image.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                decrypted_image[i, j, k] = encrypted_image[i, j, k] ^ key  # XOR decryption

    decrypted_path = "decrypted_image.png"
    cv2.imwrite(decrypted_path, decrypted_image)
    print(f"Decrypted image saved as {decrypted_path}")
    return decrypted_path


# Example usage:
key = 123  # Encryption key (should be same for encryption and decryption)
image_path = "butterfly.jpg"
if os.path.exists(image_path):
    encrypted_path = encrypt_image(image_path, key)
    decrypt_image(encrypted_path, key)
else:
    print(f"Error: Image file '{image_path}' does not exist.")