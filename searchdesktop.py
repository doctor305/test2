import os
import os.path as path


userlist_unuse = ('All Users', 'Default', 'Default User','Public')
userlist = os.listdir('C:\Users')

for user in userlist:
    if user not in userlist_unuse and path.isdir('C:\Users'+os.sep+user):
        print user
        for filename in os.listdir('C:\Users'+os.sep+user+os.sep+'Desktop'):
            print filename
