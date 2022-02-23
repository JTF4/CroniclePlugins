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
2. Run `pip install obs-websocket-py`
3. Copy `obs.py` to your Cronicle plugins directory
4. Install OBS Plugin in Cronicle
   * Requires the following parameters:
      * `host`: Text Field: IP Address of OBS computer.
      * `port`: Text Field: Port that OBS websockets is using. Example: `4444`
      * `password`: Text Field: Password that OBS websockets is using.
      * `command`: Menu: Command to send to OBS. Items: Start Streaming Bool, Stop Stream, Start Stream, Switch Scene
      * `destinationScene`: Text Field: Scene to switch to in OBS
      * `enableOverride`: Menu: Allows you to switch scenes even if already streaming. Items: True, False

# PJ Link
## About
This is a Cronicle Plugin that allows you to control any proejector that support PJLink Class 1

## Installation
1. Run `pip install pypjlink2` to install the required libraries
2. Copy the pjlink.py plugin to your Cronicle plugin directory
3. Install OBS Plugin in Cronicle
   * Requires the following parameters:
      * `host`: Text Field: IP Address of OBS computer.
      * `command`: Menu: Selects from the available commands Items: `On, Off`

# SnapAV WattBox
## About
This is a Cronicle Plugin that allows you to control the WattBox family of products by SnapAV

The plugin's repo is located at [here](https://github.com/JTF4/cronicle-plugin-snapav-wattbox).

## Installation
1. CD to your Cronicle plugin directory in a terminal
2. Run `npm install cronicle-plugin-snapav-wattbox` to install the plugin and it's required libraries.
3. Setup the plugin in Cronicle.
   * Plugin directory will be `<Your Plugin Folder>/node_modules/cronicle-plugin-snapav-wattbox/index.js`
   * The plugin requires the following parameters:
      * `ip`: Text Field: IP Address of OBS computer.
      * `command`: Menu: Selects from the available commands Items:
        * `Power Off, Power On, Power Reset, Auto Reboot On, Auto Reboot Off`
      * `outlet`: Text Field: The outlet number you want to control.
      * `username`: Text Field: The username for the WattBox.
      * `password`: Text Field: The password for the WattBox.
