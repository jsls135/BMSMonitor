# -*- coding: utf-8 -*-
from PCANBasic import *
#import threading
#from threading import RLock
import lookupTable
import time

newMsgBuf = []
PCANConnected=False

curMenu=1
curCscPage=0
DEBUG="NO"

if DEBUG=="YES":
	CAN_MSG_ID_CSC1_VOLT = 260
	CAN_MSG_ID_CSC2_VOLT = 260
	CAN_MSG_ID_CSC3_VOLT = 260
	CAN_MSG_ID_CSC1_TEMP = 260
	CAN_MSG_ID_CSC2_TEMP = 260
	CAN_MSG_ID_CSC3_TEMP = 260
	CAN_MSG_ID_BMS_STATE = 260
	CAN_MSG_ID_ISO_STATE = 260
	CAN_BUS_CLOCK = PCAN_BAUD_250K
else:
	CAN_MSG_ID_CSC1_VOLT = 256
	CAN_MSG_ID_CSC2_VOLT = 257
	CAN_MSG_ID_CSC3_VOLT = 258
	CAN_MSG_ID_CSC1_TEMP = 512
	CAN_MSG_ID_CSC2_TEMP = 513
	CAN_MSG_ID_CSC3_TEMP = 514
	CAN_MSG_ID_BMS_STATE = 0x6E
	CAN_MSG_ID_ISO_STATE = 0x8E
	CAN_BUS_CLOCK = PCAN_BAUD_500K

cscVolt = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
cscTemp = [
	[0,0,0,0],
	[0,0,0,0],
	[0,0,0,0]]
maxVolt=[0,0,0]
minVolt=[0,0,0]
avgVolt=[0,0,0]
gapVolt=[0,0,0]
maxTemp=[0,0,0]
minTemp=[0,0,0]
avgTemp=[0,0,0]
gapTemp=[0,0,0]

batteryState=0
current=0
voltage=0
#currentCapacity=0
soc=0
mainPosRelayState=0
mainNegRelayState=0
isoState=-1

requestCount=0
csc1ReplyCount=0
csc2ReplyCount=0
csc3ReplyCount=0

