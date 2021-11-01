# Domain-monitor

Script that check if domains are available.

## How to begin 

You need to create two config-files in the script root folder. 

### config.py

```
mail_host = "mail.host.com"
mail_port = 465
mail_username = "username"
mail_password = "password
```

### domains.yaml

Email: Mail address to receive notification if one or more domains are available

Domains: List of domains to check if available

```
Email: alert@me.com
Domains: 
  - domain1.com
  - domain2.com
  - domain3.net
```

## Dependencies

The script require that you have Chromedriver installed.

### Windows

[How to install Chromedriver on Windows 10 - YouTube](https://www.youtube.com/watch?v=dz59GsdvUF8)

### Linux Server

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb
google-chrome --version

Donaload latest version of Chromedriver: https://sites.google.com/chromium.org/driver/downloads
wget last-version-of-chromedriver-for-Linux-Server.zip
unzip last-version-of-chromedriver-for-Linux-Server.zip
rm last-version-of-chromedriver-for-Linux-Server.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```