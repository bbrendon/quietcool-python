# quietcool-python

A python library for communicating with the discontinued [QuietCool WiFi Smart Control](https://quietcoolsystems.com/support/how-to-setup-and-install-wi-fi-smart-control/).

This is primarily to support the [Home Assistant Integration](https://github.com/bbrendon/homeassistant-quietcool) but use it how you like.

This is a fork of [stabbylambda/quietcool-python](https://github.com/stabbylambda/quietcool-python)


## Usage

QuietCool's WiFi controller works with all the fans in your attic. One controller (the Master Hub) connects to your wifi and the others (the Remote Hubs) connect to the Master. All commands you send to any fan go through the Master Hub, which means you have to initialize the `Hub` class with the IP address of the Master Hub.

```python
async def print_all_fans():
    master_hub_ip = "10.0.0.100"
    hub = await Hub.create(master_hub_ip)
    fans = await hub.get_fans()

    for fan in fans:
        print(fan.name)
```

One you get the `Fan`s, all communication should really be done through those objects.

Currently, the library supports:

* Getting all fans in a system
* Turning them on/off
* Getting/setting current fan speed
* Getting/setting available fan speeds

Things this library doesn't support:

* Setting the fan name
* Configuring the wifi settings for the hub
* Updating firmware
* Reading the fan diagnostics

