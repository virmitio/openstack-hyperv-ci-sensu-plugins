#! /bin/python
import yaml
import os
import getopt

if os.name == 'nt':
    summaryPath = 'C:/ProgramData/PuppetLabs/puppet/var/state/last_run_summary.yaml'
else:
    summaryPath = '/var/lib/puppet/state/last_run_summary.yaml'

maxage = 0

opts, args = getopt.getopt(sys.argv[1:], "t:f:", ["time=",file="])
except getopt.GetoptError:
    print "Incorrect usage.
  {0} [-t|--time SECONDS] [-f|--file FILENAME]".format(sys.argv[0])
    exit(3)

for opt, arg in opts:
    if opt in ("-t", "--time"):
        maxage = arg
    elif opt in ("-f", "--file"):
        summaryPath = arg

age = time.time()-os.path.getmtime(summaryPath)
if maxage > 0 and age > maxage:
    exit(1)

summary = open(summaryPath)
data = yaml.safe_load(summary)
summary.close()

if data["events"]["failure"] > 0:
    with open(summaryPath) as summary:
        for line in summary:
            print(line)
    exit(2)
else:
    exit(0)

