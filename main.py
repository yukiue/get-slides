#!/usr/bin/env python3

import cv2


def main():
    path = 'sample.mp4'
    cap = cv2.VideoCapture(path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frames = []
    for i in range(1, frame_count, fps):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        frame = cap.read()[1]
        frames.append(frame)
        cv2.imwrite('out/{:0=4}.jpg'.format(i), frame)

    cap.release()


if __name__ == "__main__":
    main()
