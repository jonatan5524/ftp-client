from cmd import Cmd
import ftplib

class ftpShell(Cmd):
    def __init__(self,ftp):
        Cmd.__init__(self)
        self.ftp = ftp

    def do_exit(self, inp):
        '''exit - disconnecting from the ftp server.'''
        print("Bye")
        self.ftp.close()
        return True

    def do_cd(self, inp):
        '''cd PATH - move to a different working directory'''
        try:
            print(self.ftp.cwd(inp))
        except ftplib.error_perm as err:
            print(err)
    
    def do_ls(self, inp):
        '''ls - list the current working directory contents'''
        print(self.ftp.retrlines('LIST') )

    def do_pwd(self, inp):
        '''pwd - return the current working directory path'''
        print(self.ftp.pwd()) 
    
    def do_cp(self, inp):
        '''cp FILE_NAME - transfer file FILE_NAME'''
        try:
            with open(inp,'wb') as fp:
                print(self.ftp.retrbinary('RETR '+inp, fp.write))
        except ftplib.error_perm as err:
            print(err)
        except FileNotFoundError:
            print('file not found')

    def do_mv(self, inp):
        '''mv FROM_NAME TO_NAME - rename file FROM_NAME on the server to TO_NAME'''
        try:
            old,new = inp.split()
            print(self.ftp.rename(old,new))
        except ftplib.error_perm as err:
            print(err)
        except ValueError:
            print('unexpected number of parameters - 2 parameters require')

    def do_rm(self, inp):
        '''rm FILE_NAME - remove file FILE_NAME from the server'''
        try:
            print(self.ftp.delete(inp))
        except ftplib.error_perm as err:
            print(err)
    
    def do_rmdir(self, inp):
        '''rmdir FOLDER_NAME - remove file FOLDER_NAME from the server'''
        try:
            print(self.ftp.rmd(inp))
        except ftplib.error_perm as err:
            print(err)
    
    def do_mkdir(self, inp):
        '''mkdir DIR_NAME - create a new directory on the server'''
        try:
            print(self.ftp.mkd(inp))
        except ftplib.error_perm as err:
            print(err)
    
    def do_size(self, inp):
        '''size FILE_NAME - return the file size of FILE_NAME'''
        try:
            print(self.ftp.size(inp))
        except ftplib.error_perm as err:
            print(err)

    def do_cat(self, inp):
        '''cat FILE_NAME - return the file FILE_NAME content'''
        try:
            self.ftp.retrbinary('RETR '+inp, lambda data: print(data.decode("utf-8")))
        except ftplib.error_perm as err:
            print(err)
        except FileNotFoundError:
            print('file not found')