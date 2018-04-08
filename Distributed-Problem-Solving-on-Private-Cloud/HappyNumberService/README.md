# Distributed Problem On Private Cloud

## Requirements

### Dependencies
- python 2.7


### Libraries
- Pyro4

## Execution

On master, in separate terminals,   
Execute:
"""

0.  python -m Pyro4.naming
1.	python msg_service/msg_server.py
2.	python server/master.py

"""

On clients,
Execute:
"""

1.	python client.py  

"""

## Contibutors

- Abhishek Jaisingh
- Ambar Zaidi

# TODO
- deploy this on OpenNebula based VMs on a local network