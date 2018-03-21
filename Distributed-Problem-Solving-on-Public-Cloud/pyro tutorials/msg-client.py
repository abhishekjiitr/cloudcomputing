# saved as msg-client.py
import Pyro4

# name = input("What is your msg? ").strip()

Q = Pyro4.Proxy("PYRONAME:example.msg")    # use name server object lookup uri shortcut
Q.sendToQueue("qresult","test msg 2 qinfo !")
print("ppp:::",Q.fetchMessage('qinfo'))
# SQS.set_fortune(1111)
# print(SQS.get_fortune(name))