requestCount10s=0
csc1ReplyCount10s=0
csc2ReplyCount10s=0
csc3ReplyCount10s=0
logFileHnd = 0
#class PCANBasic(object):
class PCANBasicClass():
	## Constructor
	##
	def __init__(self,parent):
		global logFileHnd
		self.m_objPCANBasic = PCANBasic()
		self.m_PcanHandle = PCAN_USBBUS1
		self.baudrate = CAN_BUS_CLOCK
		self.hwtype = PCAN_TYPE_ISA_SJA
		self.ioport = int('0x2A0',16)
		self.interrupt = 11
		self.initCanDevice()
		
		self.errLogFileHnd = open('Log\\errLogFile.csv', 'w')
		self.errLogFileHnd.write("时间标识,电芯编号,电压值(mV),\n")
		tempCurData = time.strftime( "%Y-%m-%d_%H-%M-%S", time.localtime())
		logFileHnd = open('Log\\logFile_'+str(tempCurData)+'.csv', 'w')
		logFileHnd.write("时间,SOC,总电压(V),总电流(A),平均电压(mV),"+"\
			最大电压(mV),最大电压位置,最小电压(mV),最小电压位置,压差(mV),"+"\
			最高温度(℃),最高温度位置,最低温度(℃),最低温度位置,"+"\
			V1(mV),V2(mV),V3(mV),V4(mV),V5(mV),V6(mV),V7(mV),V8(mV),V9(mV),"+"\
			V10(mV),V11(mV),V12(mV),V13(mV),V14(mV),V15(mV),V16(mV),V17(mV),V18(mV),V19(mV),"+"\
			V20(mV),V21(mV),V22(mV),V23(mV),V24(mV),V25(mV),V26(mV),V27(mV),V28(mV),V29(mV),"+"\
			V30(mV),V31(mV),V32(mV),V33(mV),V34(mV),V35(mV),V36(mV),V37(mV),V38(mV),V39(mV),"+"\
			V40(mV),V41(mV),V42(mV),V43(mV),V44(mV),V45(mV),V46(mV),V47(mV),V48(mV),V49(mV),"+"\
			V50(mV),V51(mV),V52(mV),V53(mV),V54(mV),V55(mV),V56(mV),V57(mV),V58(mV),V59(mV),"+"\
			V60(mV),V61(mV),V62(mV),V63(mV),V64(mV),V65(mV),V66(mV),V67(mV),V68(mV),V69(mV),"+"\
			V70(mV),V71(mV),V72(mV),V73(mV),V74(mV),V75(mV),V76(mV),V77(mV),V78(mV),V79(mV),"+"\
			V80(mV),V81(mV),V82(mV),V83(mV),V84(mV),V85(mV),V86(mV),V87(mV),V88(mV),V89(mV),"+"\
			V90(mV),"+"\
			T1(℃),T2(℃),T3(℃),T4(℃),T5(℃),T6(℃),T7(℃),T8(℃),T9(℃),T10(℃),T11(℃),T12(℃)\n")
		# self._lock = RLock()
		#self.setConnectionStatus(False)
	
	def destroy(self):
		self.m_objPCANBasic.Uninitialize(self.m_PcanHandle)
		self.setConnectionStatus(False)
		self.errLogFileHnd.close()
		logFileHnd.close()
		

	def initCanDevice(self):
		# gets the connection values
		#
		# self.m_objPCANBasic = PCANBasic()
		# self.m_PcanHandle = PCAN_USBBUS1
		# #self.m_LastMsgsList = []

		# self.baudrate = CAN_BUS_CLOCK
		# self.hwtype = PCAN_TYPE_ISA_SJA
		# self.ioport = int('0x2A0',16)
		# self.interrupt = 11

		# Connects a selected PCAN-Basic channel
		#
		result =  self.m_objPCANBasic.Initialize(self.m_PcanHandle,self.baudrate,self.hwtype,self.ioport,self.interrupt)

		#if result != PCAN_ERROR_OK:
		#	if result != PCAN_ERROR_CAUTION:
		#		tkMessageBox.showinfo("Error!", self.GetFormatedError(result))
		#	else:
		#		self.IncludeTextMessage('******************************************************')
		#		self.IncludeTextMessage('The bitrate being used is different than the given one')
		#		self.IncludeTextMessage('******************************************************')
		#		result = PCAN_ERROR_OK
		#else:
		#	# Prepares the PCAN-Basic's PCAN-Trace file
		#	#
		#	self.ConfigureTraceFile()

		# Sets the connection status of the form
		#
		self.setConnectionStatus(result == PCAN_ERROR_OK)

	def setConnectionStatus(self, bConnected=True):
		global PCANConnected
		# Gets the status values for each case
		#
		PCANConnected = bConnected

	def readMessages(self):
		global PCANConnected
		stsResult = PCAN_ERROR_OK

		# We read at least one time the queue looking for messages.
		# If a message is found, we look again trying to find more.
		# If the queue is empty or an error occurr, we get out from
		# the dowhile statement.
		#
		while (PCANConnected and not (stsResult & PCAN_ERROR_QRCVEMPTY)):
			stsResult=self.readMessage()
			if stsResult == PCAN_ERROR_ILLOPERATION:
				break

	def readMessage(self):
		# We execute the "Read" function of the PCANBasic
		#
		result = self.m_objPCANBasic.Read(self.m_PcanHandle)

		if result[0] == PCAN_ERROR_OK:
			self.processMessage(result[1:])
		#else:
			#print 'PCAN ERROR:%d',result[0]  
		return result[0]

	def writeFrame(self,id,len,type,buffer):   
		# We create a TPCANMsg message structure
		#
		CANMsg = TPCANMsg()

		# We configurate the Message.  The ID,
		# Length of the Data, Message Type and the data
		#
		CANMsg.ID = id
		CANMsg.LEN = len
		CANMsg.MSGTYPE = type #PCAN_MESSAGE_STANDARD

		# # If a remote frame will be sent, the data bytes are not important.
		# #
		# if self.m_RemoteCHB.get():
		#     CANMsg.MSGTYPE |= PCAN_MESSAGE_RTR.value
		# else:
		#     # We get so much data as the Len of the message
		#     #
		for i in range(CANMsg.LEN):
			CANMsg.DATA[i] = buffer[i]

		# The message is sent to the configured hardware
		#
		return self.m_objPCANBasic.Write(self.m_PcanHandle, CANMsg)

	def processMessage(self, *args): 
		global curMenu,curCscPage
		global batteryState,current,voltage,soc,mainPosRelayState,mainNegRelayState,isoState #,currentCapacity
		global requestCount,csc1ReplyCount,csc2ReplyCount,csc3ReplyCount
		global requestCount10s,csc1ReplyCount10s,csc2ReplyCount10s,csc3ReplyCount10s
		#with self._lock:       
			# Split the arguments. [0] TPCANMsg, [1] TPCANTimestamp
			#updateMsgFlag=False
			#theMsg = args[0][0]
		newMsg = args[0][0]
		self.TimeStamp = args[0][1]    
		if (newMsg.ID==32) and (newMsg.DATA[0]==248):
			requestCount += 1
			requestCount10s += 1
		elif newMsg.ID==CAN_MSG_ID_CSC1_VOLT:
			csc1ReplyCount += 1
			csc1ReplyCount10s += 1
		elif newMsg.ID==CAN_MSG_ID_CSC2_VOLT:
			csc2ReplyCount += 1
			csc2ReplyCount10s += 1
		elif newMsg.ID==CAN_MSG_ID_CSC3_VOLT:
			csc3ReplyCount += 1
			csc3ReplyCount10s += 1
		#if curMenu==0:
			#if curCscPage==0:
		if newMsg.ID==CAN_MSG_ID_CSC1_VOLT:
			#self.calcVolt(curCscPage,newMsg)
			self.calcVolt(0,newMsg)
		elif newMsg.ID==CAN_MSG_ID_CSC1_TEMP:
			self.calcTemp(0,newMsg)
					#updateMsgFlag=True
			#elif curCscPage==1:
		elif newMsg.ID==CAN_MSG_ID_CSC2_VOLT:
			self.calcVolt(1,newMsg)
		elif newMsg.ID==CAN_MSG_ID_CSC2_TEMP:
			self.calcTemp(1,newMsg)
			#elif curCscPage==2:
		elif newMsg.ID==CAN_MSG_ID_CSC3_VOLT:
			self.calcVolt(2,newMsg)
		elif newMsg.ID==CAN_MSG_ID_CSC3_TEMP:
			self.calcTemp(2,newMsg)
		# if curMenu==1:
		elif newMsg.ID==CAN_MSG_ID_BMS_STATE:
			batteryState=newMsg.DATA[5]&0xf
			current=(newMsg.DATA[0]<<4)+(newMsg.DATA[1]>>4)
			voltage=((newMsg.DATA[1]&15)<<8)+newMsg.DATA[2]
			soc=newMsg.DATA[3]
			mainPosRelayState=(newMsg.DATA[4]>>2)&3
			mainNegRelayState=(newMsg.DATA[4]>>4)&3
		elif newMsg.ID==CAN_MSG_ID_ISO_STATE:
			#currentCapacity=(newMsg.DATA[0]<<2)+(newMsg.DATA[1]>>6)
			isoState=((newMsg.DATA[1]&63)<<4)+(newMsg.DATA[2]>>4)
		
	def calcVolt(self,page,msg):
		cellID=msg.DATA[0]
		if (cellID < 32):
			Value0=(msg.DATA[1]<<6)+(msg.DATA[2]>>2)
			Value1=((msg.DATA[2]&3)<<12)+(msg.DATA[3]<<4)+(msg.DATA[4]>>4)
			Value0=20002*Value0//65535
			Value1=20002*Value1//65535
			cscVolt[page][cellID] = Value0
			cscVolt[page][cellID+1] = Value1
			if (Value0>4230) or (Value0<2800):
				self.errLogFileHnd.write(str(self.TimeStamp)+","+str(page+1)+"--"+str(cellID+1)+","+str(Value0)+",\n" )
			if (Value1>4230) or (Value1<2800):
				self.errLogFileHnd.write(str(self.TimeStamp)+","+str(page+1)+"--"+str(cellID+2)+","+str(Value1)+",\n" )
			if (cellID < 28):
				Value2=((msg.DATA[4]&15)<<10)+(msg.DATA[5]<<2)+(msg.DATA[6]>>6)
				Value3=((msg.DATA[6]&63)<<8)+msg.DATA[7]
				Value2=20002*Value2//65535
				Value3=20002*Value3//65535
				cscVolt[page][cellID+2] = Value2
				cscVolt[page][cellID+3] = Value3
				if (Value2>4230) or (Value2<2800):
					self.errLogFileHnd.write(str(self.TimeStamp)+","+str(page+1)+"--"+str(cellID+3)+","+str(Value2)+",\n" )
				if (Value3>4230) or (Value3<2800):
					self.errLogFileHnd.write(str(self.TimeStamp)+","+str(page+1)+"--"+str(cellID+4)+","+str(Value3)+",\n" )
			maxVolt[page] = max(cscVolt[page])
			minVolt[page] = min(cscVolt[page])
			avgVolt[page] = sum(cscVolt[page]) // len(cscVolt[page])
			gapVolt[page] = maxVolt[page]-minVolt[page]
	
	def calcTemp(self,page,msg):
		cellID=msg.DATA[0]
		if cellID < 4:
			Value0=(msg.DATA[1]<<6)+(msg.DATA[2]>>2)
			Value1=((msg.DATA[2]&3)<<12)+(msg.DATA[3]<<4)+(msg.DATA[4]>>4)
			Value2=((msg.DATA[4]&15)<<10)+(msg.DATA[5]<<2)+(msg.DATA[6]>>6)
			Value3=((msg.DATA[6]&63)<<8)+msg.DATA[7]
			Value0=lookupTable.lookupTable(Value0)
			Value1=lookupTable.lookupTable(Value1)
			Value2=lookupTable.lookupTable(Value2)
			Value3=lookupTable.lookupTable(Value3)
			cscTemp[page][cellID] = Value0
			cscTemp[page][cellID+1] = Value1
			cscTemp[page][cellID+2] = Value2
			cscTemp[page][cellID+3] = Value3
			maxTemp[page] = max(cscTemp[page])
			minTemp[page] = min(cscTemp[page])
			#avgTemp[page] = round(float(sum(cscTemp[page])) / len(cscTemp[page]),2)
			avgTemp[page] = sum(cscTemp[page]) // len(cscTemp[page])
			gapTemp[page] = maxTemp[page]-minTemp[page]
