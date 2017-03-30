# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.propgrid as pg

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,630 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 695,630 ), wx.DefaultSize )
		
		bSizer_csc_mainPanel = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listbook_menu = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT|wx.RAISED_BORDER )
		m_listbook_menuImageSize = wx.Size( 64,64 )
		m_listbook_menuIndex = 0
		m_listbook_menuImages = wx.ImageList( m_listbook_menuImageSize.GetWidth(), m_listbook_menuImageSize.GetHeight() )
		self.m_listbook_menu.AssignImageList( m_listbook_menuImages )
		self.m_panel_csc = wx.Panel( self.m_listbook_menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_csc = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook_csc = wx.Notebook( self.m_panel_csc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_csc1 = wx.Panel( self.m_notebook_csc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_csc1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid_csc1 = wx.grid.Grid( self.m_panel_csc1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid_csc1.CreateGrid( 30, 5 )
		self.m_grid_csc1.EnableEditing( False )
		self.m_grid_csc1.EnableGridLines( True )
		self.m_grid_csc1.EnableDragGridSize( False )
		self.m_grid_csc1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid_csc1.EnableDragColMove( False )
		self.m_grid_csc1.EnableDragColSize( True )
		self.m_grid_csc1.SetColLabelSize( 30 )
		self.m_grid_csc1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid_csc1.EnableDragRowSize( True )
		self.m_grid_csc1.SetRowLabelSize( 80 )
		self.m_grid_csc1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid_csc1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer_csc1.Add( self.m_grid_csc1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_csc1.SetSizer( bSizer_csc1 )
		self.m_panel_csc1.Layout()
		bSizer_csc1.Fit( self.m_panel_csc1 )
		self.m_notebook_csc.AddPage( self.m_panel_csc1, u"CSC1", True )
		self.m_panel_csc2 = wx.Panel( self.m_notebook_csc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_csc2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid_csc2 = wx.grid.Grid( self.m_panel_csc2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid_csc2.CreateGrid( 30, 5 )
		self.m_grid_csc2.EnableEditing( True )
		self.m_grid_csc2.EnableGridLines( True )
		self.m_grid_csc2.EnableDragGridSize( False )
		self.m_grid_csc2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid_csc2.EnableDragColMove( False )
		self.m_grid_csc2.EnableDragColSize( True )
		self.m_grid_csc2.SetColLabelSize( 30 )
		self.m_grid_csc2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid_csc2.EnableDragRowSize( True )
		self.m_grid_csc2.SetRowLabelSize( 80 )
		self.m_grid_csc2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid_csc2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer_csc2.Add( self.m_grid_csc2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_csc2.SetSizer( bSizer_csc2 )
		self.m_panel_csc2.Layout()
		bSizer_csc2.Fit( self.m_panel_csc2 )
		self.m_notebook_csc.AddPage( self.m_panel_csc2, u"CSC2", False )
		self.m_panel_csc3 = wx.Panel( self.m_notebook_csc, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_csc3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_grid_csc3 = wx.grid.Grid( self.m_panel_csc3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid_csc3.CreateGrid( 30, 5 )
		self.m_grid_csc3.EnableEditing( True )
		self.m_grid_csc3.EnableGridLines( True )
		self.m_grid_csc3.EnableDragGridSize( False )
		self.m_grid_csc3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid_csc3.EnableDragColMove( False )
		self.m_grid_csc3.EnableDragColSize( True )
		self.m_grid_csc3.SetColLabelSize( 30 )
		self.m_grid_csc3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid_csc3.EnableDragRowSize( True )
		self.m_grid_csc3.SetRowLabelSize( 80 )
		self.m_grid_csc3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid_csc3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer_csc3.Add( self.m_grid_csc3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_csc3.SetSizer( bSizer_csc3 )
		self.m_panel_csc3.Layout()
		bSizer_csc3.Fit( self.m_panel_csc3 )
		self.m_notebook_csc.AddPage( self.m_panel_csc3, u"CSC3", False )
		
		bSizer_csc.Add( self.m_notebook_csc, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel_csc.SetSizer( bSizer_csc )
		self.m_panel_csc.Layout()
		bSizer_csc.Fit( self.m_panel_csc )
		self.m_listbook_menu.AddPage( self.m_panel_csc, u"CSC", False )
		m_listbook_menuBitmap = wx.Bitmap( u"src/1.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook_menuBitmap.Ok() ):
			m_listbook_menuImages.Add( m_listbook_menuBitmap )
			self.m_listbook_menu.SetPageImage( m_listbook_menuIndex, m_listbook_menuIndex )
			m_listbook_menuIndex += 1
		
		self.m_panel_bms = wx.Panel( self.m_listbook_menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_bms = wx.BoxSizer( wx.VERTICAL )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer38.SetMinSize( wx.Size( -1,205 ) ) 
		self.m_propertyGridManager1 = pg.PropertyGridManager(self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.propgrid.PGMAN_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER)
		self.m_propertyGridManager1.Enable( False )
		
		
		self.m_propertyGridPage1 = self.m_propertyGridManager1.AddPage( u"Page", wx.NullBitmap );
		self.m_propertyGridItem1 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Battery State", u"Battery State" ) ) 
		self.m_propertyGridItem9 = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Voltage(V)", u"Voltage(V)" ) ) 
		self.m_propertyGridItem2 = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Current(A)", u"Current(A)" ) ) 
		self.m_propertyGridItem3 = self.m_propertyGridPage1.Append( pg.IntProperty( u"Nominal Capacity(Ah)", u"Nominal Capacity(Ah)" ) ) 
		self.m_propertyGridItem4 = self.m_propertyGridPage1.Append( pg.FloatProperty( u"Current Capacity(KWh)", u"Current Capacity(KWh)" ) ) 
		self.m_propertyGridItem5 = self.m_propertyGridPage1.Append( pg.FloatProperty( u"SOC(%)", u"SOC(%)" ) ) 
		self.m_propertyGridItem6 = self.m_propertyGridPage1.Append( pg.IntProperty( u"SOH(%)", u"SOH(%)" ) ) 
		self.m_propertyGridItem7 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Pack SN.", u"Pack SN." ) ) 
		self.m_propertyGridItem8 = self.m_propertyGridPage1.Append( pg.StringProperty( u"Version", u"Version" ) ) 
		bSizer38.Add( self.m_propertyGridManager1, 1, wx.EXPAND, 5 )
		
		
		bSizer_bms.Add( bSizer38, 0, wx.EXPAND, 5 )
		
		
		bSizer_bms.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"***** Error/Warning Status *****", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		bSizer_bms.Add( self.m_staticText1, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"MainPosRelay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer12.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel_bms, wx.ID_ANY, wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"MainNegRelay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer13.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer13.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel_bms, wx.ID_ANY, wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer11.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"ISO Normal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer14.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel_bms, wx.ID_ANY, wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText41 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"ISO Warning", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer141.Add( self.m_staticText41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline22 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer141.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_bitmap31 = wx.StaticBitmap( self.m_panel_bms, wx.ID_ANY, wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_bitmap31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		bSizer142 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText42 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"ISO Error", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer142.Add( self.m_staticText42, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline23 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer142.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_bitmap32 = wx.StaticBitmap( self.m_panel_bms, wx.ID_ANY, wx.Bitmap( u"src/11.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer142.Add( self.m_bitmap32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer142, 1, wx.EXPAND, 5 )
		
		
		bSizer_bms.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		self.m_staticline30 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline30, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_bms.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"***** User Control Area *****", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		bSizer_bms.Add( self.m_staticText5, 0, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer37 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer37.Add( self.m_staticText25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel_bms, wx.ID_ANY, u"admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline25 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer37.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer37.Add( self.m_staticText26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel_bms, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		bSizer37.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		self.m_staticline27 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer15.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"Close Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer36.Add( self.m_staticText21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer36.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline24 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer36.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"MainRelay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		bSizer36.Add( self.m_staticText22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel_bms, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button14.Enable( False )
		
		bSizer36.Add( self.m_button14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer36, 1, wx.EXPAND, 5 )
		
		self.m_staticline28 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer15.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText23 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"Open(Cur<1A)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		bSizer35.Add( self.m_staticText23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self.m_panel_bms, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer35.Add( self.m_button10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticline26 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer35.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_panel_bms, wx.ID_ANY, u"EmergencyOpen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer35.Add( self.m_staticText24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self.m_panel_bms, wx.ID_ANY, u"SOS Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_button11.SetMinSize( wx.Size( 140,50 ) )
		
		bSizer35.Add( self.m_button11, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer35, 1, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_bms.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		self.m_staticline32 = wx.StaticLine( self.m_panel_bms, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_bms.Add( self.m_staticline32, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer_bms.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panel_bms.SetSizer( bSizer_bms )
		self.m_panel_bms.Layout()
		bSizer_bms.Fit( self.m_panel_bms )
		self.m_listbook_menu.AddPage( self.m_panel_bms, u"BMS", True )
		m_listbook_menuBitmap = wx.Bitmap( u"src/2.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook_menuBitmap.Ok() ):
			m_listbook_menuImages.Add( m_listbook_menuBitmap )
			self.m_listbook_menu.SetPageImage( m_listbook_menuIndex, m_listbook_menuIndex )
			m_listbook_menuIndex += 1
		
		self.m_panel_car = wx.Panel( self.m_listbook_menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook_menu.AddPage( self.m_panel_car, u"Car", False )
		m_listbook_menuBitmap = wx.Bitmap( u"src/3.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook_menuBitmap.Ok() ):
			m_listbook_menuImages.Add( m_listbook_menuBitmap )
			self.m_listbook_menu.SetPageImage( m_listbook_menuIndex, m_listbook_menuIndex )
			m_listbook_menuIndex += 1
		
		self.m_panel_setting = wx.Panel( self.m_listbook_menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook_menu.AddPage( self.m_panel_setting, u"Setting", False )
		m_listbook_menuBitmap = wx.Bitmap( u"src/4.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook_menuBitmap.Ok() ):
			m_listbook_menuImages.Add( m_listbook_menuBitmap )
			self.m_listbook_menu.SetPageImage( m_listbook_menuIndex, m_listbook_menuIndex )
			m_listbook_menuIndex += 1
		
		self.m_panel_diag = wx.Panel( self.m_listbook_menu, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook_menu.AddPage( self.m_panel_diag, u"Diag", False )
		m_listbook_menuBitmap = wx.Bitmap( u"src/5.png", wx.BITMAP_TYPE_ANY )
		if ( m_listbook_menuBitmap.Ok() ):
			m_listbook_menuImages.Add( m_listbook_menuBitmap )
			self.m_listbook_menu.SetPageImage( m_listbook_menuIndex, m_listbook_menuIndex )
			m_listbook_menuIndex += 1
		
		
		bSizer_csc_mainPanel.Add( self.m_listbook_menu, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_csc_mainPanel )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_listbook_menu.Bind( wx.EVT_LISTBOOK_PAGE_CHANGED, self.funcMenuChanged )
		self.m_listbook_menu.Bind( wx.EVT_LISTBOOK_PAGE_CHANGING, self.funcMenuChanging )
		self.m_notebook_csc.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.cscPageChanged )
		self.m_notebook_csc.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGING, self.cscPageChanging )
		self.m_textCtrl1.Bind( wx.EVT_TEXT_ENTER, self.passwordInputFinished )
		self.m_button14.Bind( wx.EVT_BUTTON, self.closeMainRelay )
		self.m_button10.Bind( wx.EVT_BUTTON, self.openMainRelay )
		self.m_button11.Bind( wx.EVT_BUTTON, self.openMainRelayEmergency )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def funcMenuChanged( self, event ):
		event.Skip()
	
	def funcMenuChanging( self, event ):
		event.Skip()
	
	def cscPageChanged( self, event ):
		event.Skip()
	
	def cscPageChanging( self, event ):
		event.Skip()
	
	def passwordInputFinished( self, event ):
		event.Skip()
	
	def closeMainRelay( self, event ):
		event.Skip()
	
	def openMainRelay( self, event ):
		event.Skip()
	
	def openMainRelayEmergency( self, event ):
		event.Skip()
	

