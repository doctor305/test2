import win32com.client
import time
import urlparse

clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'  ## IE
url_list = {}

windows = win32com.client.Dispatch(clsid)
n = 0
while n < 5:
    temp_list = []
    for browser in windows:
        url = urlparse.urlparse(browser.LocationUrl)
        temp_list.append(url.hostname)
    url_list[time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())] = temp_list
    time.sleep(5)
    n += 1

f = open('url.txt','w')
for key in url_list.keys():
    f.write(key + '  ' + str(url_list[key]) + '\n')
    

f.close()        
