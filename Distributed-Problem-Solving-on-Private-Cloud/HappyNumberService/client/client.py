import time
import primer
import Pyro4

def processMessage(msg):
	# print msg
	L, R = map(int, msg.split())
	numPrimes = primer.NumHappyPrimes(L, R)
	Q.sendToQueue('qresult', str(numPrimes))

def listen():
	while True:
		msg = Q.fetchMessage('qinfo')
		if len(msg) == 0:
			print "Queue is empty"
			time.sleep(3)
		else:
			try:
				print "Message Received: { %s } from Queue: { %s }" %(msg, 'qinfo')
				processMessage(msg)
			except:
				print("Invalid Message: { %s } in Info Queue" %(msg))

if __name__ == '__main__':
	Q = Pyro4.Proxy("PYRONAME:service.msg")
	# Q.fetchMessage('qinfo')
	listen()

