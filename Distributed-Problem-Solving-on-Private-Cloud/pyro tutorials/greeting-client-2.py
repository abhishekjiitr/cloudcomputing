# saved as greeting-client.py
import Pyro4

name = input("What is your name? ").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:example.greeting")    # use name server object lookup uri shortcut
print(greeting_maker.get_fortune(name))
greeting_maker.set_fortune(1111)
print(greeting_maker.get_fortune(name))