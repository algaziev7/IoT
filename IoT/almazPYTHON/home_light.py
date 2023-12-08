import tkinter as tk
import random

class home_light:
    def __init__(self, device_id, initial_value=0):
        self.device_id = device_id
        self.status = False
        self.value = initial_value

    def toggle_device(self):
        self.status = not self.status

    def set_value(self, level):
        if 0 <= level <= 100:
            self.value = level

    def simulate_change(self):
        if self.status:
            self.value = random.randint(0, 100)
