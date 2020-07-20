#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

# Initialize the EV3 Brick
ev3 = EV3Brick()

# Set volume to 100% and make a beep to signify program has started
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Turn off the light
ev3.light.off()

# Initialize EV3 touch sensor and motors
colour = ColorSensor(Port.S1)
nextColour = None

# Create a loop to react to buttons
while True:

    # Check for center button events
    if Button.CENTER in ev3.buttons.pressed():
        ev3.light.off()
        break

    # Fetch the colour using the colour sensor
    nextColour = colour.color()

    # Check the sensor colour and change the EV3 light and speak the
    # colour. The EV3 light only supports four colours, for other colours
    # simply speak the colour. 
    if nextColour == Color.RED:
        ev3.light.on(Color.RED)
        ev3.speaker.say("Red detected")

    elif nextColour == Color.GREEN:
        ev3.light.on(Color.GREEN)
        ev3.speaker.say("Green detected")

    elif nextColour == Color.ORANGE:
        ev3.light.on(Color.ORANGE)
        ev3.speaker.say("Orange detected")

    elif nextColour == Color.YELLOW:
        ev3.light.on(Color.YELLOW)
        ev3.speaker.say("Yellow detected")

    elif nextColour is not None:

        ev3.light.off()

        if nextColour == Color.BLACK:
            ev3.speaker.say("Black detected")
        elif nextColour == Color.BLUE:
            ev3.speaker.say("Blue detected")
        elif nextColour == Color.WHITE:
            ev3.speaker.say("White detected")
        elif nextColour == Color.BROWN:
            ev3.speaker.say("Brown detected")
        elif nextColour == Color.PURPLE:
            ev3.speaker.say("Purple detected")

    # If no colours are detected turn the light off.
    else:
        ev3.light.off()

    # Check colour using RGB format
    print("Colours: ", colour.rgb())
    wait(10)

    # Checn ambience
    print("Ambient: ", colour.ambient())
    wait(10)

    # Check reflection
    print("Reflection: ", colour.reflection())
    wait(10)

    # Check colour
    print("Colour: ", colour.color())
    wait(10)

# Use the speech tool to signify the program has finished
ev3.speaker.say("Program complete")
