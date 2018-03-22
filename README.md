# Raspi-light-server

Raspi-light-server hosts a web interface to broadcast settings to raspi-light-clients (see https://github.com/justinwagg/raspi-light-client)

## Details

On form submission (setting change), the app publishes the new settings dict to a topic dictated by the device chosen. If a device is listening it can take action on the update. Settings are stored in MySQL.

## Getting Started
From scratch, you'll need a new formatted SD card, a raspberry pi with internet connectivity, and a little creativity.

### Flash SD Card
1. Format new Raspian SD card
Following [raspberrypi.org's documentation]( https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) will be helpful in the next step.
[Download](https://www.raspberrypi.org/downloads/raspbian/) the Raspian image and move to your SD card. From the terminal, having found your SD card mount point:
```
sudo dd bs=1m if=/path/to-your-image.img of=/dev/rdiskn conv=sync
```

1. Once the image is transferred, you'll want to setup headless access. Create a file in `boot` on the SD Card named `wpa_supplicant.conf` with the contents below. Change `SSID` and `PASS` to be your local credentials.

	```
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1
	country=US

	network={
		ssid="SSID"
		psk="PASS"
		key_mgmt=WPA-PSK
	}
	```

1. To enable SSH (default is not enabled) create an empty file `ssh.txt` in same directory.
1. Boot your RasberryPi.
1. After a minute or so the image should boot and gain access to your provided network SSID.

### Connect to your Raspberry Pi
Replace the IP shown with your own modules IP. Checking your router for attached devices might expedite the processes.

```
ssh pi@192.168.1.55
pi@192.168.1.55's password:
```


##### Setup Project Requirements

Install requirements.

```
sudo apt-get update
sudo apt-get install python3-flask mosquitto
sudo pip install virtualenv paho-mqtt
```

##### Setup GitHub Access
Get a public key, add to GitHub, and clone the repo.

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
cat /home/pi/.ssh/id_rsa.pub
cd
cd mkdir Projects
cd Projects
git clone git@github.com:justinwagg/raspi-light-server.git
```
##### Setup Virtualenv

```
cd raspi-light-server
virtualenv venv
venv/bin/pip install -r requirements.txt
```

##### Build settings database

I used MySQL, but you're welcome to BYOD. You'll need to setup a local instance, and create some tables. You'll find table create statements in the `setup/table_create.sql`


##### Running

Run `venv/bin/python app`

If successful, setup a cronjob to launch the server on boot.

```
sudo crontab -e
@reboot sh /path/to/folder/launcher.sh > /path/to/folder/cronlog 2>&1
```

### Notes:
#### Localization

Remember to change the localization settings of your Raspberry Pi
`sudo raspi-config`

### To Do
- Add logging
- Add code to relaunch if crash
