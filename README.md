Installation

NOTE: you need to have previously install a grub theme for this to work, as the necessary file paths would not be there otherwise

1. Download the grub_randomizer.py file. it does not matter where this file is located but after this is set up its best not to move it.

2. Now you need to set it up as a service so that it will run on startup.
  first create the grub-randomizer.service file:
```
sudo touch /etc/systemd/system/grub-randomizer.service
```
3. Now copy this code into the grub-randomizer.service file and replace the file path to where you put the script. EX filepath: /home/USER/Downloads/grub_randomizer.py
  
  you can use this command to edit the grub-randomizer.service file
  ```
  sudo nano /etc/systemd/system/grub-randomizer.service
  ```
```
[Unit]
Description=randomize grub

[Service]
ExecStart=sudo python3 /FILE/PATH/TO/SCRIPT.py

[Install]
WantedBy=multi-user.target
```
4. now you need to enable the serive
  copy these commands and run them in the terminal
```
sudo systemctl enable grub-randomizer.service
```
```
sudo systemctl start grub-randomizer.service
```
  now reboot


Info

this script will work with any amount of grub themes without modifying the script. this script also will not choose the same grub theme 2 times in a row.


