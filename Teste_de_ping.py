#!/usr/bin/python3
import subprocess, re, os, statistics
print('Pingando...')
if os.sys.platform == 'win32':
    result = subprocess.check_output("ping v.vrv.co", shell=True).decode()
else:
    result = subprocess.check_output("ping -c5 v.vrv.co", shell=True).decode()
pings = re.findall("time?[=,<].*?ms", result)
for i in range(len(pings)):
	pings[i] = re.sub("time?[=,<]", "", pings[i])
	if os.sys.platform == 'win32':
		pings[i] = re.sub("ms", "", pings[i])
	else:
		pings[i] = re.sub(" ms", "", pings[i])
	pings[i] = float(pings[i])
print('O seu ping médio é', statistics.mean(pings), "ms.")
