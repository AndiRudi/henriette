import SimpleHTTPServer
import SocketServer
import lcddriver
from datetime import datetime
from time import *



PORT = 8000

# Main Application

lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string("henOS starting up", 1)
lcd.lcd_display_string(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 2)


# Use netifaces to get the IP





Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
