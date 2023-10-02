import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd

def run_suburb_rating():
    data = pd.read_csv('listings_dec18.csv')

    # Clean up data (commas, Sydney, NSW, etc.)
    data['city'] = data['city'].str.strip()
    data['city'] = data['city'].str.replace(',', '').str.replace(' Sydney', '').str.replace(' New South Wales AU', '').str.replace(' NSW', '')
    data['city'] = data['city'].str.lower().str.title()
    suburb_data = data['city'].astype(str).unique()

    data['price'] = data['price'].str.replace('$', '').str.replace(',', '').astype(float)
    price_data = data['price'].unique()
    price_data.sort()

    property_data = data['property_type']
    property_data_dropdown = data['property_type'].unique()

    room_data = data['room_type']
    room_data_dropdown = data['room_type'].unique()

    rating_data = data['review_scores_value']

    from suburb_specific_template import MyFrame5 as MyFrame1

    class CalcFrame(MyFrame1):
        def __init__(self, parent=None):
            super().__init__(parent)

            self.SSI_property_type_dropdown.SetItems(property_data_dropdown)
            self.SSI_room_type_dropdown.SetItems(room_data_dropdown)

            self.Layout()
            self.Show(True)

            self.Bind(wx.EVT_CHOICE, self.on_property_type_choice, self.SSI_property_type_dropdown)
            self.Bind(wx.EVT_CHOICE, self.on_room_type_choice, self.SSI_room_type_dropdown)
            self.Bind(wx.EVT_BUTTON, self.on_search_button_click, self.SSI_search_button)

            # Column labels
            self.SSI_grid_price_sort.SetColLabelValue(0, "Suburb")
            self.SSI_grid_price_sort.SetColLabelValue(1, "Avg Price")

            self.SSI_grid_rating_sort.SetColLabelValue(0, "Suburb")
            self.SSI_grid_rating_sort.SetColLabelValue(1, "Avg Rating")

        def on_property_type_choice(self, event):
            self.filter_changed = True

        def on_room_type_choice(self, event):
            self.filter_changed = True

        def calculate_average_prices(self, property_type, room_type):
            filtered_data = data[(data['property_type'] == property_type) & (data['room_type'] == room_type)]

            # Calculate average price for each suburb
            avg_prices = filtered_data.groupby('city')['price'].mean().reset_index()

            return avg_prices

        def calculate_average_rating(self, property_type, room_type):
            filtered_data = data[(data['property_type'] == property_type) & (data['room_type'] == room_type)]

            # Calculate average rating for each suburb
            avg_ratings = filtered_data.groupby('city')['review_scores_value'].mean().reset_index()

            return avg_ratings

        def on_search_button_click(self, event):
            property_type = self.SSI_property_type_dropdown.GetStringSelection()
            room_type = self.SSI_room_type_dropdown.GetStringSelection()

            if property_type and room_type:
                avg_prices = self.calculate_average_prices(property_type, room_type)
                avg_ratings = self.calculate_average_rating(property_type, room_type)

                # Populate the grids
                self.populate_price_grid(avg_prices)
                self.populate_rating_grid(avg_ratings)

        def populate_price_grid(self, avg_prices):
            # Clear existing grid data
            self.SSI_grid_price_sort.ClearGrid()

            # Set the number of rows in the grid to match the number of suburbs
            num_suburbs = len(avg_prices)
            self.SSI_grid_price_sort.DeleteRows(numRows=self.SSI_grid_price_sort.GetNumberRows())
            self.SSI_grid_price_sort.AppendRows(num_suburbs)

            # Populate grid rows with suburb and average price data
            for index, row in avg_prices.iterrows():
                self.SSI_grid_price_sort.SetCellValue(index, 0, row['city'])
                self.SSI_grid_price_sort.SetCellValue(index, 1, str(round(row['price'], 2)))

        def populate_rating_grid(self, avg_ratings):
            self.SSI_grid_rating_sort.ClearGrid()

            # Set the number of rows in the grid to match the number of suburbs
            num_suburbs = len(avg_ratings)
            self.SSI_grid_rating_sort.DeleteRows(numRows=self.SSI_grid_rating_sort.GetNumberRows())
            self.SSI_grid_rating_sort.AppendRows(num_suburbs)

            # Populate grid rows with suburb and average rating data
            for index, row in avg_ratings.iterrows():
                self.SSI_grid_rating_sort.SetCellValue(index, 0, row['city'])
                self.SSI_grid_rating_sort.SetCellValue(index, 1, str(round(row['review_scores_value'], 2)))

    return CalcFrame()