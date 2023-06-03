
# media-control-android

This Python script is a simple script to toggle media settings on an Android device. It allows you to control the settings from your Linux or Mac machine using `adb`, without having to fiddle around with the device's settings directly or install unnecessary software.

## Installation
REQUIREMENTS:
`adb` will need to be installed and configured on the connected Linux/Mac machine

You need to enable Wireless Debugging on the Android device.

More information about how to configure `adb`, as well as instructions on how to enable Wireless Debugging, can be found in the [Android Platform Guide](https://source.android.com/setup/build/running).

Enable wireless debugging in the Developer options menu.

Connect the device over USB and click the notification to trust the computer.

Confirm the device is recognised by running:
`adb devices`

Run the following to enable wireless debugging:
`adb tcpip 5555`

## Usage
The script should immediately recognise any previously connected devices that are currently broadcasting on tcp 5555 on wifi.
