import socket
import requests

#discover function
def discover(ip=True, name=False, type=False, ipv6=False, ssid=False, bssid=False, _id=False, timeout='2.50', debug=False):
    #request the data to the nanoleaf api
    data = requests.get('https://my.nanoleaf.me/api/v1/devices/discover', timeout)
    #parse the data
    datas = data.json()
    finaldict = []
    #return error or empty dict

    try:
        #for each device display, ip, name etc in function of the parameter
        for i in range(len(datas)):
            nanoleaf_dict = {}
            dicte = datas[i]
            ips = dicte.get('private_ipv4')
            if ip == True:
                nanoleaf_dict.update({'ip':ips})
            if ipv6 == True:
                ipv6s = dicte.get('private_ipv6')
                nanoleaf_dict.update({'ipv6' : ipv6s})
            if ssid == True:
                sside = dicte.get('ssid')
                nanoleaf_dict.update({'ssid' : sside})
            if bssid == True:
                bsside = dicte.get('bssid')
                nanoleaf_dict.update({'bssid' : bsside})
            if _id == True:
                id = dicte.get('_id')
                nanoleaf_dict.update({'id' : id})
            if name == True:
                #lookup for the device name
                names = socket.getfqdn(ips)
                #remove the .home after the name
                beautiful = names.split(".", 1)[0]
                nanoleaf_dict.update({'name' : beautiful})
            if type == True:
                types = dicte.get('model')
                if types == 'NL29':
                    types = 'Canvas'
                elif types == 'NL22':
                    types = 'Aurora'
                else:
                    types = 'Shapes'
                nanoleaf_dict.update({'type' : types})
            #append final dict
            finaldict.append(nanoleaf_dict)
        print(finaldict)
        return finaldict
    except:
        if debug == True:
            print( {'error' : datas.get('status')} )
            return {'error' : datas.get('status')}
        else:
            print(finaldict)
            return finaldict