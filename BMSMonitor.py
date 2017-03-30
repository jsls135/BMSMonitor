# -*- coding: utf-8 -*-
import wx
import autoGenUi
import time

#import time
from threading import Thread,Event
import canMessage
from wx.lib.pubsub import pub

#Variable define
TIMER_UPDATE_UI = 0.2
TIMER_READ_MSG = 0.01
TIMER_PCAN_RECONNECT = 1
TIMER_MISSRATE_3S = 3
TIMER_WRITELOG_2S = 2
TIMER_MISSRATE_10S = 10
#timeCounter = 0
#pcanInfo=None
controlBuffer=[0,0,0,0,0,0,0,0]

class mainWindow(autoGenUi.mainFrame):
	def __init__( self, parent ):
		autoGenUi.mainFrame.__init__( self, parent )
		
		for page in range(3):
			if page == 0:
				handle = self.m_grid_csc1
			elif page == 1:
				handle = self.m_grid_csc2
			else:
				handle = self.m_grid_csc3
			handle.SetColSize(0, 100)
			handle.SetColSize(2, 90)
			handle.SetCellValue(0, 2, "最大电压(mV):")
			handle.SetCellValue(1, 2, "最小电压(mV):")
			handle.SetCellValue(2, 2, "平均电压(mV):")
			handle.SetCellValue(3, 2, "压      差(mV):")
			handle.SetCellValue(4, 2, "===========================")
			handle.SetCellValue(5, 2, "最大温度(℃):")
			handle.SetCellValue(6, 2, "最小温度(℃):")
			handle.SetCellValue(7, 2, "平均温度(℃):")
			handle.SetCellValue(8, 2, "温      差(℃):")
			handle.SetCellValue(9, 2, "===========================")
			handle.SetCellBackgroundColour(0, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(1, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(2, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(3, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(4, 2, wx.Colour(190,190,190))
			handle.SetCellBackgroundColour(4, 3, wx.Colour(190,190,190))
			handle.SetCellBackgroundColour(4, 4, wx.Colour(190,190,190))
			handle.SetCellBackgroundColour(5, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(6, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(7, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(8, 2, wx.Colour(245,245,245))
			handle.SetCellBackgroundColour(9, 2, wx.Colour(190,190,190))
			handle.SetCellBackgroundColour(9, 3, wx.Colour(190,190,190))
			handle.SetCellBackgroundColour(9, 4, wx.Colour(190,190,190))
		
			handle.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_BOTTOM)
			handle.SetColLabelValue(0, "电压(mV)")
			handle.SetColLabelValue(1, "温度(℃)")
			handle.SetColLabelValue(2, "")
			handle.SetColLabelValue(3, "值")
			handle.SetColLabelValue(4, "电芯号")
		
		self.m_propertyGridItem1.Enable(False)
		self.m_propertyGridItem2.Enable(False)
		#self.m_propertyGridItem3.Enable(False)
		#self.m_propertyGridItem4.Enable(False)
		self.m_propertyGridItem5.Enable(False)
		#self.m_propertyGridItem6.Enable(False)
		#self.m_propertyGridItem7.Enable(False)
		#self.m_propertyGridItem8.Enable(False)
		self.m_propertyGridItem9.Enable(False)
		self.m_propertyGridItem10.Enable(False)
		self.m_propertyGridItem11.Enable(False)
		self.m_propertyGridItem12.Enable(False)
		self.m_propertyGridItem13.Enable(False)
		self.m_propertyGridItem14.Enable(False)
		self.m_propertyGridItem15.Enable(False)
		self.m_propertyGridItem16.Enable(False)
		self.m_propertyGridItem17.Enable(False)
		self.m_propertyGridItem1.SetValue("初始化")#0:Initialize 3:Output 6:Chargeing 9:Running
		#self.m_propertyGridItem3.SetValue(104)
		#self.m_propertyGridItem6.SetValue(100)
		#self.m_propertyGridItem7.SetValue("NA")
		#self.m_propertyGridItem8.SetValue("V.1.0.0")
		self.m_button10.Enable( False )
		self.m_button11.Enable( False )
		self.m_textCtrl1.Enable( False )
		
		self.m_statusBar1.SetFieldsCount(3)
		self.m_statusBar1.SetStatusText("CSC1 丢包率:", 0)
		self.m_statusBar1.SetStatusText("CSC2 丢包率:", 1)
		self.m_statusBar1.SetStatusText("CSC3 丢包率:", 2)
		
		#self.ledOffPic = images.LB10.GetBitmap()
		self.ledOffPic = wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY )
		self.ledOnPic = wx.Bitmap( u"src/12.png", wx.BITMAP_TYPE_ANY )
		self.ledWarningPic = wx.Bitmap( u"src/13.png", wx.BITMAP_TYPE_ANY )
		self.ledErrorPic = wx.Bitmap( u"src/14.png", wx.BITMAP_TYPE_ANY )
		self.m_button14.SetBackgroundColour(wx.Colour(255,255,0))
		self.m_button10.SetBackgroundColour(wx.Colour(0,255,0))
		self.m_button11.SetBackgroundColour(wx.Colour(255,0,0))
		#self.timer = wx.Timer(self)
		#self.Bind(wx.EVT_TIMER, self.OnTimer,self.timer)
		#self.pcanInfo = pcanInfo = canMessage.PCANBasicClass(self)
		pub.subscribe(self.updateUI, "update")
		self.msgthread = msgThread()
		
	def __del__( self ):
		#global pcanInfo
		#self.OffTimer()
		self.msgthread.stop()
		#if canMessage.PCANConnected == True:
			#self.pcanInfo.destroy()
		pass
	
	def funcMenuChanged( self, event ):
		canMessage.curMenu = event.GetSelection()
		#print canMessage.curMenu
		event.Skip()

	def cscPageChanged( self, event ):
		canMessage.curCscPage = event.GetSelection()
		#print canMessage.curCscPage
		event.Skip()
	
	def passwordInputFinished( self, event ):
		if "123" == self.m_textCtrl1.GetValue():
			dlg = MessageDialog('欢迎您，登陆成功!','信息')  
			wx.FutureCall(2000, dlg.Destroy)
			dlg.ShowModal()
			self.m_button14.Enable( True )
			#self.m_button14.SetFoucs
			
		else:
			dlg = wx.MessageDialog(None,'抱歉，密码错误!','错误',wx.ICON_ERROR)
			dlg.ShowModal()
				
		event.Skip()
	
	def closeMainRelay( self, event ):
		#print "close relay"
		global controlBuffer
		#self.startTime = time.time()
		#self.timer.Start(1000)
		#self.startTime = True
		self.msgthread.startTimer(True)
		self.closeRelayTime = 0
		controlBuffer[0]=(5<<4)
		pub.sendMessage("control")
		event.Skip()
	
	def openMainRelay( self, event ):
		global controlBuffer
		#self.OffTimer()
		#self.startTime = False
		self.msgthread.startTimer(False)
		#print "open relay"
		controlBuffer[0]=(6<<4)
		pub.sendMessage("control")
		event.Skip()
	
	def openMainRelayEmergency( self, event ):
		#self.startTime = False
		global controlBuffer
		controlBuffer[0]=(7<<4)
		self.msgthread.startTimer(False)
		pub.sendMessage("control")
		event.Skip()
	
	'''def OnTimer(self, evt):
		gapt =time.time() - self.startTime
		t = time.localtime(gapt)
		st = time.strftime("%H:%M:%S", t)
		self.m_staticText101.SetLabel(st)'''
	
	#def OffTimer(self):
		#self.timer.Stop()

	def updateUI(self, msg):
		"""Receives data from thread and updates the display"""
		#print "update UI" 
		
		if msg == 1:
			if canMessage.curMenu == 0:
				if canMessage.curCscPage == 0:
					handle = self.m_grid_csc1
				elif canMessage.curCscPage == 1:
					handle = self.m_grid_csc2
				elif canMessage.curCscPage == 2:
					handle = self.m_grid_csc3
				for row in range(30):
					handle.SetCellValue(row, 0, str(canMessage.cscVolt[canMessage.curCscPage][row]))
				for row in range(4):
					handle.SetCellValue(row, 1, str(canMessage.cscTemp[canMessage.curCscPage][row]))
				handle.SetCellValue(0, 3, str(canMessage.maxVolt[canMessage.curCscPage]))
				handle.SetCellValue(0, 4, str(canMessage.cscVolt[canMessage.curCscPage].index(canMessage.maxVolt[canMessage.curCscPage])+1))
				handle.SetCellValue(1, 3, str(canMessage.minVolt[canMessage.curCscPage]))
				handle.SetCellValue(1, 4, str(canMessage.cscVolt[canMessage.curCscPage].index(canMessage.minVolt[canMessage.curCscPage])+1))
				handle.SetCellValue(2, 3, str(canMessage.avgVolt[canMessage.curCscPage]))
				handle.SetCellValue(3, 3, str(canMessage.gapVolt[canMessage.curCscPage]))
				handle.SetCellValue(5, 3, str(canMessage.maxTemp[canMessage.curCscPage]))
				handle.SetCellValue(5, 4, str(canMessage.cscTemp[canMessage.curCscPage].index(canMessage.maxTemp[canMessage.curCscPage])+1))
				handle.SetCellValue(6, 3, str(canMessage.minTemp[canMessage.curCscPage]))
				handle.SetCellValue(6, 4, str(canMessage.cscTemp[canMessage.curCscPage].index(canMessage.minTemp[canMessage.curCscPage])+1))
				handle.SetCellValue(7, 3, str(canMessage.avgTemp[canMessage.curCscPage]))
				handle.SetCellValue(8, 3, str(canMessage.gapTemp[canMessage.curCscPage]))
			elif canMessage.curMenu == 1:
				if False == self.m_button10.IsEnabled():
					self.m_button10.Enable( True )
				if False == self.m_button11.IsEnabled():
					self.m_button11.Enable( True )
				if False == self.m_textCtrl1.IsEnabled():
					self.m_textCtrl1.Enable( True )
				if canMessage.batteryState==0:
					batstate="初始化"
				elif canMessage.batteryState==3:
					batstate="输出模式"
				elif canMessage.batteryState==6:
					batstate="充电中"
				elif canMessage.batteryState==9:
					batstate="运行中"
				self.m_propertyGridItem1.SetValue(batstate)
				self.m_propertyGridItem9.SetValue(round(canMessage.voltage/4.0,2))
				self.m_propertyGridItem2.SetValue(round(canMessage.current/4.0-511,2))
				#self.m_propertyGridItem4.SetValue(round(canMessage.currentCapacity*0.05,2))
				self.m_propertyGridItem5.SetValue(canMessage.soc/2.0)
				if canMessage.mainPosRelayState==0:
					self.m_bitmap1.SetBitmap(self.ledOffPic)
				else:
					self.m_bitmap1.SetBitmap(self.ledOnPic)
				if canMessage.mainNegRelayState==0:
					self.m_bitmap2.SetBitmap(self.ledOffPic)
				else:
					self.m_bitmap2.SetBitmap(self.ledOnPic)
				#canMessage.isoState*1000/canMessage.voltage > 500
				normalResisThread = 5*25*canMessage.voltage/10000
				errorResisaThread = 2*25*canMessage.voltage/10000
				if canMessage.isoState>normalResisThread:
					self.m_bitmap3.SetBitmap(self.ledOnPic)
					self.m_bitmap31.SetBitmap(self.ledOffPic)
					self.m_bitmap32.SetBitmap(self.ledOffPic)
				elif (canMessage.isoState<errorResisaThread) and (canMessage.isoState!=-1):
					self.m_bitmap3.SetBitmap(self.ledOffPic)
					self.m_bitmap31.SetBitmap(self.ledOffPic)
					self.m_bitmap32.SetBitmap(self.ledErrorPic)
				elif (canMessage.isoState>=errorResisaThread) and (canMessage.isoState<=normalResisThread):
					self.m_bitmap3.SetBitmap(self.ledOffPic)
					self.m_bitmap31.SetBitmap(self.ledWarningPic)
					self.m_bitmap32.SetBitmap(self.ledOffPic)
				else:
					pass
				#self.m_propertyGridPage2 == 
				self.m_propertyGridItem10.SetValue(str(max(canMessage.maxVolt)))
				self.m_propertyGridItem11.SetValue(str(min(canMessage.minVolt)))
				self.m_propertyGridItem12.SetValue(str(sum(canMessage.avgVolt)//3))
				self.m_propertyGridItem13.SetValue(str(max(canMessage.maxVolt)-min(canMessage.minVolt)))
				self.m_propertyGridItem14.SetValue(str(max(canMessage.maxTemp)))
				self.m_propertyGridItem15.SetValue(str(min(canMessage.minTemp)))
				self.m_propertyGridItem16.SetValue(str(sum(canMessage.avgTemp)//3))
				self.m_propertyGridItem17.SetValue(str(max(canMessage.maxTemp)-min(canMessage.minTemp)))
		elif msg==2:
			self.closeRelayTime += 1
			hour = self.closeRelayTime//3600
			minute = (self.closeRelayTime%3600)//60
			sec = (self.closeRelayTime%3600)%60
			self.m_staticText14.SetLabel(str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(sec).zfill(2))
		elif (msg==3) or (msg==4):
			if 0==canMessage.requestCount:
				msgMissRate1 = 0
				msgMissRate2 = 0
				msgMissRate3 = 0
			else:
				msgMissRate1 = (1-round(canMessage.csc1ReplyCount/(canMessage.requestCount*8.0),2))*100
				msgMissRate2 = (1-round(canMessage.csc2ReplyCount/(canMessage.requestCount*8.0),2))*100
				msgMissRate3 = (1-round(canMessage.csc3ReplyCount/(canMessage.requestCount*8.0),2))*100
			if 0==canMessage.requestCount10s:
				msgMissRate11 = 0
				msgMissRate12 = 0
				msgMissRate13 = 0
			else:
				msgMissRate11 = (1-round(canMessage.csc1ReplyCount10s/(canMessage.requestCount10s*8.0),2))*100
				msgMissRate12 = (1-round(canMessage.csc2ReplyCount10s/(canMessage.requestCount10s*8.0),2))*100
				msgMissRate13 = (1-round(canMessage.csc3ReplyCount10s/(canMessage.requestCount10s*8.0),2))*100
			if msg == 3:
				canMessage.requestCount = 0
				canMessage.csc1ReplyCount = 0
				canMessage.csc2ReplyCount = 0
				canMessage.csc3ReplyCount = 0
			else:
				canMessage.requestCount10s = 0
				canMessage.csc1ReplyCount10s = 0
				canMessage.csc2ReplyCount10s = 0
				canMessage.csc3ReplyCount10s = 0
			self.m_statusBar1.SetStatusText("CSC1丢包率:  3s:"+str(msgMissRate1)+"%  10s:"+str(msgMissRate11)+"%", 0)
			self.m_statusBar1.SetStatusText("CSC2丢包率:  3s:"+str(msgMissRate2)+"%  10s:"+str(msgMissRate12)+"%", 1)
			self.m_statusBar1.SetStatusText("CSC3丢包率:  3s:"+str(msgMissRate3)+"%  10s:"+str(msgMissRate13)+"%", 2)
		elif msg==5:
			tempCurTime = time.strftime( "%H:%M:%S", time.localtime())
			tempMaxVoltPos = canMessage.cscVolt[canMessage.maxVolt.index(max(canMessage.maxVolt))].index(max(canMessage.maxVolt))+1+canMessage.maxVolt.index(max(canMessage.maxVolt))*30
			tempMinVoltPos = canMessage.cscVolt[canMessage.minVolt.index(min(canMessage.minVolt))].index(min(canMessage.minVolt))+1+canMessage.minVolt.index(min(canMessage.minVolt))*30
			tempMaxTPos = canMessage.cscTemp[canMessage.maxTemp.index(max(canMessage.maxTemp))].index(max(canMessage.maxTemp))+1+canMessage.maxTemp.index(max(canMessage.maxTemp))*4
			tempMinTPos = canMessage.cscTemp[canMessage.minTemp.index(min(canMessage.minTemp))].index(min(canMessage.minTemp))+1+canMessage.minTemp.index(min(canMessage.minTemp))*4
			canMessage.logFileHnd.write(str(tempCurTime)+','+str(int(canMessage.soc//2))+','+str(canMessage.voltage//4)+','+str(canMessage.current//4-511)+','+str(sum(canMessage.avgVolt)//3)+','+
			str(max(canMessage.maxVolt))+','+str(tempMaxVoltPos)+','+str(min(canMessage.minVolt))+','+str(tempMinVoltPos)+','+str(max(canMessage.maxVolt)-min(canMessage.minVolt))+','+
			str(max(canMessage.maxTemp))+','+str(tempMaxTPos)+','+str(min(canMessage.minTemp))+','+str(tempMinTPos))
			for cscIndex in range(3):
				for cellIndex in range(30):
					canMessage.logFileHnd.write(','+str(canMessage.cscVolt[cscIndex][cellIndex]))
			for cscIndex in range(3):
				for tsensorIndex in range(4):
					canMessage.logFileHnd.write(','+str(canMessage.cscTemp[cscIndex][tsensorIndex]))
			canMessage.logFileHnd.write("\n")
		
class msgThread(Thread):
	"""Test Worker Thread Class."""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Init Worker Thread Class."""
		Thread.__init__(self)
		self.event = Event()
		self.reConnectCont = 0
		self.timeCounter = 0
		self.missRate3s = 0
		self.writeLogCount = 0
		self.missRate10s = 0
		self.startTime = False
		self.pcanInfo = canMessage.PCANBasicClass(self)
		pub.subscribe(self.sendControl, "control")
		self.start()    # start the thread

	#----------------------------------------------------------------------
	def run(self):
		"""Run Worker Thread."""
		global TIMER_READ_MSG
		# wx.CallAfter(self.postTime, i)
		# wx.CallAfter(Publisher().sendMessage, "update", "Thread finished!")
		while not self.event.wait(TIMER_READ_MSG):
			wx.CallAfter(self.cycReadMsg)

	#----------------------------------------------------------------------
	def stop(self):
		"""Stops the timer Returns:None"""
		#if (self._thread != None):
		self.event.set()
		if canMessage.PCANConnected == True:
			self.pcanInfo.destroy()
			#self._thread = None
	#----------------------------------------------------------------------
	def startTimer(self,flag):
		self.startTime = flag
	#----------------------------------------------------------------------
	def cycReadMsg(self):
		"""Send time to GUI"""

		self.reConnectCont += 1
		if self.reConnectCont > (TIMER_PCAN_RECONNECT//TIMER_READ_MSG):
			self.reConnectCont=0
			if canMessage.PCANConnected == False:
				#print "Reconnect CAN"
				self.pcanInfo.initCanDevice()
			# if self.startTime == True:
				# pub.sendMessage("update", msg=2)
			#pcanInfo = canMessage.PCANBasicClass(self)
		if canMessage.PCANConnected == True:
			#print "Read Message"
			self.pcanInfo.readMessages()
			self.timeCounter+=1
			if self.timeCounter >= (TIMER_UPDATE_UI//TIMER_READ_MSG):
				self.timeCounter = 0
				pub.sendMessage("update", msg=1)
			self.missRate10s += 1
			self.missRate3s += 1
			self.writeLogCount += 1
			if self.missRate10s > (TIMER_MISSRATE_10S//TIMER_READ_MSG):
				self.missRate10s=0
				pub.sendMessage("update", msg=4)
			if self.missRate3s > (TIMER_MISSRATE_3S//TIMER_READ_MSG):
				self.missRate3s=0
				pub.sendMessage("update", msg=3)
			if self.writeLogCount >(TIMER_WRITELOG_2S//TIMER_READ_MSG):
				self.writeLogCount=0
				pub.sendMessage("update", msg=5)

	def sendControl(self):
		#print "receive control"
		global controlBuffer
		if canMessage.PCANConnected == True:
			self.pcanInfo.writeFrame(0x62,8,0,controlBuffer)
	
class MessageDialog(wx.Dialog):
	def __init__(self, message, title):
		wx.Dialog.__init__(self, None, -1, title,size=(300, 120))
		self.CenterOnScreen(wx.BOTH)
		#ok = wx.Button(self, wx.ID_OK, "OK")
		#ok.SetDefault()
		text = wx.StaticText(self, -1, message)
		vbox = wx.BoxSizer(wx.HORIZONTAL)
		vbox.Add(text, 1, wx.ALIGN_CENTER|wx.ALL, 10)
		#vbox.Add(ok, 1, wx.ALIGN_CENTER|wx.BOTTOM, 10)
		self.SetSizer(vbox)	
		
if __name__ == "__main__":
	app = wx.App(False)
	frame = mainWindow(None)
	frame.Show(True)
	app.MainLoop()