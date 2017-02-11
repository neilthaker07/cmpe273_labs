import psutil
myProcesses = psutil.net_connections(kind='tcp')
fdList = []
pidDataList = []

for process in myProcesses:
	fdList.append(process[-7])
	pidDataList.append(str(process[-1]).strip('[]')+ "," + str(process[-4]).strip('[]')+ ","
					  + str(process[-3]).strip('[]')+"," + str(process[-2]).strip('[]'))

outputList = {}
for i in range(len(myProcesses)):
		outputList[fdList[i]] = pidDataList[i]

counterStorage = {}
for i in range(len(myProcesses)):
	if pidDataList[i].split(',', 1)[0] in counterStorage:
		counterStorage[pidDataList[i].split(',', 1)[0]] = (counterStorage.get(pidDataList[i].split(',', 1)[0]) + 1)
	else:
		counterStorage[pidDataList[i].split(',', 1)[0]] = 1

import operator
sortedList = sorted(counterStorage.items(), key=operator.itemgetter(1), reverse=True)

print '"pid","laddr","raddr","status"'
for k,v in sortedList:
	for j in range(len(myProcesses)):
		if k == pidDataList[j].split(',', 1)[0] :
			finalResult = '"'+str(pidDataList[j]).split(',', 1)[0]+'"' + ',' +  '"'+str(pidDataList[j]).split(',', 1)[1]+'"'
			finalResult = finalResult.replace("),", ",")
			finalResult = finalResult.replace(", ","@")
			finalResult = finalResult.replace("(","")
			finalResult = finalResult.replace("'","")
			finalResult = finalResult.replace(",",'",')
			finalResult = finalResult.replace('",','","')
			finalResult = finalResult.replace('"",""','","')
			print(finalResult)

