import Pyro4

# To implement:
# 	0. initQueue(qname)
# 	1. sendToQueue(qname,msg)
# 	2. fetchMessage(qname)

@Pyro4.expose
class SQS(object):
	qlist = dict()
	def initQueue(self,qname):
		SQS.qlist[qname]=[]
		print "==> Initiated queue with name \"",qname,"\""
	def sendToQueue(self,qname,msg):
		try:
			SQS.qlist[qname].append(msg)
		except:
			print ">> ERROR in sendToQueue() ! : No queue with name \"",qname,"\" found"
	def fetchMessage(self,qname):
		try:
			q = SQS.qlist[qname]
		except:
			print ">>> ERROR in fetchMessage() ! : No queue with name \"",qname,"\" found"
			return None
		msg = ""
		if len(SQS.qlist[qname])>0:
			msg = SQS.qlist[qname].pop(0)
			print "Message Relayed: { %s } from Queue: { %s }" %(msg, qname)
			return msg
		# print "None"
		return msg

Q = SQS()
Q.initQueue("qinfo")
Q.initQueue("qresult")
# Q.sendToQueue("qino","test msg 2 qinfo !")
Q.sendToQueue("qinfo","test msg 2 qinfo !")
Q.sendToQueue("qresult","test msg 2 qresult !")
Q.fetchMessage("qinfo")
Q.fetchMessage("qresult")

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Q)   # register the greeting maker as a Pyro object
ns.register("service.msg", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls