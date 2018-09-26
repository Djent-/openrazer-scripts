#!/usr/bin/python3

from openrazer.client import DeviceManager
from openrazer.client import constants as razer_constants

# Create a DeviceManager. This is used to get specific devices
device_manager = DeviceManager()

# List of effect I've chosen to make an example for
effects = [
    'breath_random',
    'breath_single',
    'breath_dual',
    'breath_triple',
    'reactive',
    'spectrum',
    'static',
    'wave',
    'logo_spectrum',
    'scroll_spectrum',
    'logo_reactive',
    'scroll_reactive',
]

print("Found {} Razer devices".format(len(device_manager.devices)))
print()

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
#device_manager.sync_effects = True

# Iterate over each device and set the wave effect
for device in device_manager.devices:
    print("device.type: {}".format(device.type))
    device_effects = [effect for effect in effects if device.fx.has(effect)]
    print("{} supports {}".format(device.name, device_effects))
    # Set the effect to wave.
    # wave requires a direction, but different effect have different arguments.
    #print(device.fx.reactive(255,255,0, razer_constants.REACTIVE_500MS))
    print('rows, cols: {}, {}'.format(device.fx.advanced.rows, device.fx.advanced.cols))
    print(device.fx.spectrum())
    if device.fx.misc.logo:
        print(device.fx.misc.logo.spectrum())
        print(device.fx.misc.scroll_wheel.spectrum())
