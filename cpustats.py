import re
import string
import functools
import math
import decimal
decimal.getcontext().prec = 10

def diff(stats1,stats2):
	result = {}
	for cpu,stats in stats1.items():
		difference = {}
		for key,value in stats.items():
			difference[key] = stats2[cpu][key] - value
		result[cpu]=difference
	return result

def calcratio(statitems):
	result = {}
	basevalue = sum(statitems.values())
	for key,value in statitems.items():
		result[key] = (decimal.Decimal(value*100) / decimal.Decimal(basevalue)).quantize(decimal.Decimal('.01'))
		#result[key] = result[key].quantize(decimal.Decimal('.01'))
	return result

def getstats():
	with open("/proc/stat",'r') as statfile:
		content = statfile.read()
		data = re.findall("cpu[0-3].*|cpu.*",content)
		structured = {}
		for item in data:
			structureditem = {}
			values = str.split(str.replace(item,'  ', ' '),' ')
			structureditem['user'] = int(values[1])
			structureditem['nice'] = int(values[2])
			structureditem['system'] = int(values[3])
			structureditem['idle'] = int(values[4])
			structureditem['iowait'] = int(values[5])
			structureditem['irq'] = int(values[6])
			structureditem['softirq'] = int(values[7])
			structured[values[0]] = structureditem
	return structured
