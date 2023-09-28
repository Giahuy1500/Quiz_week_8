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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		PDC_suburb_dropdownChoices = []
		self.PDC_suburb_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PDC_suburb_dropdownChoices, 0 )
		self.PDC_suburb_dropdown.SetSelection( 0 )
		bSizer24.Add( self.PDC_suburb_dropdown, 0, wx.ALL, 5 )
		self.PDC_suburb_dropdown.SetFont( wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

		self.PDC_property_type_label = wx.StaticText( self, wx.ID_ANY, u"Property Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_property_type_label.Wrap( -1 )

		self.PDC_property_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_property_type_label, 0, wx.ALL, 5 )

		PDC_property_dropdownChoices = []
		self.PDC_property_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PDC_property_dropdownChoices, 0 )
		self.PDC_property_dropdown.SetSelection( 0 )
		self.PDC_property_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_property_dropdown, 0, wx.ALL, 5 )

		self.PDC_room_type_label = wx.StaticText( self, wx.ID_ANY, u"Room Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_room_type_label.Wrap( -1 )

		self.PDC_room_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_room_type_label, 0, wx.ALL, 5 )

		PDC_room_dropdownChoices = []
		self.PDC_room_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, PDC_room_dropdownChoices, 0 )
		self.PDC_room_dropdown.SetSelection( 0 )
		self.PDC_room_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_room_dropdown, 0, wx.ALL, 5 )

		self.PDC_search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PDC_search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer24.Add( self.PDC_search_button, 0, wx.ALL, 5 )


		bSizer23.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.PDC_graph = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25.Add( self.PDC_graph, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.PDC_search_button.Bind( wx.EVT_BUTTON, self.PDC_search )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def PDC_search( self, event ):
		event.Skip()


