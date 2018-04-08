import boto3, json

def sendToQueue(queueName='qinfo', message='test message'):	
	sqs = boto3.resource('sqs')
	# Get URL for SQS queue
	queue = sqs.get_queue_by_name(QueueName=queueName)
	# print queue.url
	response = queue.send_message(MessageBody=message)
	print("Message Sent: { %s } to Queue: { %s }"%(message, queueName))
	# parsed = json.loads(json.dumps(response))
	# print json.dumps(parsed, indent=4, sort_keys=True)

if __name__ == '__main__':
	sendToQueue('qinfo', '1 100')