from PIL import Image

def encode_image(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    pixels = encoded.load()
    width, height = img.size

    message += "###"
    if len(message) > width * height:
        print("Message too long to encode in this image.")
        return

    data_index = 0
    done = False

    for row in range(height):
        for col in range(width):
            if data_index < len(message):
                r, g, b = pixels[col, row]
                ascii_val = ord(message[data_index])
                pixels[col, row] = (r, g, ascii_val)
                data_index += 1
            else:
                done = True
                break
        if done:
            break

    encoded.save(output_path, "PNG")
    print(f"[✅] Message encoded and saved as '{output_path}'")

if __name__ == "__main__":
    msg = input("Enter your secret message: ")
    encode_image("sample.jpeg", msg, "encoded_img.png") 
