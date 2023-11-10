import ffmpeg
import subprocess

import numpy as np
from scipy.fftpack import dct, idct

# EXERCISE 1

print("\nEXERCISE 1: ")


def rgb_to_yuv(r, g, b):
    y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    u = -0.148 * r - 0.291 * g + 0.439 * b + 128
    v = 0.439 * r - 0.368 * g - 0.071 * b + 128

    return y, u, v


def yuv_to_rgb(y, u, v):
    r = 1.164 * (Y - 16) + 1.596 * (V - 128)
    g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (U - 128)
    b = 1.164 * (y - 16) + 2.018 * (u - 128)

    return r, g, b


print("RGB to YUV: ")
(R, G, B) = (255, 255, 255)
print("R: ", R, "G: ", G, "B: ", B)
(Y, U, V) = rgb_to_yuv(R, G, B)
print("Y: ", Y, "U: ", U, "V: ", V)

print("\n YUB to RGB: ")
(Y, U, V) = (235.04500000000002, 128, 128)
print("Y: ", Y, "U: ", U, "V: ", V)
(R, G, B) = yuv_to_rgb(Y, U, V)
print("R: ", R, "G: ", G, "B: ", B)


# EXERCISE 2

print("\nEXERCISE 2: ")


def image_resize(input_image, output_image, new_width, new_height):
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_image,
        "-vf", f"scale={new_width}:{new_height}",
        output_image
    ]

    subprocess.run(ffmpeg_command)


original_image = "input.jpg"
output = "output_resized.png"
width = 320
height = 240

image_resize(original_image, output, width, height)

print("\nCODE OF EXERCISE 2 EXECUTED WITH SUCCESS! THE OUTPUT IMAGE IS IN THE PROJECT FOLDER.")


# EXERCISE 3

print("\nEXERCISE 3: ")


def serpentine_image_reading(image_path):
    with open(image_path, 'rb') as file:

        information_bytes = file.read()
        image_width = int.from_bytes(information_bytes[163:165], byteorder='big')

        zigzag_pattern = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (3, 0), (2, 1),
                          (1, 2), (0, 3), (0, 4), (1, 3), (2, 2), (3, 1), (4, 0), (5, 0)]

        for coord in zigzag_pattern:
            x, y = coord
            index = 167 + (y * image_width + x) * 3
            print(information_bytes[index:index + 3])


image = "input.jpg"
serpentine_image_reading(image)


# EXERCISE 4

print("\nEXERCISE 4: ")


def color_to_black_and_white_image_converter(input_image, output_image):
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_image,
        "-vf", "format=gray",
        output_image
    ]

    subprocess.run(ffmpeg_command)


original_image = "input.jpg"
output = "output_black_white.png"

color_to_black_and_white_image_converter(original_image, output)

print("\nCODE OF EXERCISE 4 EXECUTED WITH SUCCESS! THE OUTPUT IMAGE IS IN THE PROJECT FOLDER.")


# EXERCISE 5

print("\nEXERCISE 5: ")


def run_length_encoding_function(input_message):
    encoded_message = ""
    i = 0
    while i <= len(input_message) - 1:
        count = 1
        character = input_message[i]
        j = i
        while j < len(input_message) - 1:
            if input_message[j] == input_message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + character
        i = j + 1

    return encoded_message


m = "AuuBBBCCCCCCcccccCCCCCCCCCA"
m_encoded = run_length_encoding_function(m)
print("The run-length encoded sequence for", m, "is", m_encoded)


# EXERCISE 6

print("\nEXERCISE 6: ")


class DCT:
    def __init__(self):
        pass

    @staticmethod
    def encode_information(input_information):
        encoded_information = dct(dct(input_information.T, norm='ortho').T, norm='ortho')
        return encoded_information

    @staticmethod
    def decode_information(encoded_information):
        decoded_information = idct(idct(encoded_information.T, norm='ortho').T, norm='ortho')
        return decoded_information


DCT_instance = DCT()

input_matrix = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])

encoded_matrix = DCT_instance.encode_information(input_matrix)
decoded_matrix = DCT_instance.decode_information(encoded_matrix)

print("Input Matrix:")
print(input_matrix)

print("\nEncoded Matrix:")
print(encoded_matrix)

print("\nDecoded Matrix:")
print(decoded_matrix)
