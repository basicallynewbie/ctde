# For ssh no password login:

In CT:

    sed -i 's/#PubkeyAuthentication/PubkeyAuthentication/g' /etc/ssh/sshd_config 
        
    echo -e "TCPKeepAlive yes\nClientAliveInterval 300\nClientAliveCountMax 2" > /etc/ssh/sshd_config 
        
In host:

    ssh-keygen 
        
    ssh-copy-id -i <private key> containerUser@containerIp
        
Add this in ~/.ssh/config to login CT without password:

    Host <ip>
        
      IdentityFile /home/userName/.ssh/<private key>

# For ctde.py:

  Change Start('the path to your compositor', 'cmd of your container manager only support "lxc" for LXD and "incus" for Incus', 'name of the container', 'username in container', 'ip of container')() in if \__name__ == '\__main__' to fit you.

# For ctde.desktop:

  Change /path/to/ctde.py to the real path of ctde.py.

# detail
https://discuss.linuxcontainers.org/t/autostart-container-desktop-environment/
