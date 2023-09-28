# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.keyword_title = wx.StaticText( self, wx.ID_ANY, u"Keyword Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.keyword_title.Wrap( -1 )

		self.keyword_title.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer26.Add( self.keyword_title, 0, wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.KS_keyword_label = wx.StaticText( self, wx.ID_ANY, u"Keyword:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_keyword_label.Wrap( -1 )

		self.KS_keyword_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_keyword_label, 0, wx.ALL, 5 )

		self.KS_keyword_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_keyword_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_keyword_text, 0, wx.ALL, 5 )

		self.KS_cleanliness_label = wx.StaticText( self, wx.ID_ANY, u"Cleanliness:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_cleanliness_label.Wrap( -1 )

		self.KS_cleanliness_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_cleanliness_label, 0, wx.ALL, 5 )

		self.KS_cleanliness_tick = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_cleanliness_tick.SetValue(True)
		bSizer27.Add( self.KS_cleanliness_tick, 0, wx.ALL, 5 )

		self.KS_pool_label = wx.StaticText( self, wx.ID_ANY, u"Pool:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_pool_label.Wrap( -1 )

		self.KS_pool_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_pool_label, 0, wx.ALL, 5 )

		self.KS_pool_tick = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_pool_tick.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_pool_tick, 0, wx.ALL, 5 )

		self.KS_wifi_label = wx.StaticText( self, wx.ID_ANY, u"Wifi:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_wifi_label.Wrap( -1 )

		self.KS_wifi_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_wifi_label, 0, wx.ALL, 5 )

		self.KS_wifi_tick = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_wifi_tick.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_wifi_tick, 0, wx.ALL, 5 )

		self.KS_ac_label = wx.StaticText( self, wx.ID_ANY, u"Air-Conditioning:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_ac_label.Wrap( -1 )

		self.KS_ac_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_ac_label, 0, wx.ALL, 5 )

		self.KS_ac_tick = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_ac_tick.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_ac_tick, 0, wx.ALL, 5 )

		self.KS_search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KS_search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer27.Add( self.KS_search_button, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.KS_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.KS_grid.CreateGrid( 20, 10 )
		self.KS_grid.EnableEditing( True )
		self.KS_grid.EnableGridLines( True )
		self.KS_grid.EnableDragGridSize( False )
		self.KS_grid.SetMargins( 0, 0 )

		# Columns
		self.KS_grid.EnableDragColMove( False )
		self.KS_grid.EnableDragColSize( True )
		self.KS_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.KS_grid.EnableDragRowSize( True )
		self.KS_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.KS_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer28.Add( self.KS_grid, 0, wx.ALL, 5 )


		bSizer26.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.KS_cleanliness_tick.Bind( wx.EVT_CHECKBOX, self.cleanliness_ticked )
		self.KS_pool_tick.Bind( wx.EVT_CHECKBOX, self.pool_ticked )
		self.KS_wifi_tick.Bind( wx.EVT_CHECKBOX, self.wifi_ticked )
		self.KS_ac_tick.Bind( wx.EVT_CHECKBOX, self.ac_ticked )
		self.KS_search_button.Bind( wx.EVT_BUTTON, self.KS_Search )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def cleanliness_ticked( self, event ):
		event.Skip()

	def pool_ticked( self, event ):
		event.Skip()

	def wifi_ticked( self, event ):
		event.Skip()

	def ac_ticked( self, event ):
		event.Skip()

	def KS_Search( self, event ):
		event.Skip()


