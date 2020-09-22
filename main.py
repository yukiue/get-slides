#!/usr/bin/env python3

import cv2
import numpy as np


def main():
    path = 'sample.mp4'
    cap = cv2.VideoCapture(path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
    frames.append(cap.read()[1])

    for i in range(2, frame_count, fps):
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
