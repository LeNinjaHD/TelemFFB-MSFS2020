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


# INIT SIMCONNECT

sm = SimConnect.SimConnect()
aq = SimConnect.AircraftRequests(sm, _time=2000)

# Define a data request for the active aircraft
aircraft_request = sm.create_data_request("PLANE INFO", "ATC MODEL", period=0)

# Get the current state of the aircraft request
aircraft_data = sm.get_data(aircraft_request)

# Extract the active aircraft from the returned data
active_aircraft = aircraft_data['ATC MODEL']

# Print the name of the active aircraft
print(f"The active aircraft is: {active_aircraft}")

#

config_path = "config.json"

if (os.path.isfile(config_path)):
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
else:
    with open("config.yml", "w") as ymlfile:
        cfg = yaml.load(ymlfile)
