import wx
import autoGenUi

#import time
from threading import Thread,Event
import canMessage
from wx.lib.pubsub import pub

#Variable define
TIMER_UPDATE_UI = 0.2
TIMER_READ_MSG = 0.01
TIMER_PCAN_RECONNECT = 1
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
			handle.SetCellValue(0, 2, "Max Volt(mV):")
			handle.SetCellValue(1, 2, "Min Volt(mV):")
			handle.SetCellValue(2, 2, "Avg Volt(mV):")
			handle.SetCellValue(3, 2, "Delt Volt(mV):")
			handle.SetCellValue(4, 2, "===========================")
			handle.SetCellValue(5, 2, "Max Temp(C):")
			handle.SetCellValue(6, 2, "Min Temp(C):")
			handle.SetCellValue(7, 2, "Avg Temp(C):")
			handle.SetCellValue(8, 2, "Delt Temp(C):")
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
			handle.SetColLabelValue(0, "Voltage(mV)")
			handle.SetColLabelValue(1, "Temper(C)")
			handle.SetColLabelValue(2, "")
			handle.SetColLabelValue(3, "Value")
			handle.SetColLabelValue(4, "CellNum")
		
		self.m_propertyGridItem1.Enable(False)
		self.m_propertyGridItem2.Enable(False)
		self.m_propertyGridItem3.Enable(False)
		self.m_propertyGridItem4.Enable(False)
		self.m_propertyGridItem5.Enable(False)
		self.m_propertyGridItem6.Enable(False)
		self.m_propertyGridItem7.Enable(False)
		self.m_propertyGridItem8.Enable(False)
		self.m_propertyGridItem9.Enable(False)
		self.m_propertyGridItem1.SetValue("Initialize")#0:Initialize 3:Output 6:Chargeing 9:Running
		self.m_propertyGridItem3.SetValue(104)
		self.m_propertyGridItem6.SetValue(100)
		self.m_propertyGridItem7.SetValue("NA")
		self.m_propertyGridItem8.SetValue("V.1.0.0")
		self.m_button10.Enable( False )
		self.m_button11.Enable( False )
		self.m_textCtrl1.Enable( False )
		
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
			dlg = MessageDialog('Welcome!','Info')  
			wx.FutureCall(2000, dlg.Destroy)
			dlg.ShowModal()
			self.m_button14.Enable( True )
			#self.m_button14.SetFoucs
			
		else:
			dlg = wx.MessageDialog(None,'Password Error!','Error',wx.ICON_ERROR)
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
				for row in range(32):
					handle.SetCellValue(row, 0, str(canMessage.cscVolt[canMessage.curCscPage][row]))
				for row in range(8):
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
					batstate="Initialize"
				elif canMessage.batteryState==3:
					batstate="Output"
				elif canMessage.batteryState==6:
					batstate="Chargeing"
				elif canMessage.batteryState==9:
					batstate="Running"
				self.m_propertyGridItem1.SetValue(batstate)
				self.m_propertyGridItem9.SetValue(round(canMessage.voltage/4.0,2))
				self.m_propertyGridItem2.SetValue(round(canMessage.current/4.0-511,2))
				self.m_propertyGridItem4.SetValue(round(canMessage.currentCapacity*0.05,2))
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
		else:
			self.closeRelayTime += 1
			hour = self.closeRelayTime//3600
			min = (self.closeRelayTime%3600)//60
			sec = (self.closeRelayTime%3600)%60
			self.m_staticText14.SetLabel(str(hour).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2))
class msgThread(Thread):
	"""Test Worker Thread Class."""
	#----------------------------------------------------------------------
	def __init__(self):
		"""Init Worker Thread Class."""
		Thread.__init__(self)
		self.event = Event()
		self.reConnectCont = 0
		self.timeCounter = 0
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
			if self.startTime == True:
				pub.sendMessage("update", msg=2)
			#pcanInfo = canMessage.PCANBasicClass(self)
		if canMessage.PCANConnected == True:
			#print "Read Message"
			self.pcanInfo.readMessages()
			self.timeCounter+=1
			if self.timeCounter >= (TIMER_UPDATE_UI//TIMER_READ_MSG):
				self.timeCounter = 0
				pub.sendMessage("update", msg=1)
	
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