# henriette

Henriette is a remote controlled swan.

/henOS.py henriette operating system

henOS is the main server of henriette. Its purpose is to control all the sensors and motors and it providers a rest endpoint to control the swans movement.

# Boot sequence

At startup henOS.py is downloaded from github and automatically started. This ensures that always the newest version is running. The startup sequence is running and displays the main information on the display.

# Display

The HD44780 display shows relevant information inside the swan and is needed for maintenance. On startup it shows the current version of henOS, the battery status, current IP address and network status. This makes it easy to get a direct connection.

# 



/console.py



