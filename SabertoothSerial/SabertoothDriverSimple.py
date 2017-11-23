#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2017, 
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Brendon Telman nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

# Simple Serial Motor Driver for the SaberTooth Motor Drivers

import serial


class SerialMotorControl:
    serialPort = '/dev/ttyUSB0'
    # Setup usb serial communication. If you have multiple usb serial devices, this may need to be changed.
    # This cannot detect which one is the SaberTooth
    ard = 0

    def __init__(self):
        self.ard = serial.Serial(self.serialPort, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

    @staticmethod
    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))

    # set serial port. if this is not done, it assumes '/dev/ttyUSB0', or may not even work at all
    def set_serial_port(self, port):
        self.serialPort = port
        self.stop()

    def get_byte_of_motor(self, motor, power):
        power = self.constrain(power, -127, 127)
        magnitude = abs(power) >> 1
        command = 0
        if motor == 0:
            if power < 0:
                command = 63 - magnitude
            else:
                command = 64 + magnitude
        else:
            if motor == 1:
                if power < 0:
                    command = 191 - magnitude
                else:
                    command = 192 + magnitude
        command = self.constrain(command, 1, 254)
        return command

    # send a command to motors (0 = motor 1, 1 = motor 2, -100 < power < 100)
    def motor_raw_simple(self, motor, power):
        data = self.get_byte_of_motor(motor, power)
        self.motor_raw(data)

    def motor_raw(self, data):
        self.ard.write(chr(data))

    def drive_both(self, left_power, right_power):
        self.motor_raw_simple(0, left_power)
        self.motor_raw_simple(1, right_power)

    def drive(self, power):
        self.drive_both(power, power)

    def drive_forward(self, power):
        self.drive(power)

    def drive_backward(self, power):
        self.drive(-power)

    def drive_left(self, power):
        self.drive_both(-power, power)

    def drive_right(self, power):
        self.drive_both(power, -power)

    def stop(self):
        self.drive(0)
