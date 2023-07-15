from PIL import Image

def encode_message(image_path, message):

    image = Image.open(image_path)
    pixel_map = image.load()
    message = message + "~"
    binary_message = ''.join(format(ord(c), '08b') for c in message)

    padding_length = (3 - len(binary_message) % 3) % 3
    binary_message += '0' * padding_length

    width, height = image.size
    index = 0
    for i in range(width):
        for j in range(height):
            r, g, b = pixel_map[i, j]
            if index < len(binary_message):
                pixel_map[i, j] = (r - r % 2 + int(binary_message[index]), g - g % 2 + int(binary_message[index+1]), b - b % 2 + int(binary_message[index+2]))
                index += 3
            else:
                break
        else:
            continue
        break

    image.save("encoded_image.png")

def decode_message(encoded_image_path):

    encoded_image = Image.open(encoded_image_path)
    pixel_map = encoded_image.load()

    binary_message = ""
    width, height = encoded_image.size
    for i in range(width):
        for j in range(height):
            r, g, b = pixel_map[i, j]
            binary_message += str(r % 2)
            binary_message += str(g % 2)
            binary_message += str(b % 2)

    message = ""
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))
        if message[-1] == "~":
            break

    return message[:-1]



while True:

    choice = input("Enter '1' to encode a message, '2' to decode a message, or 'q' to quit: ")

    if choice == '1':
        img_path=input("Enter the path of the encoded image:")
        image_path = img_path
        message = input("Enter the message to encode: ")
        encode_message(image_path, message)
        end_task="Message encoded successfully.\n\n\n"
        print(end_task)

    elif choice == '2':
        encoded_image_path = input("Enter the path of the decoded image: ")
        decoded_message = decode_message(encoded_image_path)
        print("Decoded message:", decoded_message)
        end_task="Message decoded successfully.\n\n\n"
        print(end_task)
    elif choice == 'q':
        break

    else:
        print("Invalid choice. Please enter '1', '2', or 'q'.")