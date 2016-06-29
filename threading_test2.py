import threading
import time

def test(n):
    print n
    time.sleep(0.1)
    
print "Start!"

for n in range(5):
    t = threading.Thread(target=test,args = n)

    t.start()
    t.join()

print "End! "  
