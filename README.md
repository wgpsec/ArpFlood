# ArpFlood
Python Arpspoof For Multiple Targets,
This is a Tool made by AdianGg,
It is easy to use,just according to the instructions, there are guidelines for each step

一个基于python3的小工具，可以简单实现多线程多目标的Arp欺骗，在kali linux中自带的arpspoof一次只可以欺骗单个目标，而在实际应用中，我们经常需要欺骗整个网段的所有存活主机，所以做了这个脚本
# 所调用的库：
 - re:python自带的标准库
 - time:python自带的标准库
 - threading:python自带的标准库
 - scapy.all:第三方库，需要自行pip install
# 已经实现的功能
 - 输入多个IP，每个IP分配一个线程发伪造的Arp包
 - 验证输入内容是否合法（匹配正则）
 
**预计改进内容**
 - 增加恢复功能（头疼，忘了加这个功能了）
 - 扫描所在网段的存活主机并支持导入到TargetList
 - 能对TargetList进行删除
# 平台
Windows with python3

Linux with python3

Thank you for using!!!!!!!!!!!!
# 界面
![微信图片_20200125115051.png][2]
# About
wgpsec:http://www.wgpsec.org

myblog:http://www.e-wolf.top


  [2]: http://www.e-wolf.top/usr/uploads/2020/01/3030503727.png
