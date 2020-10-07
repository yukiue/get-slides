#!/usr/bin/env python3

import argparse
import cv2


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
        frames.append(frame)

        # if not np.array_equal(frames[-1], frame):
        #     print(np.array_equal(frames[-1], frame))
        #     frames.append(frame)

    cap.release()

    for i, frame in enumerate(frames):
        cv2.imwrite('out/{:0=5}.jpg'.format(i), frame)


if __name__ == "__main__":
    main()
