def distributeQuery(qu, L, R, VMs=4):
	qrange = R-L+1
	load = qrange // VMs
	for vm in range(VMs):
		i = L + load * vm
		j = L + load * (vm+1) - 1
		if vm == VMs-1:
			j = R
		# generateQuery(i, j)
		qu.append((i, j))
		print("Query: " + str(i)+", " + str(j))
