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
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,630 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.SSI_title = wx.StaticText( self, wx.ID_ANY, u"Suburb Specific Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SSI_title.Wrap( -1 )

		self.SSI_title.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer29.Add( self.SSI_title, 0, wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.SSI_property_label = wx.StaticText( self, wx.ID_ANY, u"Property Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SSI_property_label.Wrap( -1 )

		bSizer33.Add( self.SSI_property_label, 0, wx.ALL, 5 )

		SSI_property_type_dropdownChoices = []
		self.SSI_property_type_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SSI_property_type_dropdownChoices, 0 )
		self.SSI_property_type_dropdown.SetSelection( 0 )
		self.SSI_property_type_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer33.Add( self.SSI_property_type_dropdown, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer33, 1, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.SSI_room_label = wx.StaticText( self, wx.ID_ANY, u"Room Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SSI_room_label.Wrap( -1 )

		bSizer34.Add( self.SSI_room_label, 0, wx.ALL, 5 )

		SSI_room_type_dropdownChoices = []
		self.SSI_room_type_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SSI_room_type_dropdownChoices, 0 )
		self.SSI_room_type_dropdown.SetSelection( 0 )
		self.SSI_room_type_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer34.Add( self.SSI_room_type_dropdown, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer34, 1, wx.EXPAND, 5 )

		self.SSI_search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.SSI_search_button, 0, wx.ALL, 5 )

		self.SSI_price_sort = wx.StaticText( self, wx.ID_ANY, u"Suburbs Sorted by Price:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SSI_price_sort.Wrap( -1 )

		self.SSI_price_sort.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer31.Add( self.SSI_price_sort, 0, wx.ALL, 5 )

		self.SSI_grid_price_sort = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(330, 400), 0)

		# Grid
		self.SSI_grid_price_sort.CreateGrid( 20, 2 )
		self.SSI_grid_price_sort.EnableEditing( True )
		self.SSI_grid_price_sort.EnableGridLines( True )
		self.SSI_grid_price_sort.EnableDragGridSize( False )
		self.SSI_grid_price_sort.SetMargins( 0, 0 )
		self.SSI_grid_price_sort.SetColSize(0, 150)

		# Columns
		self.SSI_grid_price_sort.EnableDragColMove( False )
		self.SSI_grid_price_sort.EnableDragColSize( True )
		self.SSI_grid_price_sort.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.SSI_grid_price_sort.EnableDragRowSize( True )
		self.SSI_grid_price_sort.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.SSI_grid_price_sort.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer31.Add( self.SSI_grid_price_sort, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.SSI_rating_sort = wx.StaticText( self, wx.ID_ANY, u"Suburbs Sorted by Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SSI_rating_sort.Wrap( -1 )

		self.SSI_rating_sort.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer32.Add( self.SSI_rating_sort, 0, wx.ALL, 5 )

		self.SSI_grid_rating_sort = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(330, 550), 0)

		# Grid
		self.SSI_grid_rating_sort.CreateGrid( 30, 2 )
		self.SSI_grid_rating_sort.EnableEditing( True )
		self.SSI_grid_rating_sort.EnableGridLines( True )
		self.SSI_grid_rating_sort.EnableDragGridSize( False )
		self.SSI_grid_rating_sort.SetMargins( 0, 0 )
		self.SSI_grid_rating_sort.SetColSize(0, 150)

		# Columns
		self.SSI_grid_rating_sort.EnableDragColMove( False )
		self.SSI_grid_rating_sort.EnableDragColSize( True )
		self.SSI_grid_rating_sort.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.SSI_grid_rating_sort.EnableDragRowSize( True )
		self.SSI_grid_rating_sort.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.SSI_grid_rating_sort.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer32.Add( self.SSI_grid_rating_sort, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer32, 1, wx.EXPAND, 5 )


		bSizer29.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer29 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


