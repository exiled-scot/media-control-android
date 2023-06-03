import subprocess
import time

# Define the media commands to be sent via adb shell
media_commands = [
    'input keyevent KEYCODE_MEDIA_PLAY_PAUSE',
    'input keyevent KEYCODE_MEDIA_NEXT',
    'input keyevent KEYCODE_MEDIA_PREVIOUS'
]

# Set the ADB binary path - make sure ADB is added to your user/system path
# or specify the full path to the ADB binary below.
adb_binary = 'adb'

# Run the adb devices command and capture the output
output = subprocess.check_output(['adb', 'devices']).decode().split('\n')

ip_address = ''
# Loop through each line of the output
for line in output:
    # Check if the line contains an IP address
    if '.' in line:
        # Extract the IP address and print it
        ip_address = line.split()[0]
        print("Found device at IP:", ip_address)

# Connect to the device wirelessly
subprocess.call([adb_binary, 'connect', f'{ip_address}'])

# Send the media commands
for cmd in media_commands:
    subprocess.call([adb_binary, '-s', f'{ip_address}', 'shell', cmd])
