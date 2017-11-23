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

import time
from SabertoothSerial.SabertoothDriverSimple import SerialMotorControl

# Basic autonomous to test all directions on your robot, assuming it is a drive train

# This cannot be interrupted normally! If using with robot drive train, prop wheels up off of the ground for testing

# Basic pseudo code
# - Stop motors
# - Wait for 1 second
# - Drive forward for 2 seconds at 100% power
# - Drive backward for 2 seconds at 100% power
# - Drive left (on a dime) for 2 seconds at 100% power
# - Drive right (on a dime) for 2 seconds at 100% power
# - Drive forward for 2 seconds at 50% power, manually controlling the motor opposed to using helper
# functions that assume drive train usage
# - Stop


# Setup SerialMotorControl from SabertoothSerial.SabertoothDriverSimple, passing in the serial port
motors = SerialMotorControl('/dev/ttyUSB0')  # This will be different for you


def run():
    motors.stop()
    time.sleep(1)
    motors.drive_forward(100)
    time.sleep(2)
    motors.drive_backward(100)
    time.sleep(2)
    motors.drive_left(100)
    time.sleep(2)
    motors.drive_right(100)
    time.sleep(2)
    motors.motor_raw_simple(0, 50)  # Individual Motor control, starting at 0
    motors.motor_raw_simple(1, 50)
    time.sleep(2)
    motors.stop()


if __name__ == '__main__':
    run()
