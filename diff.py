#!/usr/bin/env python3

import cv2
import numpy as np


def main():
    path = 'sample.mp4'
    cap = cv2.VideoCapture(path)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frames = []
    cap.set(cv2.CAP_PROP_POS_FRAMES, 30)
    frames.append(cap.read()[1])
    cap.set(cv2.CAP_PROP_POS_FRAMES, 60)
    frames.append(cap.read()[1])
    cap.set(cv2.CAP_PROP_POS_FRAMES, 600)
    frames.append(cap.read()[1])

    cv2.imwrite('1.jpg', frames[0])
    cv2.imwrite('2.jpg', frames[1])
    cv2.imwrite('3.jpg', frames[2])
    cv2.imwrite('4.jpg', cv2.cvtColor(frames[2], cv2.COLOR_BGR2GRAY))

    print(np.array_equal(frames[0], frames[0]))
    print(np.array_equal(frames[0], frames[1]))
    print(
        np.array_equal(cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY),
                       cv2.cvtColor(frames[1], cv2.COLOR_BGR2GRAY)))
    print(np.array_equal(frames[0], frames[2]))

    print(np.abs(frames[0].astype(int) - frames[0].astype(int)).max())
    print(np.abs(frames[0].astype(int) - frames[1].astype(int)).max())
    print(np.abs(frames[0].astype(int) - frames[2].astype(int)).max())
    print(np.abs(frames[0].astype(int) - frames[0].astype(int)).min())
    print(np.abs(frames[0].astype(int) - frames[1].astype(int)).min())
    print(np.abs(frames[0].astype(int) - frames[2].astype(int)).min())

    # print('diff_12')
    # diff_12 = cv2.absdiff(cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY),
    #                       cv2.cvtColor(frames[1], cv2.COLOR_BGR2GRAY))
    # print(diff_12)

    # print(cv2.threshold(diff_12, 20, 255, cv2.THRESH_BINARY)[1])

    # print('diff_13')
    # diff_13 = cv2.absdiff(cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY),
    #                       cv2.cvtColor(frames[2], cv2.COLOR_BGR2GRAY))
    # print(diff_13)

    # print(cv2.threshold(diff_13, 20, 255, cv2.THRESH_BINARY)[1])

    cap.release()


if __name__ == "__main__":
    main()
