import boto3, time
import gen, primer

def processMessage(msg):
	# print msg
	L, R = map(int, msg.split())
	numPrimes = primer.NumHappyPrimes(L, R)
	gen.sendToQueue('qresult', str(numPrimes))

def fetchMessage(queueName):
	sqs = boto3.resource('sqs')
	queue = sqs.get_queue_by_name(QueueName=queueName)
	client = boto3.client('sqs')

	# Get URL for SQS queue
	response = client.receive_message(
	    QueueUrl=queue.url,
	    MaxNumberOfMessages=1,
	)
	# print response
	try:
		messages = response['Messages']
		for msg in messages:
			body = msg['Body']
			print "Message Received: { %s } from Queue: { %s }" %(body, queueName)
			rhandle = msg['ReceiptHandle']
			del_response = client.delete_message(
			    QueueUrl=queue.url,
			    ReceiptHandle=rhandle
			)
			# print del_response
			return body
	except:
		return ""


def listen():
	while True:
		msg = fetchMessage('qinfo')
		if len(msg) == 0:
			print "Queue is empty"
			time.sleep(3)
		else:
			try:
				processMessage(msg)
			except:
				print("Invalid Message: { %s } in Info Queue" %(msg))


if __name__ == '__main__':
	fetchMessage('qinfo')
	listen()

