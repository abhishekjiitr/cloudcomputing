import gen, time
import slave

def generateQuery(i, j):
	msg = str(i)+' '+str(j)
	print("Generating Query: %s"%(msg))
	gen.sendToQueue('qinfo', msg)

def compileResult(VMs):
	parts = 0
	ans = 0
	while parts < VMs:
		msg = str(slave.fetchMessage('qresult'))
		try:
			val = int(msg)
			ans += val
			parts += 1
			progress = 100*float(parts) / VMs
			print("%.2f %% Completed" % (progress))
		except:
			if len(msg) != 0:
				print("Invalid Result: { %s } in Queue qresult"%(msg))
	print("\nAnswer to Query: %d" % (ans))

def distributeQuery(L, R, VMs=4):
	start_time = time.time()
	qrange = R-L+1
	load = qrange / VMs
	for vm in range(VMs):
		i = L + load * vm
		j = L + load * (vm+1) - 1
		if vm == VMs-1:
			j = R
		generateQuery(i, j)
	compileResult(VMs)
	end_time = time.time()
	time_taken = end_time-start_time
	print("The computation took %d seconds" %(time_taken))

inp = raw_input("Algorithm to count happy prime numbers in a range\nEnter L and R to find happy prime numbers from L to R:\n")
L, R = map(int, inp.split())
distributeQuery	(L, R, 4)