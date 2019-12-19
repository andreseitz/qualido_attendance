#! /bin/bash

wget https://barcodetopc.com/download/linux -O /usr/bin/barcode_host.AppImage
sudo chmod 777 /usr/bin/barcode_host.AppImage
sudo apt install ufw -y
sudo ufw enable
sudo ufw allow 57891/tcp
sudo ufw allow 5353/udp

cp startup_host.sh /etc/profile.d/
