import tkinter as tk
import random

class TemperatureControl:
    def __init__(self, device_id, initial_temperature=20):
        self.device_id = device_id
        self.status = False
        self.temperature = initial_temperature

    def toggle_control(self):
        self.status = not self.status

    def set_temperature(self, temp):
        if 10 <= temp <= 30:
            self.temperature = temp

    def simulate_change(self):
        if self.status:
            self.temperature = random.randint(10, 30)