from def_file.zabbix_def import *

url = 'http://192.168.147.138/zabbix/api_jsonrpc.php'
username = 'Admin'
password = 'zabbix'
groupname = 'Zabbix servers'

token = zabbix_login(url,username,password)

group_id = zabbix_get_groupid(url,groupname,token)

print(group_id)
