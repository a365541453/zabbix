import requests
import json


def zabbix_login(url, username, password):
	header = {"Content-Type": "application/json-rpc"}

	#################################
	data = {                        #这是zabbix规定的
    "jsonrpc": "2.0",               #API接口样式
    "method": "user.login",         #
    "params": {                     #
        "user": username,           #
        "password": password        #
    },                              #
    "id": 1                         #
	}                               #
	#################################
	value = json.dumps(data)
	#dumps是将dict转化成str格式
	server = requests.request('POST',url,headers=header,data=value)
	msg = server.text
	#读取访问回来的数据,类型为‘str’
	msg = json.loads(msg)
	#将‘str’类型转换为dict类型
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
	#读取访问回来的数据,类型为‘str’
	msg = json.loads(msg)
	#将‘str’类型转换为dict类型
	id = msg['result'][0]['groupid']
	return id


def create_group(url,group_name,token):
	header = { 'Content-Type': 'application/json-rpc' }

	data = {
    "jsonrpc": "2.0",
    "method": "hostgroup.create",
    "params": {
        "name": group_name
    },
    "auth": token,
    "id": 1
	}

	value = json.dumps(data)
	server = requests.request('post',url,headers=header,data=value)
	msg = json.loads(server.text)
	groupid = msg['result']['groupids'][0]
	return groupid







