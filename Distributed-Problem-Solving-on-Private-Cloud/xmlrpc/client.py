import xmlrpc.client
import time, primer

server_ip = '172.25.15.143'
s = xmlrpc.client.ServerProxy('http://'+server_ip+':8000')

while True:
    L, R = s.query()
    if L != -1 and R != -1:
        print(L, R)
        answer = primer.NumHappyPrimes(L, R)
        # print("NICE"+str(answer))
        # if answer:
        s.compile_result(answer)
    else:
        time.sleep(5) 