# Nanoleaf Discovery

Nanoleaf Discovery is a Python library to discover every nanoleaf device on the network, the others api use the ssdp protocol to find the nanoleafs, the drawback is that it doesn't work every time so I used the api that the official nanoleaf app uses to find the nanoleafs, this one always works /!\ except with a vpn /!\

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Nanoleaf Discovery

```bash
pip install NanoLeafDiscovery
```

## Options
You can manage different parameters :

| Options | What it does | Value |
| ------- | ------------ | ------- |
| ip | Display IPV4 | True/False |
| name | Display Nanoleaf Name | True/False |
| type | Display Canvas/Shape/Aurora | True/False |
| ipv6 | Display IPV6 | True/False |
| ssid | Display the ssid | True/False |
| bssid | Display the bssid | True/False |
| timeout | Request time before timeout | Int |
| _id | ID of the nanoleaf | True/False |
| debug | If error display it  | True/False |

## Usage

```python
import NanoLeafDiscovery

NanoLeafDiscovery.scan() # returns [{'ip': '192.168.1.1'}]
NanoLeafDiscovery.scan(name=True) # returns [{'ip': 192.168.1.1, 'name': 'Canvas-f77e'}]
NanoLeafDiscovery.scan(name=True, type=True, ip=False) # returns [{'name': 'Canvas-f77e', 'type':'Canvas'}]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
