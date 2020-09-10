# CroniclePlugins
My repository for my Cronicle Plugins

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
