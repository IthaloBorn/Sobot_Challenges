#!/usr/bin/python3
"""
Solis Robot - SoBot

challenge_001_solved.py: Programming challenge for the SoBot to move a simple route.

Created By   : Ithalo A. Nascimento
Version      : 1.0

Company: SENAI - Imperatriz
"""

from time import sleep
import serial

# Set serial port
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Waits data configuration

usb.write(b"LT E1 RD50 GR0 BL0")    # Turn on led tape in red

usb.write(b"MT0 E1")                # Enables wheel motors

sleep(1)

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD0 GR0 BL50")                # Turn led tape in blue
usb.write(b"MT0 E1 D90 L AT1000 DT3950 V25")    # Move 90° to the left

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD50 GR25 BL0")                # Turn led tape in yellow
usb.write(b"MT0 E1 D90 R AT1000 DT3950 V25")    # Move 90° to the right

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD50 GR0 BL0")               # Turn led tape in red
usb.write(b"MT0 E1 D180 R AT5000 DT5000 V25")    # turn around

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD0 GR0 BL50")                # Turn led tape in blue
usb.write(b"MT0 E1 D90 L AT1000 DT3950 V25")    # Move 90° to the left

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD50 GR25 BL0")                # Turn led tape in yellow
usb.write(b"MT0 E1 D90 R AT1000 DT3950 V25")    # Move 90° to the right

usb.write(b"LT E1 RD0 GR50 BL0")               # Turn led tape in green
usb.write(b"MT0 E1 D500 AT5000 DT5000 V25")    # Move forward

usb.write(b"LT E1 RD50 GR0 BL0")               # Turn led tape in red
usb.write(b"MT0 E1 D180 R AT1000 DT5000 V25")    # turn around

usb.write(b"LT E1 RD0 GR0 BL0")    # Turn off led tape

usb.write(b"MT0 E0")                # Disables wheel motors
