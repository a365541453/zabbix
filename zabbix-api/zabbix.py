from def_file.zabbix_def import *

url = 'http://192.168.147.138/zabbix/api_jsonrpc.php'
username = 'Admin'
password = 'zabbix'
groupname = 'Zabbix servers'
group_list = ['192.168.147.193',
              '192.168.147.194',
              '192.168.147.195',
              '192.168.147.196',
              '192.168.147.192']

token = zabbix_login(url,username,password)

group_id = zabbix_get_groupid(url,groupname,token)


for name in group_list:
	groupid = create_group(url,name,token)
	print(groupid)

