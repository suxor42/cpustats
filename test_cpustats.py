import cpustats
import time
import functools
import math

def test_percentage():
	stat1 = cpustats.getstats()
	time.sleep(0.250)
	stat2 = cpustats.getstats()
	difference = cpustats.diff(stat1,stat2)
	percentage = {}
	for cpu,stats in difference.items():
		percentage[cpu] = cpustats.calcratio(stats)

	for cpu,stats in percentage.items():
		yield check_percentage, sum(stats.values())

def check_percentage(percentage):
	assert percentage == 100
