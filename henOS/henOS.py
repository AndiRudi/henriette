import SimpleHTTPServer
import SocketServer
import lcddriver
import netifaces
import json
from datetime import datetime
from time import *



PORT = 8000

# Main Application

lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("henOS starting up", 1)
lcd.lcd_display_string(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 2)


# Use netifaces to get the IP
addrs = netifaces.ifaddresses('wlan0')
addr = json.load(addrs[netifaces.AF_INET])
lcd.lcd_display_string(str(addr[0]['addr']), 3)


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
