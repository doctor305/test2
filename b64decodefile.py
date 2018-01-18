import base64

with open('log.txt','r') as f:
    output = open('output.txt','w')
    output.write(base64.decode(f.read()))
