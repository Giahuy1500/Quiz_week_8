import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd
import subprocess

listing_data = pd.read_csv('listings_dec18.csv')

name = listing_data['name']
property_type = listing_data['property_type']
bedrooms = listing_data['bedrooms']
bathrooms = listing_data['bathrooms']
occupants = listing_data['accommodates']
rating = listing_data['review_scores_value']
price = listing_data['price'].str.replace('$', '').str.replace(',', '').astype(float)
superhost = listing_data['host_is_superhost']

from main_template import MyFrame1


class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Bind the event handler for the price_dist_chart_button
        self.price_dist_chart_button.Bind(wx.EVT_BUTTON, self.priceDistSearch)
        self.keyword_search_button.Bind(wx.EVT_BUTTON, self.keywordSearch)
        self.price_customer_search_button.Bind(wx.EVT_BUTTON, self.priceCustSearch)

    def priceDistSearch(self, event):
        script_to_run = "price_dist_chart_template_run.py"
        try:
            subprocess.run(["python", script_to_run], check=True)
        except subprocess.CalledProcessError as e:
            wx.MessageBox("Error running the script.", "Error", wx.OK | wx.ICON_ERROR)

    def keywordSearch( self, event ):
        script_to_run = "keyword_template_run.py"
        try:
            subprocess.run(["python", script_to_run], check=True)
        except subprocess.CalledProcessError as e:
            wx.MessageBox("Error running the script.", "Error", wx.OK | wx.ICON_ERROR)

    def priceCustSearch( self, event ):
        script_to_run = "suburb_specific_run.py"
        try:
            subprocess.run(["python", script_to_run], check=True)
        except subprocess.CalledProcessError as e:
            wx.MessageBox("Error running the script.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
