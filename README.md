# PRODIGY_CS_02
Pixel Manipulation for Image Encryption 

WHAT IS PIXEL MANIPILATION?
Pixel Manipulation is the ability to manipulate pixels. 

WHAT IS IMAGE ENCRYPTION?
Image Encryption efers to the process of hiding images from unauthorized access using a secret key.

WHAT IS MEANT BY PIXEL MANIPULATION FOR IMAGE ENCRYPTION.
By putting the two previous definitions together, we get a new definition of 'the ability to manipilate pixels to hide images from unauthorized access using a secret key'. That is the mening of pixel manipulation for image encryption.

WHY IMAGE ENCRYPTION?
It is done to safeguard the confidentiality and integrity of digital images. By encrypting images, sensitive information contained within them can be protected from unauthorized viewing, tampering, or interception.

HOW IT WORKS.
Image encryption techniques employ mathematical algorithms and cryptographic methods to alter the pixel values or the visual representation of an image. These algorithms convert the original image into a ciphered or scrambled version, making it useless to anyone without the  decryption key. The encryption process makes sure that even if an intruder gains access to the encrypted image, they cannot retrieve the original content. Not without the decryption key, that is. Image encryption works by transforming the pixel values of an image into an encrypted form, making it unintelligible to unauthorized individuals.

Here's a general overview of how image encryption works:
>Encryption (encrypt_image):The image is loaded using the Pillow library.
>Each pixel’s RGB values are modified using a basic XOR operation with a random number generated from a user-provided key.
>The modified pixels are saved into a new image file.
>Decryption (decrypt_image): Since the XOR operation is symmetric, the decryption process is the same as encryption. Using the same key, the pixel values are reverted to their original state.
>Main Function (main): Collects user input for the image path, output path, mode (encrypt/decrypt), and a key for encryption/decryption. Calls the appropriate function based on the user’s choice.


LIMITATIONS
>Pixels by themselves don't move, so the user may need to manipulate the pixels directly.
>Limited control over digital data.
