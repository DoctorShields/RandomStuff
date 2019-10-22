# RandomStuff

## Table of Contents
* [Git](#Git)
* [Pi](#Pi)

## Git
### That annoying LF/CRLF warning
`git config core.autocrlf false`

or

`git config --global core.autocrlf false`

### Making pretty trees
```
git config --global alias.lgb "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset%n' --abbrev-commit --date=relative --branches"

git lgb
```
### Cool tool:
https://nic-hartley.github.io/git-gud/

## Pi
### Hop on a non-broadcasting SSID
`sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

then

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US
 
network={
        ssid="insert_your_hidden_SSID_here"
        scan_ssid=1
        key_mgmt=NONE
}
```
