#!/usr/bin/env python
#coding:utf-8

from ctypes import *
import os
import sys
import ftplib
import time

today = time.strftime('%Y%m%d',time.localtime(time.time()))
ip = '192.168.100.16'
username = 'jiangsu' 
password = 'asdfghj1234567assaddsac'
filename = '22222211111'+ today + '.tar.gz'
src_file = '/data/'+filename

class myFtp:
    ftp = ftplib.FTP()
    ftp.set_pasv(False) 
    def __init__(self, host, port=21):
        self.ftp.connect(host, port)
 
    def Login(self, user, passwd):
        self.ftp.login(user, passwd)
        print(self.ftp.welcome)
 
    def DownLoadFile(self, LocalFile, RemoteFile):  
        file_handler = open(LocalFile, 'wb')
        print(file_handler)
        # self.ftp.retrbinary("RETR %s" % (RemoteFile), file_handler.write)#接收服务器上文件并写入本地文件
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        return True

    def DownLoadFileTree(self, LocalDir, RemoteDir): 
        print("remoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        self.ftp.cwd(RemoteDir)
        RemoteNames = self.ftp.nlst()
        print("RemoteNames", RemoteNames)
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)
            print(self.ftp.nlst(file))
            if file.find(".") == -1:
                if not os.path.exists(Local):
                    os.makedirs(Local)
                self.DownLoadFileTree(Local, file)
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")
        return True
 
    def close(self):
        self.ftp.quit()
 
 
if __name__ == "__main__":
    ftp = myFtp(ip)
    ftp.Login(username, password)
    ftp.DownLoadFile(filename,src_file )
#    ftp.DownLoadFileTree('.', '/data/')

    ftp.close()
    print("ok!")
