import subprocess
import json

netstat = subprocess.run(["netstat", "-anutp"], stdout=subprocess.PIPE)

with open("output.txt","w") as output:
  output.write(netstat.stdout.decode('utf-8'))

data = []

# Read each line from file and store in data object
with open("output.txt","r") as input:
  # Skip 1st and 2nd line that contains header information
  next(input)
  next(input)
  for line in input:
    data.append(line.split())

# Read each element (netstat line entry) from the data list object containing the netstat results
with open("output.json","w") as json_file:
  for netstat_line in data:
    net_data = dict()
    for i in range(len(netstat_line)):
      # Protocol
      if i == 0:
        net_data.update({"proto": netstat_line[i]})
      # Local Address:Port 
      elif i == 3:
        addr_port = netstat_line[i].split(":")
        net_data.update({"local_address": addr_port[0]})
        net_data.update({"local_port": addr_port[1]})
      # Foreign Address:Port
      elif i == 4:
        addr_port = netstat_line[i].split(":")
        net_data.update({"remote_address": addr_port[0]})
        net_data.update({"remote_port": addr_port[1]})
      # State
      elif i == 5:
        net_data.update({"state": netstat_line[i]})
      # PID/Program Name
      elif i == 6:
        pid_prog = netstat_line[i].split("/")
        net_data.update({"pid": pid_prog[0]})
        net_data.update({"program_name": pid_prog[1]})
      else:
        continue
    json.dump(net_data, json_file)
