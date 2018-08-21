#安装serial easygui for python3
import serial
import sys
import os
import time
import re
 

def testZiJieXuLie():
    # 将16进制字符串 转换为 字节数组
    resDemo2 = "4101012412c116a1"
    #a116c11224010141

    #利用内置bytes方法，将字符串转换为指定编码的bytes

    print("利用内置bytes方法，将字符串转换为指定编码的bytes")
    b = bytes(resDemo2,encoding='ASCII') 
    """将16进制字符串 转为字节数组  encoding 指明要 ASCII 其他 有问题呀""" 
    print(b)
    print(b[0])
    listStrByte =[]
    listValByte =[]
    for i in range(len(resDemo2)//2,0,-1):
        print(i)
    #切片去处字符串前两个字符序列 输出转换后的16进制
        val = int(resDemo2[(2*(i-1)):(2*i)],16)
        print(val)
        print(hex(val))
        listStrByte.append(hex(val))
        listValByte.append(val)

    print(listStrByte)
    print(listValByte)

    b = bytes(listValByte)
    print(b)
    print(b[0])
    print(b[4])
    print(b[5])
    print(b[6])
    print(b[7])


    v = (b[7]<<16)|(b[6]<<8)|b[5]
    print(v)
    print(bin(v))
    print("智云标志:{0}".format(hex((b[7]<<16)|(b[6]<<8)|b[5])))
    brandType = (b[4]>>4)&0x0F
    print(brandType)
    print(bin(brandType))
    print("产品类型:{0}".format((b[4]>>4)&0x0F))
    pindianType = (b[4])&0x0F
    print(pindianType)
    print(bin(pindianType))
    print("频点类型:{0}".format((b[4])&0x0F))
    outStyle = (b[3]>>7)&0x01
    print(outStyle)
    print(bin((b[3]>>7)&0x01))
    print("OUIStyle:{0}".format((b[3]>>7)&0x01))
    year = (b[3])&0x7F
    print(year)
    print(bin(year))
    print("生产年份余数:{0}".format(year))
    month = (b[2]>>4)&0x0F
    print(month)
    print(bin(month))
    print("生产月份:{0}".format(month))
    day = ((b[1]>>7&0x01)<<4)|(b[2]&0x0F)
    print(day)
    print(bin(day))
    print("生产日期的天:{0}".format(day))
    sn = ((b[1]&0x7F)<<8)|(b[0]&0xFF)

    print(sn)
    print(bin(sn))
    print("产品SN号:{0}".format(sn))

    print("字节数组 转为大整型")
    bigInt = int.from_bytes(b, byteorder='big', signed=False)

    print(hex(bigInt))

    print(bin(bigInt))


'''
命令字指令字节定义了报文的不同功能，该指令长度为 1 个字节。
bit7 指令定义了报文的源头，如果 bit7==0 意味着该报文来自模块，否则如果
bit7==1 意味着该报文来自控制端。
bit6 指令定义了模块的操作模式，如果 bit6==0 意味着主控想要获取模块的数
据，否则如果 bit6==1 意味着控制端想要把数据写入模块的寄存器。
bit5 指令定义了回复的状态，如果 bit5==1 意味着指令已经执行成功，
否则如 果 bit5==0 意味着模块执行指令失败。

'''
#如果bit7==1 意味着该报文来自控制端
#11000000 0xc0 如果 bit6==1 意味着控制端想要把数据写入模块的寄存器
#10000000 0x80 如果 bit6==0 意味着主控想要获取模块的数据
#01000000 0x40 如果 bit7==0 意味着该报文来自模块
#来自模块，bit7=0，bit6=1
#来自主控，bit7=1，bit6=0
#0xC0
#x | (1 << (k-1))   把右数第k位变成1   101001->101101,k=3
#x & ~ (1 << (k-1))  把右数第k位变成0   101101->101001,k=3
print("将数据的指定位置为1")
val = 8
k=3
print(bin(val))
val = val|(1<<(k-1))
print(bin(val))
print(val)

data = []
qiandao = 0xFF
startFlag = 0xFF 
command = 0xFF
length  = 0x00
content = "1234abcd"
crcdata = 0x00
endFlag = 0x40
'''
字符串与bytes 
字符串是由字符组成的有序序列，字符可以使用编码来理解
bytes是字节组成的有序的不可变序列
bytearray是字节组成的有序的可变序列
'''
#现实生活中都是 大端字节序
def baowen(qiandao,startFlag,command,length,content,crcdata,endFlag):
    print("报文")
    dataValByte = bytearray()
    dataValByte.append(qiandao)
    dataValByte.append(startFlag)
    dataValByte.append(command)
    #字符串通过encode()方法就可以转化为字节 默认是'ASCII'
    contentCode = content.encode()
    print(contentCode)
    conA = bytearray(contentCode)
    print(type(conA))
    print(conA)
    print(dataValByte)
    #字节序列拼接
    dataValByte.extend(contentCode)
    print(dataValByte)
    dataValByte.append(length)
 
    dataValByte.append(crcdata)
    dataValByte.append(endFlag)

    print(dataValByte)
    b = bytes(dataValByte)

    '''
    这里字节（单个字符）数组 ，字节序列 与16进制序列对应
    b'\xff\xff\xff1234abcd\x00\x00@'
    字节数组 转为大整型
    0xffffff3132333461626364000040
    '''
    print(b)
    print("字节数组 转为大整型")
    bigInt = int.from_bytes(b, byteorder='big', signed=False)
    print(hex(bigInt))

    return hex(bigInt)


def commandConfig():
    pass


def wait_for_cmd_OK():
    while True:
        line = ser.readline()
        try:
            print(line.decode('utf-8'),end='')
        except:
            pass
        if ( re.search(b'OK',line)):
            break

def sendAT_Cmd(serInstance,atCmdStr):
    serInstance.write(atCmdStr.encode('utf-8'))
    wait_for_cmd_OK()

debugT = False
#选择串口号及波特率，因为我是在ubuntu下使用，故串口号为/dev/ttyACM0
if debugT:
    ser = serial.Serial("/dev/tty.SLAB_USBtoUART",9600,timeout=30) 

testZiJieXuLie()

b = baowen(qiandao,startFlag,command,length,content,crcdata,endFlag)

print(type(b))

if debugT:
    sendAT_Cmd(ser,b)
    ser.close()

