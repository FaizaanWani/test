def funct():
	f = open("/home/faizaan/Desktop/abc.txt")
	file_str = f.read().title()
	#print file_str
	# x = file_str.split(" ")
	# j = len(x)
	# print j
	# for i in range(1,j):
	# 	#print x[i]
	f.close()
	yield file_str

for f in funct():
	print "--------------This is text in tilte case---------------\n",f
