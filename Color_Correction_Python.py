import cv2
import numpy as np
clip = cv2.VideoCapture(r"\Users\ILLEGEAR\Desktop\APU\Year 2\Sem 2\ISE\Group Video\ori_dark.mp4")

while True:
    ret, frame = clip.read()

    if not ret:
        break

    lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    l_channel, a_channel, b_channel = cv2.split(lab_frame)

    lift = 35
    gamma = 1.8
    gain = 1.5

    l_channel = np.uint8(np.clip((l_channel + lift) * gamma, 0, 255))

    lab_frame = cv2.merge((l_channel, a_channel, b_channel))

    corrected_frame = cv2.cvtColor(lab_frame, cv2.COLOR_LAB2BGR)

    cv2.imshow('Original', frame)
    cv2.imshow('Corrected', corrected_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

clip.release()
cv2.destroyAllWindows()