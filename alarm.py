import datetime
import time
import os

def set_alarm():
    while True:
        alarm_time = input("Enter the time in 24 hour format (HH:MM): ")
        try:
            datetime.datetime.strptime(alarm_time, '%H:%M')
            break
        except ValueError:
            print("Invalid time format! Please enter time in HH:MM format.")
    
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            print("Time's up!")
            os.system('takkanhilang.wav') # ganti dengan nama file musik atau audio yang ingin digunakan sebagai alarm
            break

if __name__ == '__main__':
    set_alarm()