import xlrd
import re
from zabbix_api.zabbix_def import *

zabbix_address = 'http://XXXXX/zabbix/api_jsonrpc.php'
zabbix_username = 'XXXXX'
zabbix_password = 'XXXXX'

xlsx = xlrd.open_workbook('F:\\script\\zabbix\\from_xlsx_add_host\\vm_list.xlsx')

sheet = xlsx.sheets()[0]

token = zabbix_login( zabbix_address,zabbix_username,zabbix_password )


for row_id in range(1,sheet.nrows):

    host_name = sheet.cell(row_id,0).value

    ip  = sheet.cell(row_id,1).value

    reg = '[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*'
    reg = re.compile(reg)

    ############################################## 这个判断有逻辑问题
    if type(re.findall(reg,ip)) != type(None):   # 但是已经懒得改了
        host_ip = re.findall(reg,ip)[0]          # 勉强还能用
    ##############################################

    host_create(host_name,host_ip,zabbix_address,token)















