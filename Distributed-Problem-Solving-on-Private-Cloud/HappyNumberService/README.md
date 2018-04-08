# Distributed Problem On Private Cloud

**Objective :**  Test and benchmark any compute intensive application on private cloud using OpenNebula or OpenStack.  

**Problem Statement :**  Given an integer range, L to R ( inclusive of L and R ) find the no. of [Happy](https://en.wikipedia.org/wiki/Happy_number) [Prime Numbers](https://en.wikipedia.org/wiki/Prime_number) in that range.


## Requirements

**Dependencies**  
- python 2.7


**Libraries**
- Pyro4

## Execution

On master, in separate terminals,  
Execute:


`1.  python -m Pyro4.naming`  
`2.	python msg_service/msg_server.py`  
`3.	python server/master.py`



On clients,  
Execute:  

`1.	python client.py `  

## Contibutors

- [Abhishek Jaisingh](https://github.com/abhishekjiitr)
- [Ambar Zaidi](https://github.com/AmbarZaidi)

# TODO
- deploy this on OpenNebula based VMs on a local network
