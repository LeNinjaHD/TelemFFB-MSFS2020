from sdl2 import *
import json
import os
import SimConnect
import yaml

SDL_Init(SDL_INIT_JOYSTICK)
SDL_Init(SDL_INIT_HAPTIC)


def find_haptic_joystick():
    for i in range(0, SDL_NumJoysticks()):
        joy = SDL_JoystickOpen(i)
        try:
            if SDL_JoystickIsHaptic(joy):
                print(f"Found FFB: {SDL_JoystickName(joy)} index {i}")
                break
        finally:
            SDL_JoystickClose(joy)
    return i


joystick = SDL_HapticOpenFromJoystick(SDL_JoystickOpen(find_haptic_joystick()))


#INIT SIMCONNECT

sm = SimConnect.SimConnect()
aq = SimConnect.AircraftRequests(sm, _time=2000)

#

config_path = "config.json"

if (os.path.isfile(config_path)):
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
else:
    with open("config.yml", "w") as ymlfile:
        cfg = yaml.load(ymlfile)
