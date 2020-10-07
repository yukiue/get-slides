#!/usr/bin/env python3

import argparse
import os
import cv2


def has_difference(frame1, frame2, threshold=0.15):
    # Note that frame1 and frame2 have the same shape

    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    height, width = frame1.shape

    pixels = height * width
    same_pixels = 0

    for h in range(height):
        for w in range(width):
            if frame1[h][w] == frame2[h][w]:
                same_pixels += 1

    ratio = (pixels - same_pixels) / pixels

    flag = True

    if ratio < threshold:
        flag = False

    return flag


def parse_args():
    parser = argparse.ArgumentParser(
        description='calculate first hitting time for random walks on network')

    parser.add_argument('file', help='input video file', type=str)
    parser.add_argument('-d', '--duration', type=int, default=1)

    args = parser.parse_args()

    return args


def main():

    args = parse_args()

    path = args.file
    duration = args.duration

    cap = cv2.VideoCapture(path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    frames.append(cap.read()[1])

    for i in range(2, frame_count, fps * duration):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        frame = cap.read()[1]

        if has_difference(frames[-1], frame):
            frames.append(frame)

    cap.release()

    os.mkdir('out')

    for i, frame in enumerate(frames):
        cv2.imwrite('out/{:0=5}.jpg'.format(i), frame)


if __name__ == "__main__":
    main()
