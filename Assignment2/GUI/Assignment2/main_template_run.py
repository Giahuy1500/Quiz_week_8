import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd

# Print the column names for debugging purposes
df = pd.read_csv(r".\listings_dec18.csv")

# Replace 'your_module_name' with your actual module name
from main_template import MyFrame1

# Create a wx.App instance
app = wx.App()

# Create an instance of your main frame
frame = MyFrame1(None)
frame.Show()

# Start the main event loop
app.MainLoop()
