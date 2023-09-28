# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 586,386 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.PDC_title = wx.StaticText( self, wx.ID_ANY, u"Price Distribution Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_title.Wrap( -1 )

		self.PDC_title.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer22.Add( self.PDC_title, 0, wx.ALL, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.PDC_suburb_label = wx.StaticText( self, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_suburb_label.Wrap( -1 )

		self.PDC_suburb_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_suburb_label, 0, wx.ALL, 5 )

		self.PDC_suburb_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_suburb_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_suburb_text, 0, wx.ALL, 5 )

		self.PDC_label = wx.StaticText( self, wx.ID_ANY, u"Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_label.Wrap( -1 )

		self.PDC_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_label, 0, wx.ALL, 5 )

		gSizer4 = wx.GridSizer( 2, 5, 0, 0 )

		self.m_checkBox21 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox21.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox21, 0, wx.ALL, 5 )

		self.m_checkBox22 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox22.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox22, 0, wx.ALL, 5 )

		self.m_checkBox23 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox23.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox23, 0, wx.ALL, 5 )

		self.m_checkBox24 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox24.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox24, 0, wx.ALL, 5 )

		self.m_checkBox25 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox25.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox25, 0, wx.ALL, 5 )

		self.m_checkBox26 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox26.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox26, 0, wx.ALL, 5 )

		self.m_checkBox27 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox27.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox27, 0, wx.ALL, 5 )

		self.m_checkBox28 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox28.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox28, 0, wx.ALL, 5 )

		self.m_checkBox29 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox29.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox29, 0, wx.ALL, 5 )

		self.m_checkBox30 = wx.CheckBox( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox30.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer4.Add( self.m_checkBox30, 0, wx.ALL, 5 )


		bSizer24.Add( gSizer4, 1, wx.EXPAND, 5 )

		self.PDC_property_type_label = wx.StaticText( self, wx.ID_ANY, u"Property Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_property_type_label.Wrap( -1 )

		self.PDC_property_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_property_type_label, 0, wx.ALL, 5 )

		self.PDC_property_type_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_property_type_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_property_type_text, 0, wx.ALL, 5 )

		self.PDC_room_type_label = wx.StaticText( self, wx.ID_ANY, u"Room Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_room_type_label.Wrap( -1 )

		self.PDC_room_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_room_type_label, 0, wx.ALL, 5 )

		self.PDC_room_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_room_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_room_text, 0, wx.ALL, 5 )

		self.PDC_search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_search_button, 0, wx.ALL, 5 )


		bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.PDC_graph = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.PDC_graph, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkBox21.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox22.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox23.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox24.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox25.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox26.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox27.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox28.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox29.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )
		self.m_checkBox30.Bind( wx.EVT_CHECKBOX, self.rating_checkbox )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def rating_checkbox( self, event ):
		event.Skip()











