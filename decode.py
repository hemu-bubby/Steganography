from PIL import Image

def decode_image(img_path):
    img = Image.open(img_path)
    width, height = img.size
    message = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            message += chr(b)
            if message.endswith("###"):
                return message[:-3]

    return "No hidden message found."

if __name__ == "__main__":
    secret = decode_image("encoded_img.png")
    print(f"[🔓] Hidden Message: {secret}")
