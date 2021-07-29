import argparse
import yaml
import logging
from gen_coordinates import Generator
from detector import MotionDetector
from line_colors import *


def main():
    logging.basicConfig(level=logging.INFO)
    #set the frame and the the video and images on start
    image_file = "images/parkinglot.png"
    data_file = "data/coordinates.yml"
    start_frame = 2
    video_file = "videos/parkinglot.mp4"
    #Read the coordinates drawn and generate on screen in video
    if image_file is not None:
        with open(data_file, "w+") as points:
            generator = Generator(image_file, points, COLOR_RED)
            generator.generate()

    with open(data_file, "r") as data:
        points = yaml.safe_load(data)
        detector = MotionDetector(video_file, points, int(start_frame))
        detector.detect_motion()

#Parse the data together 
def parse_data():
    parser = argparse.ArgumentParser(description='Generates Coordinates File')

    parser.add_argument("--image",
                        dest="image_file",
                        required=False,
                        help="Image file to generate coordinates on")

    parser.add_argument("--video",
                        dest="video_file",
                        required=True,
                        help="Video file to detect motion on")

    parser.add_argument("--data",
                        dest="data_file",
                        required=True,
                        help="Data file to be used with OpenCV")

    parser.add_argument("--start-frame",
                        dest="start_frame",
                        required=False,
                        default=1,
                        help="Starting frame on the video")

    return parser.parse_data()


if __name__ == '__main__':
    main()
