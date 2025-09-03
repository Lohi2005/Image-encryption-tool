from PIL import Image
import numpy as np
import json
import os

# Optional: For displaying images inline in Jupyter
try:
    from IPython.display import display
    IN_JUPYTER = True
except ImportError:
    IN_JUPYTER = False

KEY_FILE = "encryption_key.json"

def save_key(key):
    with open(KEY_FILE, "w") as f:
        json.dump(key.tolist(), f)
    print(f"Key saved to {KEY_FILE}")

def load_key():
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("No saved key found. You must encrypt first or provide a key.")
    with open(KEY_FILE, "r") as f:
        return np.array(json.load(f), dtype=np.uint8)

def display_image(image, title="Image"):
    print(f"Displaying: {title}")
    if IN_JUPYTER:
        display(image)
    else:
        image.show(title=title)

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    display_image(img, title="Original Image")

    img_array = np.array(img)
    key = np.resize(key, img_array.shape)

    encrypted_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save("encrypted_image.png")

    print("Image encrypted successfully as encrypted_image.png")
    display_image(encrypted_img, title="Encrypted Image")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    display_image(encrypted_img, title="Encrypted Image (Before Decryption)")

    encrypted_array = np.array(encrypted_img)
    key = np.resize(key, encrypted_array.shape)

    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save("decrypted_image.png")

    print("Image decrypted successfully as decrypted_image.png")
    display_image(decrypted_img, title="Decrypted Image")

def main():
    print("Image Encryption and Decryption with Key Saving")
    choice = input("Choose mode (E for encrypt, D for decrypt): ").strip().lower()

    if choice == "e":
        image_path = input("Enter the path to the image file: ").strip().strip('"')
        img = Image.open(image_path)
        img_array = np.array(img)
        key = np.random.randint(0, 256, size=img_array.shape, dtype=np.uint8)
        save_key(key)
        encrypt_image(image_path, key)

    elif choice == "d":
        key = load_key()
        decrypt_image("encrypted_image.png", key)

    else:
        print("Invalid choice! Please enter 'E' for encrypt or 'D' for decrypt.")

if _name_ == "_main_":
    main()
