from gpiozero import Servo
import time
import os

# Initialize servo on GPIO pin 17
servo = Servo(17)
servo_is_active = False  # Track the servo state

def control_servo(command):
    global servo_is_active  # To modify the servo state variable

    # Move servo to the 'up' position when "አበበ" is spoken
    if "አበበ" in command:  # Command for standing up
        if not servo_is_active:
            servo.max()  # Move servo to maximum (fully up)
            servo_is_active = True
            print("Servo moved to 'stand up' position")
        else:
            print("Servo is already in 'stand up' position")

    # Move servo to the 'down' position when "ከበደ" is spoken
    elif "ከበደ" in command:  # Command for laying down
        if servo_is_active:
            servo.min()  # Move servo to minimum (fully down)
            servo_is_active = False
            print("Servo moved to 'lay down' position")
        else:
            print("Servo is already in 'lay down' position")

    else:
        print("Unknown command:", command)

def read_command_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            command = file.read().strip()
        os.remove(file_path)  # Remove the file after reading the command
        return command
    return None

if __name__ == '__main__':
    try:
        file_path = '/home/pi/command_input.txt'  # The file where the command will be written by the PC
        while True:
            command = read_command_from_file(file_path)
            if command:
                control_servo(command)
            time.sleep(0.4)  # Check for commands every 0.4 seconds
    except KeyboardInterrupt:
        print("Program exiting")
