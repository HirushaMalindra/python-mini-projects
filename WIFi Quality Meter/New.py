import pywifi
import time
wifi = pywifi.pywifi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(3)
for n in iface.scan_results():
    if n.signal>-50:
        q="Exellent"
    elif n.signal>-65:
        q="Good"