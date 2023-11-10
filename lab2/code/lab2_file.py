import subprocess
import os

# IMPORTANT! The project folder is "venv". Everything it has to be in that folder in order to be executed correctly.
# In that folder also it has to be the inputs of the previous lab, because of the import of the previous script.

# Import the Lab 1 python file since it's asked in Exercise 5.
# The 2 files needs to be in the same project folder:
from rgb_yuv import image_resize
from rgb_yuv import serpentine_image_reading
from rgb_yuv import color_to_black_and_white_image_converter


# EXERCISE 1

print("\nEXERCISE 1 LAB 2: ")


# IMPORTANT COMMENT: It's strange that the statement asks to convert the "BigBuckBunny" .mp4 video
# into a .mp2 video file (.mp2 it's an audio file!). But since it's what the statement asks, I've done it.
# However, I have also converted the .mp4 video into a .mpeg video, because it has more sense.

def mp2_video_converter(input_video, output_video):  # Function to convert a video into a .mp2 file.
    subprocess.run(['ffmpeg', '-i', input_video, '-c:v', 'mpeg2video', '-c:a', 'mp2', output_video])


def mpeg_video_converter(input_video, output_video):  # Function to convert a video into a .mpeg file.
    subprocess.run(['ffmpeg', '-i', input_video, '-c:v', 'mpeg4', output_video])


def mp2_mpeg_information_parsing(input_file, file_type):  # Function to obtain the info of a .mp2 or .mpeg file.
    result = subprocess.run(['ffmpeg', '-i', input_file], capture_output=True, text=True)
    information = result.stderr

    if file_type == 0:  # Me make that if in order to choose the correct output file name.
        with open('mp2_information_ex1.txt', 'w') as information_file:
            information_file.write(information)

    elif file_type == 1:
        with open('mpeg_information_ex1.txt', 'w') as information_file:
            information_file.write(information)


original_video = 'BigBuckBunny_mp4_video.mp4'
output_mp2 = 'BigBuckBunny_mp2_video.mp2'
output_mpeg = 'BigBuckBunny_mpeg_video.mpeg'

mp2_video_converter(original_video, output_mp2)  # First we convert the .mp4 video into a .mp2 file.
mp2_mpeg_information_parsing(output_mp2, 0)  # Then we parse the .mp2 file and save its information.

# As I have said, I also have converted the .mp4 video into a mpeg file:
mpeg_video_converter(original_video, output_mpeg)  # Also I have converted the .mp4 video onto an .mpeg file.
mp2_mpeg_information_parsing(output_mpeg, 1)   # Then we parse the .mpeg file and save its information.

print("\nCODE OF EXERCISE 1 EXECUTED WITH SUCCESS! THE OUTPUT VIDEO AND THE VIDEO INFO IS IN THE PROJECT FOLDER.")


# EXERCISE 2

print("\nEXERCISE 2 LAB 2: ")


def change_resolution(input_video, output_video, new_width, new_height):
    subprocess.run(['ffmpeg', '-i', input_video, '-vf', f'scale={new_width}:{new_height}', output_video])


# original_video = 'BigBuckBunny_video.mp4'
video_resized = 'output_video_resized_ex2.mp4'

width = 640
height = 480

change_resolution(original_video, video_resized, width, height)

print("\nCODE OF EXERCISE 2 EXECUTED WITH SUCCESS! THE OUTPUT VIDEO IS IN THE PROJECT FOLDER.")
print(f"New Video Resolution: {width}x{height}")


# EXERCISE 3

print("\nEXERCISE 3 LAB 2: ")


def chroma_subsampling_changing(inp, out, subs):
    t3_command = f"ffmpeg -i {inp} -c:v libx264 -vf format={subs} {out}"
    subprocess.run(t3_command, shell=True, check=True)


original_video = "BigBuckBunny_mp4_video.mp4"
output_ex3 = "output_video_changed_subsampling.mp4"

chroma_subsampling_1 = 'yuv444p'
chroma_subsampling_2 = 'yuv422p'
chroma_subsampling_3 = 'yuv420p'

chroma_subsampling_changing(original_video, output_ex3, chroma_subsampling_3)

print("\nCODE OF EXERCISE 3 EXECUTED WITH SUCCESS! THE OUTPUT VIDEO IS IN THE PROJECT FOLDER.")


# EXERCISE 4

print("\nEXERCISE 4 LAB 2: ")


def read_and_print_txt_file_lines(txt_path, lines_to_be_printed_list):
    try:
        with open(txt_path, 'r') as file:
            lines = file.readlines()

            for line_number in lines_to_be_printed_list:
                if 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print(f"Line {line_number} is out of range.")

    except FileNotFoundError:
        print(f"File not found: {txt_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


video_information_file = "mpeg_information_ex1.txt"  # We print 5 relevant data about the .mpeg converted video.
line_list = [12, 13, 14, 15]
read_and_print_txt_file_lines(video_information_file, line_list)


# EXERCISE 5

print("\nEXERCISE 5 LAB 2: ")


# Let's do some interactions with the script of Lab 1.
# We will use some of its functions we have created in the previous Lab.

# Before, we will extract a frame from the "BigBuckBunny" video, because in the
# previous Lab we have created some functions that only works with images.
# We will use those Lab 1 script functions to the frame extracted of the video.

def obtain_video_frame(input_video, output_frame, frame_time):
    cmd = [
        "ffmpeg",
        "-i", input_video,
        "-ss", str(frame_time),
        "-vframes", "1",
        output_frame
    ]
    subprocess.run(cmd)


original_video = "BigBuckBunny_mp4_video.mp4"
frame = "frame.jpg"
time = 32

obtain_video_frame(original_video, frame, time)
print("-> Frame from 'BigBuckBunny' video extracted correctly.")

# First, we will use the function "image_resize" of the previous Lab 1 script:
original_image = "frame.jpg"
output = "frame_resized.png"
width = 320
height = 240

image_resize(original_image, output, width, height)
print("-> 'image_resize' function from the Lab 1 script executed correctly in the Lab 2 script.")
print("-> The output is in the project folder.")

# Second, we will use the function "serpentine_image_reading" of the previous Lab 1 script:
image = "frame.jpg"
serpentine_image_reading(image)
print("-> 'serpentine_image_reading' function from the Lab 1 script executed correctly in the Lab 2 script.")

# Third, we will use the function "color_to_black_and_white_image_converter" of the previous Lab 1 script:
original_image = "frame.jpg"
output = "frame_black_white.png"

color_to_black_and_white_image_converter(original_image, output)
print("-> 'color_to_black_and_white_image_converter' function from the Lab 1 script executed correctly.")
print("-> The output is in the project folder.")
