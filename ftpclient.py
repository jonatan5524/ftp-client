import ftplib
import argparse
from ftpshell import ftpShell

parser = argparse.ArgumentParser()
parser.add_argument('host',help='host name or ip address of the ftp server')
parser.add_argument('-p','--port',help='port number to onnect to, defualt port nubmer: 21',default=21,type=int)
parser.add_argument('-u','--username',help='username to the ftp server, defualt username: anonymous',default='anonymous')
parser.add_argument('--password','--pass',help='password to the ftp server, defualt username: anonymous',default='anonymous')
args = parser.parse_args()

class ftpClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.password = password
        self.username = username
        self.port = port
        self.ftp = ftplib.FTP()
        self.shell = ftpShell(self.ftp)
    
    def connect(self):
        try:
            print(f'connecting to {self.host} : {self.port}\nusername and password {self.username} : {self.password}')
            self.ftp.connect(host= self.host, port = self.port)
            self.ftp.login(user = self.username, passwd = self.password)
            print('login successful')
            print(self.ftp.getwelcome())
        except ConnectionRefusedError:
            print('connection to host refused, check if the server is up')
        except TimeoutError:
            print('timeout Error check if the ftp server is up')
        except ftplib.error_perm as err:
            print(err)

    def start_shell(self):
        self.shell.prompt = 'FTP>>'
        self.shell.cmdloop('Starting prompt...')
   
    def close(self):
        self.ftp.quit()

if __name__ == "__main__":
    client = ftpClient(args.host, args.port, args.username, args.password)
    client.connect()
    client.start_shell()