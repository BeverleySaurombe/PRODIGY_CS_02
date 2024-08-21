from PIL import Image 
import random

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size
    
    # Initialize the random seed
    random.seed(key)
    
    # Perform encryption by modifying pixel values
    for i in range(len(pixels)):
        r, g, b = pixels[i]
        # Apply a simple mathematical operation (e.g., XOR with a random value)
        r = r ^ random.randint(0, 255)
        g = g ^ random.randint(0, 255)
        b = b ^ random.randint(0, 255)
        pixels[i] = (r, g, b)
    
    # Create a new image with the modified pixels
    encrypted_image = Image.new(image.mode, (width, height))
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Decryption is essentially the same as encryption for this method
    encrypt_image(image_path, output_path, key)
    print(f"Image decrypted and saved as {output_path}")

def main():
    # Get user input for the operation
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the path to save the output image: ")
    key = input("Enter the encryption key (integer): ")
    
    try:
        key = int(key)
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return
    
    if mode == "encrypt":
        encrypt_image(image_path, output_path, key)
    elif mode == "decrypt":
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()


