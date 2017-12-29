import requests
import json



def zabbix_login( url,username,password ):
	header = {'Content-Type' : 'application/json-rpc'}

	zabbix_json = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": username,
        "password": password,
            },
    "id": 1
	}
	value = json.dumps(zabbix_json)

	server = requests.request('POST',url,headers=header,data = value)
	msg = server.text
	msg = json.loads(msg)

	token = msg['result']

	return token

def zabbix_get_groupid(url,groupname,token):
	header = {"Content-Type": "application/json-rpc"}
	data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": groupname
        }
    },
    "auth": token,
    "id": 1
	}
	value = json.dumps(data)
	server = requests.request('POST', url, headers=header, data=value)
	msg = server.text
	print(msg)
	#读取访问回来的数据,类型为‘str’
	msg = json.loads(msg)
	#将‘str’类型转换为dict类型
	id = msg['result'][0]['groupid']
	return id

def host_create (vm_name,vm_ip,url,token):
	header = {'Content-Type': 'application/json-rpc'}

	zabbix_json = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
	    "name": vm_name,
        "host": vm_ip, 
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": vm_ip,
	            "dns": "",
                "port": "10050" 
            }
        ],
        "groups": [
            {
                "groupid": "XXXXXXX" 
            }
        ],
        "inventory_mode": -1,  #1是自动清单描述，0是手动清单描述，-1是关闭清单描述
    },
    "auth": token,
    "id": 1
	}

	value = json.dumps(zabbix_json)

	server = requests.request('POST',url,headers=header,data=value)
	msg = server.text




