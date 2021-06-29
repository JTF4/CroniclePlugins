# CroniclePlugins
A repository for my Cronicle Plugins

# Vizio API Connector
## About
This is a Cronicle Plugin that makes use of vkorn's pyvizio API to control Vizio TVs and speakers.

His repository can be found here: https://github.com/vkorn/pyvizio

## Installation
1. Install pyvisio from https://github.com/vkorn/pyvizio
2. Follow vkorn's instructions on how to setup and get pairing information for the TV or speaker
3. Install Visio API Connector Plugin in Cronicle
    * Requires the following parameters:
      * `ip`: Text Field: IP address of the TV or speaker. Recommend you set a DHCP reservation for the it if you do not want this to change.
      * `command`: Menu: Command to send
      * Items: on
      * `pin`: The pin number obtained from step 2
      * `token`: The Auth Token obtained from step 2
4. Schedule away!

# OBS
## About
This is a Cronicle Plugin that allows you to control OBS Studio using the websockets control.

## Installation
1. Make sure OBS Studio has the websockets plugin installed and configured.
2. Install OBS Plugin in Cronicle
   * Requires the following parameters:
      * `host`: Text Field: IP Address of OBS computer.
      * `port`: Text Field: Port that OBS websockets is using. Example: `4444`
      * `password`: Text Field: Password that OBS websockets is using.
      * `command`: Menu: Command to send to OBS. Items: Start Streaming Bool, Stop Stream, Start Stream, Switch Scene
      * `destinationScene`: Text Field: Scene to switch to in OBS
      * `enableOverride`: Menu: Allows you to switch scenes even if already streaming. Items: True, False
