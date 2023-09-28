import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd

# Replace 'your_module_name' with your actual module name
from suburb_specific_template import MyFrame5 as MyFrame1

# Create a wx.App instance
app = wx.App()

# Create an instance of your main frame
frame = MyFrame1(None)
frame.Show()

# Start the main event loop
app.MainLoop()
