import tkinter as tk
import random
from SmartCamera import SmartCamera
from TemperatureControl import TemperatureControl
from home_light import home_light


class HomeAutomationSystem:
    def __init__(self):
        self.devices = {'device': None, 'control': None, 'camera': None}

    def add_component(self, component):
        if isinstance(component, home_light):
            self.devices['device'] = component
        elif isinstance(component, TemperatureControl):
            self.devices['control'] = component
        elif isinstance(component, SmartCamera):
            self.devices['camera'] = component

    def simulate(self):
        for component in self.devices.values():
            if component:
                component.simulate_change()

class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Intelligent Home IoT Simulator")

        self.device = home_light(device_id='device1')
        self.control = TemperatureControl(device_id='control1')
        self.camera = SmartCamera(device_id='camera1')
        self.automation_system = HomeAutomationSystem()

        self.automation_system.add_component(self.device)
        self.automation_system.add_component(self.control)
        self.automation_system.add_component(self.camera)

        self.setup_interface()

    def setup_interface(self):
        self.text_display = tk.Text(relief=tk.SUNKEN, borderwidth=2)
        self.text_display.pack()

        self.text_display.insert("1.0", "Living Area Device: SmartDevice Status: OFF\n")

        self.device_value_slider = tk.Scale(self, from_=0, to=100, orient='horizontal',
                                            command=self.adjust_device_value)
        self.device_value_slider.pack()

        self.device_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_device)
        self.device_toggle_button.pack()

        self.device_value_label = tk.Label(self, text="Living Area Device - off")
        self.device_value_label.pack()

        self.text_display.insert("2.0", "Living Area Temperature Control: Control Status: OFF\n")

        self.control_temperature_slider = tk.Scale(self, fr = 10, to = 30, orient='horizontal',
                                                  command=self.adjust_control_temperature)
        self.control_temperature_slider.pack()

        self.control_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_control)
        self.control_toggle_button.pack()

        self.control_temperature_label = tk.Label(self, text="Living Area Temperature Control - off")
        self.control_temperature_label.pack()

        self.text_display.insert("3.0", "Main Entrance  Camera: SecurityCamera Status: OFF")

        self.camera_status_label = tk.Label(self, text="SecurityCamera Status: OFF")
        self.camera_status_label.pack()

        self.camera_motion_button = tk.Button(self, text="Random Detect Motion", command=self.simulate_camera_motion)
        self.camera_motion_button.pack()
        self.camera_toggle_button = tk.Button(self, text="Toggle ON/OFF", command=self.toggle_camera)
        self.camera_toggle_button.pack()

    def toggle_device(self):
        self.device.toggle_device()
        state = "ON" if self.device.status else "OFF"
        self.text_display.delete("1.0", "1.end")
        self.text_display.insert("1.0", f"Living Area Device: SmartDevice Status: {state}")
        self.device_value_label.config(
            text=f"Living Area Device - {self.device.value}%" if self.device.status else "Living Area Device - OFF")

        if not self.device.status:
            self.device_value_label.config(text="Living Area Device - OFF")

    def adjust_device_value(self, val):
        device_value = int(val)
        self.device.set_value(device_value)
        if self.device.status:
            self.device_value_label.config(text=f"Living Area Device - {device_value}%")

    def toggle_control(self):
        self.control.toggle_control()
        state = "ON" if self.control.status else "OFF"
        self.text_display.delete("2.0", "2.end")
        self.text_display.insert("2.0", f"Living Area Temperature Control: Control Status: {state}")

        if not self.control.status:
            self.control_temperature_label.config(text="Living Area Temperature Control - OFF")

    def adjust_control_temperature(self, val):
        control_temperature = int(val)
        self.control.set_temperature(control_temperature)
        if self.control.status:
            self.control_temperature_label.config(text=f"Living Area Temperature Control - {control_temperature}°C")

    def simulate_camera_motion(self):
        if self.camera.status:
            self.camera.simulate_motion()
            motion = "YES" if self.camera.motion_detected else "NO"
            self.camera_status_label.config(text=f"Main Entrance  Camera: Motion: {motion}")
            if self.camera.motion_detected and not self.device.status:
                self.toggle_device()
        else:
            self.camera_status_label.config(text=f"Main Entrance  Camera: Motion: NO")

    def toggle_camera(self):
        self.camera.toggle_camera()
        state = "ON" if self.camera.status else "OFF"
        self.text_display.delete("3.0", "3.end")
        self.text_display.insert("3.0", f"Main Entrance Camera: SecurityCamera: {state}")

        if self.camera.status:
            self.simulate_camera_motion()

    def update(self):
        self.automation_system.simulate()
        if self.device.status:
            self.device_value_label.config(text=f"Living Area Device - {self.device.value}%")
        if self.control.status:
            self.control_temperature_label.config(text=f"Living Area Temperature Control - {self.control.temperature}°C")
        self.after(900, self.update)

if __name__ == "__main__":
    app = SmartHomeApp()
    app.after(900, app.update)
    app.mainloop()
