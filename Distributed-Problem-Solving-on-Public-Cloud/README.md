# Distributed Problem On Public Cloud

**Objective :**  Test and benchmark any compute intensive application on any public cloud platform like
AWS, GAE or Azure.

**Problem Statement :**  Given an integer range, L to R ( inclusive of L and R ) find the no. of [Happy](https://en.wikipedia.org/wiki/Happy_number) [Prime Numbers](https://en.wikipedia.org/wiki/Prime_number) in that range.


## Requirements/Setup

### Instances created
- 2 instances of SQS &  
- Multiple instances of Amazon EC2 service
are used.

### Software requirements  
Each EC2 instance (Ubuntu Server 16.04 LTS) is installed with the following :  
- aws-cli  
- python 2.7  
- AWS sdk for python - boto3

For further details, refer [report](Distributed-Problem-Solving-on-Public-Cloud//Cloud%20Computing%20Report.pdf).

## Execution

On master, execute:

`1. python master.py`

On clients, execute:  

`1.	python slave.py`  

## Contibutors

- [Abhishek Jaisingh](https://github.com/abhishekjiitr)
- [Ambar Zaidi](https://github.com/AmbarZaidi)
