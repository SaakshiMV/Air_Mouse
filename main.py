import cv2
import time
import math
from hand_tracking.tracker import HandTracker
from mouse_control.controller import MouseController
from utils import config

def distance(p1, p2):
    return math.hypot(p2[1] - p1[1], p2[2] - p1[2])

def is_fist(landmarks):
    tips = [8, 12, 16, 20]
    folded = 0

    for tip in tips:
        _, tx, ty = landmarks[tip]
        _, bx, by = landmarks[tip - 2]

        if ty > by:
            folded += 1

    return folded >= 3

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, config.CAM_WIDTH)
    cap.set(4, config.CAM_HEIGHT)

    tracker = HandTracker()
    mouse = MouseController()

    prev_time = 0

    while True:
        success, frame = cap.read()
        frame = cv2.flip(frame, 1)

        tracker.find_hands(frame)
        tracker.draw_hands(frame)
        landmarks = tracker.get_landmarks(frame)

        h, w, _ = frame.shape

        # Bounding Box
        m = config.FRAME_MARGIN
        cv2.rectangle(frame, (m, m), (w - m, h - m), (255, 0, 0), 2)

        mode_text = "NO HAND"

        if landmarks:
            if is_fist(landmarks):
                mode_text = "PAUSE"
            else:
                _, x, y = landmarks[8]
                mouse.move_cursor(x, y, w, h)

                thumb = landmarks[4]
                index = landmarks[8]
                middle = landmarks[12]

                click_length = distance(thumb, index)
                scroll_length = distance(index, middle)

                dy = y - mouse.prev_y

                scroll_state = mouse.detect_scroll(scroll_length, dy)
                if scroll_state:
                    mode_text = scroll_state
                else:
                    mode_text = mouse.detect_click_and_drag(click_length)

                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        # FPS Counter
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time

        cv2.putText(frame, f"FPS: {int(fps)}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # UI Label
        cv2.putText(frame, f"MODE: {mode_text}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Air Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()