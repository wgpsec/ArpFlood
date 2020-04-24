# ArpFlood
Python Arpspoof For Multiple Targets,
This is a Tool made by AdianGg,
It is easy to use,just according to the instructions, there are guidelines for each step

一个基于python3的小工具，可以简单实现多线程多目标的Arp欺骗，在kali linux中自带的arpspoof一次只可以欺骗单个目标，而在实际应用中，我们经常需要欺骗整个网段的所有存活主机，所以做了这个脚本，只有短短六十几行，主要目的也是想锻炼一下个人能力，毕竟在[Python-Socket通信简单实现][1]中提到过了，我是一个重度工具依赖患者，所以自己实现一下功能，顺便理解一下攻击原理。
# 所调用的库：
 - re:python自带的标准库
 - time:python自带的标准库
 - threading:python自带的标准库
 - scapy.all:第三方库，需要自行pip install
# 已经实现的功能
 - 输入多个IP，每个IP分配一个线程发伪造的Arp包
 - 验证输入内容是否合法（匹配正则）
 - 可以开启ip转发配合Driftnet等工具使用，都兼容
 
**预计改进内容**
 - 增加恢复功能（头疼，忘了加这个功能了）
 - 扫描所在网段的存活主机并支持导入到TargetList
 - 能对TargetList进行删除
# 平台
Windows with python3

Linux with python3

Thank you for using!!!!!!!!!!!!
# 界面
![ui.png][2]
# 被攻击目标情况
![xp.png][3]
# About
WgpSec狼组安全团队:http://www.wgpsec.org

AdianGg's Blog:http://www.e-wolf.top

  [1]: http://www.e-wolf.top/index.php/archives/113/
  [2]: http://www.e-wolf.top/usr/uploads/2020/01/3030503727.png
  [3]: http://www.e-wolf.top/usr/uploads/2020/01/3782156961.png
