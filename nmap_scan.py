#!/usr/bin/env python
import sys
import nmap
#scan_row=[]
hosts = input('请输入要扫描的IP,如192.168.1.0/24，192.168.1.0-10: ')
ports = input('请输入要扫描的端口，如80，22，443，1000-1500：')
#scan_row = input_data.split(' ')
#if len(scan_row)!=2:
#    print("Input error,example \"192.168.1.10/24 80,443,22\""can_row=[]
#    sys.exita(0)
#hosts = scan_row[0] 
#ports = scan_row[1]
try:         
    nm =nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found',sys.exc_info()[0])
    sys,exit(0)
except:
    print('Unexpected error',sys.exc_info()[0])
    sys.exit(0)
try:
    nm.scan(hosts=hosts,arguments = '-v -sS -p '+ports)
except Exception as e:
    print('scan error:'+str(e))
for host in nm.all_hosts():
    print('------------------------------------')
    print('Host: %s(%s)'%(host,nm[host].hostname()))
    print('State: %s' %nm[host].state())
    for proto in nm[host].all_protocols():
        print('-------------')                                                                  
        print('Protocol: %s' %proto)    
        lport =list(nm[host][proto].keys())                                         
        lport.sort()                                                      
        for port in lport:
            print('port: %s\tstate: %s' %(port,nm[host][proto][port]['state']))
