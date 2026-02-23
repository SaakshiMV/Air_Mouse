import pyautogui
import numpy as np
import math
import time
from utils import config

class MouseController:
    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()
        self.prev_x, self.prev_y = 0, 0
        self.last_click_time = 0
        self.dragging = False

        pyautogui.PAUSE = 0

    def dynamic_smoothening(self, dx, dy):
        speed = math.hypot(dx, dy)

        if speed > 40:
            return 3   # Fast movement → responsive
        elif speed > 15:
            return 5   # Medium movement
        else:
            return config.SMOOTHENING  # Slow → stable

    def move_cursor(self, x, y, frame_w, frame_h):
        margin = config.FRAME_MARGIN

        x = np.clip(x, margin, frame_w - margin)
        y = np.clip(y, margin, frame_h - margin)

        screen_x = np.interp(x, (margin, frame_w - margin), (0, self.screen_w))
        screen_y = np.interp(y, (margin, frame_h - margin), (0, self.screen_h))

        dx = screen_x - self.prev_x
        dy = screen_y - self.prev_y

        if abs(dx) < config.MIN_MOVEMENT_THRESHOLD:
            dx = 0
        if abs(dy) < config.MIN_MOVEMENT_THRESHOLD:
            dy = 0

        smooth = self.dynamic_smoothening(dx, dy)

        curr_x = self.prev_x + dx / smooth
        curr_y = self.prev_y + dy / smooth

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x, self.prev_y = curr_x, curr_y

    def detect_click_and_drag(self, length):
        if length < config.CLICK_THRESHOLD:
            if not self.dragging:
                pyautogui.mouseDown()
                self.dragging = True
                return "DRAG"
        else:
            if self.dragging:
                pyautogui.mouseUp()
                self.dragging = False

        return "MOVE"

    def detect_scroll(self, length, dy):
        if length < config.SCROLL_THRESHOLD:
            if abs(dy) > 2:
                pyautogui.scroll(int(-dy / abs(dy) * config.SCROLL_SPEED))
                return "SCROLL"
        return None