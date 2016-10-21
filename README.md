# Mote® API

The Mote® API is a simple HTTP API written in Python, using the standard Mote library provided by Pimoroni® to allow the Mote to be controlled by a remote device. The initial version of this API is based on the code provided in the **[Using Mote with Homekit and Siri](https://learn.pimoroni.com/tutorial/sandyj/using-mote-with-homekit-and-siri)** tutorial, and is provided here for easy download.

## Pre-requisites
The Mote API requires the Mote Python library from Pimoroni and the Flask.

If your Mote is connected to a Raspberry Pi (running Raspbian), the recommended way to install is to use the following command:
```
curl -sS get.pimoroni.com/mote | bash
```
Alternatively you can use pip:
```
sudo pip install mote
```
Flask is also installed via pip:
```
sudo pip install flask
```

## Using the API
Download the moteapi.py file to a suitable location, and run it using:
```
python moteapi.py
```
This will start the API in the foreground. To run the API in the background, or to have it automatically start on system boot, please refer to the appropriate documentation for your OS.

The API uses port 5000, and so the URL required to access it is:
```
http://{device ip address}:5000
```

## Known Restrictions
* To change the port used by the API you need to update the code accordingly. Refer to the Flask documentation for this.
* If there are multiple Mote hosts connected to a system, the API can only control the first one
* The API will set all Mote sticks connected to the host to the same colour.

### Raising Issues
Issues can be raised via the **[GitHub Issue tracker](https://github.com/EarthstormSoftware/controllerformote-api/issues)**. 

### Contributing
Before raising a pull request, it's recommended to raise an issue to enable discussion of the suggested change before spending time coding it. If there is no existing issue, please raise a new one. This is to reduce frustration at spending precious time crafting a change only for it to be rejected.

#### Trademarks
Pimoroni and Mote are trademarks of Pimoroni Ltd
