# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1050,615 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.main_title = wx.StaticText( self, wx.ID_ANY, u"Sydney Airbnb Information Analysis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.main_title.Wrap( -1 )

		self.main_title.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer1.Add( self.main_title, 0, wx.ALL, 5 )

		top_selection = wx.BoxSizer( wx.HORIZONTAL )

		self.suburb_label = wx.StaticText( self, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.suburb_label.Wrap( -1 )

		self.suburb_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.suburb_label, 0, wx.ALL, 5 )

		self.suburb_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.suburb_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.suburb_text, 0, wx.ALL, 5 )

		self.date_label = wx.StaticText( self, wx.ID_ANY, u"Date Range: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_label.Wrap( -1 )

		self.date_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.date_label, 0, wx.ALL, 5 )

		self.date1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.date1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.date1, 0, wx.ALL, 5 )

		self.date_to = wx.StaticText( self, wx.ID_ANY, u"to", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_to.Wrap( -1 )

		self.date_to.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.date_to, 0, wx.ALL, 5 )

		self.date2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.date2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.date2, 0, wx.ALL, 5 )

		self.search_button = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		top_selection.Add( self.search_button, 0, wx.ALL, 5 )


		bSizer1.Add( top_selection, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		sort_by = wx.BoxSizer( wx.VERTICAL )

		self.sort_by_label = wx.StaticText( self, wx.ID_ANY, u"Sort by:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sort_by_label.Wrap( -1 )

		self.sort_by_label.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sort_by.Add( self.sort_by_label, 0, wx.ALL, 5 )

		self.price_range_label = wx.StaticText( self, wx.ID_ANY, u"Price Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_range_label.Wrap( -1 )

		self.price_range_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sort_by.Add( self.price_range_label, 0, wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.price_min_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_min_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.price_min_text, 0, wx.ALL, 5 )

		self.price_range_to = wx.StaticText( self, wx.ID_ANY, u"to", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_range_to.Wrap( -1 )

		self.price_range_to.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.price_range_to, 0, wx.ALL, 5 )

		self.price_max_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_max_text.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer7.Add( self.price_max_text, 0, wx.ALL, 5 )


		sort_by.Add( bSizer7, 1, wx.EXPAND, 5 )

		min_rating_box = wx.BoxSizer( wx.VERTICAL )

		self.min_rating_label = wx.StaticText( self, wx.ID_ANY, u"Min Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.min_rating_label.Wrap( -1 )

		self.min_rating_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		min_rating_box.Add( self.min_rating_label, 0, wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 2, 5, 0, 0 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox3 = wx.CheckBox( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox3, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox5, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox7, 0, wx.ALL, 5 )

		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox8.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox8, 0, wx.ALL, 5 )

		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox9.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox9, 0, wx.ALL, 5 )

		self.m_checkBox10 = wx.CheckBox( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox10.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer2.Add( self.m_checkBox10, 0, wx.ALL, 5 )


		min_rating_box.Add( gSizer2, 1, wx.EXPAND, 5 )


		sort_by.Add( min_rating_box, 1, wx.EXPAND, 5 )

		prop_room_type_box = wx.BoxSizer( wx.VERTICAL )

		self.property_type_label = wx.StaticText( self, wx.ID_ANY, u"Property Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.property_type_label.Wrap( -1 )

		self.property_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.property_type_label, 0, wx.ALL, 5 )

		property_type_dropdownChoices = []
		self.property_type_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, property_type_dropdownChoices, 0 )
		self.property_type_dropdown.SetSelection( 0 )
		self.property_type_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.property_type_dropdown, 0, wx.ALL, 5 )

		self.room_type_label = wx.StaticText( self, wx.ID_ANY, u"Room Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.room_type_label.Wrap( -1 )

		self.room_type_label.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.room_type_label, 0, wx.ALL, 5 )

		room_type_dropdownChoices = []
		self.room_type_dropdown = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, room_type_dropdownChoices, 0 )
		self.room_type_dropdown.SetSelection( 0 )
		self.room_type_dropdown.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.room_type_dropdown, 0, wx.ALL, 5 )

		self.apply_button = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apply_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.apply_button, 0, wx.ALL, 5 )

		self.more_label = wx.StaticText( self, wx.ID_ANY, u"More:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.more_label.Wrap( -1 )

		self.more_label.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.more_label, 0, wx.ALL, 5 )

		self.price_dist_chart_button = wx.Button( self, wx.ID_ANY, u"Price Distribution Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_dist_chart_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.price_dist_chart_button, 0, wx.ALL, 5 )

		self.keyword_search_button = wx.Button( self, wx.ID_ANY, u"Keyword Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.keyword_search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		prop_room_type_box.Add( self.keyword_search_button, 0, wx.ALL, 5 )


		sort_by.Add( prop_room_type_box, 1, wx.EXPAND, 5 )


		bSizer4.Add( sort_by, 1, wx.EXPAND, 5 )

		data_display = wx.BoxSizer( wx.VERTICAL )

		self.main_data_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.main_data_grid.CreateGrid( 22, 8 )
		self.main_data_grid.EnableEditing( True )
		self.main_data_grid.EnableGridLines( True )
		self.main_data_grid.EnableDragGridSize( False )
		self.main_data_grid.SetMargins( 0, 0 )

		# Columns
		self.main_data_grid.EnableDragColMove( False )
		self.main_data_grid.EnableDragColSize( True )
		self.main_data_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.main_data_grid.EnableDragRowSize( True )
		self.main_data_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.main_data_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		data_display.Add( self.main_data_grid, 0, wx.ALL, 5 )


		bSizer4.Add( data_display, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.price_customer_search_button = wx.Button( self, wx.ID_ANY, u"Don't know where to stay? Click here to view all suburbs sorted by price and customer ratings.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.price_customer_search_button.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer1.Add( self.price_customer_search_button, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.search_button.Bind( wx.EVT_BUTTON, self.mainSearch )
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox3.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox4.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox7.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox8.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox9.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.m_checkBox10.Bind( wx.EVT_CHECKBOX, self.min_rating_checkbox )
		self.apply_button.Bind( wx.EVT_BUTTON, self.mainApply )
		self.price_dist_chart_button.Bind( wx.EVT_BUTTON, self.priceDistSearch )
		self.keyword_search_button.Bind( wx.EVT_BUTTON, self.keywordSearch )
		self.price_customer_search_button.Bind( wx.EVT_BUTTON, self.priceCustSearch )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def mainSearch( self, event ):
		event.Skip()

	def min_rating_checkbox( self, event ):
		event.Skip()










	def mainApply( self, event ):
		event.Skip()

	def priceDistSearch( self, event ):
		event.Skip()

	def keywordSearch( self, event ):
		event.Skip()

	def priceCustSearch( self, event ):
		event.Skip()


