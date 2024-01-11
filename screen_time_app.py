import time
import os
from datetime import datetime
from plyer import notification
from playsound import playsound


def check_time_and_lock():
    while True:
        # Check the current time
        current_time = datetime.now()
        current_time_notification = f"Current time is: {datetime.now().hour}:{datetime.now().minute}"
        current_hour = int(current_time.strftime("%H"))

        # Check if the current time is between 11 PM and 6 AM
        if 23 <= current_hour or current_hour < 6:
            # Notify the user
            print(current_time_notification)
            notification.notify(
                title='Screen Time Alert',
                message='Your screen time is up! The computer will lock after the song is finished.',
                app_name='Love yourself.',
                app_icon=r'',  # Replace this with a .ico of Josh Hutcherson, or whoever you like
                timeout=30  # The notification stays for 30 seconds
            )
            playsound(r'')  # Replace this with a .mp3 of the whistling meme, or whatever you like

            # Lock the computer (This command might vary based on your operating system)
            if os.name == 'nt':  # For Windows
                os.system("rundll32.exe user32.dll,LockWorkStation")
            elif os.name == 'posix':  # For Unix/Linux
                os.system("gnome-screensaver-command -l")

            # Wait until it's past 6 AM to restart the cycle
            while int(datetime.now().strftime("%H")) < 6:
                time.sleep(60)

        # If it's not within the time range, check every minute
        else:
            print(current_time_notification)
            time.sleep(60)


# Run the function
check_time_and_lock()
