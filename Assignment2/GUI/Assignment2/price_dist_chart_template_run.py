import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
import pandas as pd

data = pd.read_csv('listings_dec18.csv')

data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)
price_data = data['price'].unique()
price_data.sort()

suburb_data = data['city']
suburb_data_dropdown = data['city'].astype(str).unique()
suburb_data_dropdown = [x.strip() for x in suburb_data_dropdown]
suburb_data_dropdown.sort()

property_data = data['property_type']
property_data_dropdown = data['property_type'].unique()

room_data = data['room_type']
room_data_dropdown = data['room_type'].unique()

from price_dist_chart_template import MyFrame3 as MyFrame1

class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.PDC_property_dropdown.SetItems(property_data_dropdown)
        self.PDC_room_dropdown.SetItems(room_data_dropdown)
        self.PDC_suburb_dropdown.SetItems(suburb_data_dropdown)

        self.figure_score = Figure()
        self.axes = self.figure_score.add_subplot(111)
        self.canvas = FigureCanvasWxAgg(self.PDC_graph, -1, self.figure_score)
        self.canvas.Hide()  # Initially hide the canvas

        self.Layout()
        self.Show(True)

        self.Bind(wx.EVT_CHOICE, self.on_property_type_choice, self.PDC_property_dropdown)
        self.Bind(wx.EVT_CHOICE, self.on_room_type_choice, self.PDC_room_dropdown)
        self.Bind(wx.EVT_CHOICE, self.on_suburb_choice, self.PDC_suburb_dropdown)

        # track if a filter has changed
        self.filter_changed = False

    def PDC_search(self, event):
        if self.filter_changed:
            self.plot_data_line()
            self.filter_changed = False

    def on_property_type_choice(self, event):
        self.filter_changed = True

    def on_room_type_choice(self, event):
        self.filter_changed = True

    def on_suburb_choice(self, event):
        self.filter_changed = True

    def plot_data_line(self):
        selected_property = self.PDC_property_dropdown.GetStringSelection()
        selected_room = self.PDC_room_dropdown.GetStringSelection()
        selected_suburb = self.PDC_suburb_dropdown.GetStringSelection()

        filtered_data = data[(data['property_type'] == selected_property) & (data['room_type'] == selected_room) & (data['city'] == selected_suburb)]

        self.axes.clear()  # Clear previous plot
        x_series = pd.Series(filtered_data['price'])
        self.axes.bar(range(len(x_series)), x_series)
        self.axes.set_title(f'Price Distribution for {selected_property}s in {selected_suburb} ({selected_room})')
        self.axes.set_ylabel('Price')
        self.axes.set_xlabel('No. of Listings')

        # Refresh the canvas
        self.canvas.draw_idle()
        self.canvas.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame()
    app.MainLoop()
