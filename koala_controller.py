"""project_3_controller controller."""

import atexit
import sys
import threading as thread
import tkinter

import master_server as Master

from controller import Robot

robot = Robot()

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')

timeStep = 256
top_speed = 6.28
msToSeconds = 0.0001
wheelSpeed = top_speed * 0.5

  
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0) 

left_pos_sensor = robot.getPositionSensor('left wheel sensor')
right_pos_sensor = robot.getPositionSensor('right wheel sensor')
left_pos_sensor.enable(timeStep)
right_pos_sensor.enable(timeStep)

def wheelDist():
    return  (left_pos_sensor.getValue() + right_pos_sensor.getValue()) * timeStep * msToSeconds * 0.5

def onExit():
    leftMotor.setVelocity(0.0)
    rightMotor.setVelocity(0.0)

atexit.register(onExit)

while robot.timeStep() != -1:
    pass #TODO: Implement control logic.

print("Shutdown.")