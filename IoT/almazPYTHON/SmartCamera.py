import tkinter as tk
import random

class SmartCamera:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.motion_detected = False

    def toggle_camera(self):
        self.status = not self.status

    def simulate_motion(self):
        if self.status:
            self.motion_detected = random.choice([True, False])

    def simulate_change(self):
        if self.status:
            self.simulate_motion()
