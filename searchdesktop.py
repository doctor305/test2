import os
import os.path as path


userlist_unuse = ('All Users', 'Default', 'Default User','Public')
userlist = os.listdir('C:\Users')
fileformat = ('xls','xlsx','doc','docx','jpg','gif')

print 'os is : ',os.name
print userlist
for user in userlist:
    if user not in userlist_unuse and path.isdir('C:\Users'+os.sep+user):
        print 'user: ',user
        if  path.isdir('C:\Users'+os.sep+user+os.sep+'Desktop'):
            for filename in os.listdir('C:\Users'+os.sep+user+os.sep+'Desktop'):
                print filename
            
        print 'End'
