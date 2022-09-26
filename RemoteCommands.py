from classes.node import node
import json
import os
import copy


config = None
try:
 with open("mnodes.config.json") as f:
    config = json.loads(f.read())
except:
 print("Configuration file is missing")
 exit(1)

UpDateConfigFileWhenFinished = False

config_backUp = copy.deepcopy(config)



for datacenter in config:
    subnet = datacenter['subnet']

    nodes = datacenter['nodes']

    def ssh_connect(hostname):
        # for n in nodes:
        try:
            if datacenter['password']:
                newNode = node(hostname, datacenter['ssh_port'], datacenter['username'], password=datacenter['password'], timeout=1)
            elif datacenter['ssh_keyfile']:
                newNode = node(n['ip_address'], datacenter['ssh_port'], datacenter['username'],
                               password=os.getcwd() + "/" + datacenter['ssh_keyfile'])
            print("Connecting to Node: %s --> " % n['ip_address'], end='')
            if newNode.Connect():
                return newNode
            else:
                return None
        except:
            print("Connection to Node: %s Failed " % n['ip_address'])

    print("\Running remote commands on servers...\n")


    for n in nodes:
        # for i in range(254):
        #     connec_ip= str(subnet) + "." + str(i)
        #     print(connec_ip)
        # break
        n0de = ssh_connect(n['ip_address'])
        if n0de:
            cmd = 'parted /dev/mmcblk0 resizepart 2 yes 100% yes 2>/root/out'
            # cmd = "parted /dev/mmcblk0 print"
            print(n0de.ExecCommand("sh ver"), "\n")
            # print(n0de.ExecCommand("lsblk|grep mmcblk0p2|awk '{print $1 \" --> \" $4}'"))
            # print(n0de.ExecCommand("ps -ef | grep vmware-|awk '{print $8}'"))
            # print(n0de.ExecCommand("%s " %cmd), "\n")
            # print(n0de.ExecCommand("lsblk"))
            # print(n0de.ExecCommand("cat ~/out"))
            break
        # break
