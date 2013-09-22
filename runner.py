import cpustats
import time

import graphite

BASEPATH = "angmar.stats"
graphite.connect()
while True:
	timestamp = int(time.time())
	stats = []
	stats.append(cpustats.getstats())
	#while time.time() <= timestamp + 1:
	time.sleep(0.250)
	stats.append(cpustats.getstats())
	result = cpustats.diff(stats[0],stats[1])
	percentages = {}
	for cpu,stats in result.items():
		percentages[cpu] = cpustats.calcratio(stats)
		if sum(percentages[cpu].values()) > 101 or sum(percentages[cpu].values()) < 99:
			print(percentages[cpu])


	for cpu,stats in percentages.items():
		#print(cpu,sum(stats.values()))
		for name,stat in stats.items():
			graphite.send_data(BASEPATH+".%s.%s"%(cpu,name),stat,timestamp)

graphite.close()
