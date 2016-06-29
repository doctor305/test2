import threading
import time

def test():
    print "The curent threading %s is running. " % threading.current_thread().name
    time.sleep(0.1)
    print "The curent threading %s is ended." % threading.current_thread().name

print "The curent threading %s is running." % threading.current_thread().name

t = threading.Thread(target=test)

t.start()
time.sleep(0.1)
t.join()

print "The curent threading %s is ended."  % threading.current_thread().name
