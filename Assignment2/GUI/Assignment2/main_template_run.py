import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd

from price_dist_chart_template_run import run_price_distribution_chart
from keyword_template_run import run_keyword_search
from suburb_specific_run import run_suburb_rating
from main_template import MyFrame1


listing_data = pd.read_csv('listings_dec18.csv')
calendar_data = pd.read_csv('calendar_dec18.csv')

name = listing_data['name']
property_type = listing_data['property_type']
bedrooms = listing_data['bedrooms']
bathrooms = listing_data['bathrooms']
occupants = listing_data['accommodates']
rating = listing_data['review_scores_value']
price = listing_data['price'].str.replace('$', '').str.replace(',', '').astype(float)
superhost = listing_data['host_is_superhost']

property_data = listing_data['property_type']
property_data_dropdown = listing_data['property_type'].unique()

room_data = listing_data['room_type']
room_data_dropdown = listing_data['room_type'].unique()


class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        # label columns
        self.main_data_grid.SetColLabelValue(0, "Name")
        self.main_data_grid.SetColLabelValue(1, "Property Type")
        self.main_data_grid.SetColLabelValue(2, "room Type")
        self.main_data_grid.SetColLabelValue(3, "Bedrooms")
        self.main_data_grid.SetColLabelValue(4, "Bathrooms")
        self.main_data_grid.SetColLabelValue(5, "Occupants")
        self.main_data_grid.SetColLabelValue(6, "Rating")
        self.main_data_grid.SetColLabelValue(7, "Price")

        self.property_type_dropdown.SetItems(property_data_dropdown)
        self.room_type_dropdown.SetItems(room_data_dropdown)

        self.filtered_data = pd.DataFrame(listing_data)
        self.search_button.Bind(wx.EVT_BUTTON, self.perform_search)
        self.apply_button.Bind(wx.EVT_BUTTON, self.applyFilters)

        self.price_dist_chart_button.Bind(wx.EVT_BUTTON, self.priceDistSearch)
        self.keyword_search_button.Bind(wx.EVT_BUTTON, self.keywordSearch)
        self.price_customer_search_button.Bind(wx.EVT_BUTTON, self.priceCustSearch)

    def perform_search(self, event):
        suburb = self.suburb_text.GetValue().strip().title()
        suburb = suburb.replace(',', '')

        start_date = self.date1.GetValue().FormatISODate()
        end_date = self.date2.GetValue().FormatISODate()

        filtered_listing_data = listing_data[listing_data['city'].str.strip().str.title() == suburb]

        # Use the filtered listings Ids to filter the calendar data:
        filtered_ids = filtered_listing_data['id'].values
        filtered_date_data = calendar_data[calendar_data['listing_id'].isin(filtered_ids)]

        # Filter the calendar data by the availability
        filtered_date_data = filtered_date_data[
            (filtered_date_data['available'] == 't') &
            (filtered_date_data['date'] >= start_date) &
            (filtered_date_data['date'] <= end_date)
            ]

        # Extract the listing IDs from the filtered calendar data:
        final_filtered_ids = filtered_date_data['listing_id'].unique()

        # Filter the listing_data again
        final_filtered_listing_data = listing_data[listing_data['id'].isin(final_filtered_ids)]

        # Use final_filtered_listing_data to populate the grid
        self.filtered_data = final_filtered_listing_data

        # Clear the grid
        self.main_data_grid.ClearGrid()

        # Define the columns in the grid
        columns_to_display = [
            'name', 'property_type', 'room_type', 'bedrooms', 'bathrooms', 'accommodates',
            'review_scores_value', 'price',
        ]

        self.populate_data_grid(self.filtered_data, columns_to_display)

    def applyFilters(self, event):
        suburb = self.suburb_text.GetValue().strip().title()
        suburb = suburb.replace(',', '')

        # get $ values, ensure they are numeric and create maximum limits if empty
        price_min_str = self.price_min_text.GetValue()
        price_max_str = self.price_max_text.GetValue()

        try:
            price_min = float(price_min_str) if price_min_str else float('-inf')
            price_max = float(price_max_str) if price_max_str else float('inf')
        except ValueError:
            wx.MessageBox("Invalid price range. Please enter numeric values.", "Error", wx.OK | wx.ICON_ERROR)
            return

        # Create a copy of the DataFrame to avoid the warning
        filtered_data = self.filtered_data.copy(deep=True)
        filtered_data = filtered_data[filtered_data['city'].str.strip().str.title() == suburb]

        # turn the price data back into a float
        filtered_data['price'] = filtered_data['price'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
        filtered_data = filtered_data[(filtered_data['price'] >= price_min) & (filtered_data['price'] <= price_max)]

        # define min rating and determine value depending on checkbox
        min_rating = []

        for checkbox in [self.m_checkBox1, self.m_checkBox2, self.m_checkBox3,
                         self.m_checkBox4, self.m_checkBox5, self.m_checkBox6,
                         self.m_checkBox7, self.m_checkBox8, self.m_checkBox9,
                         self.m_checkBox10]:
            if checkbox.GetValue():
                min_rating.append(int(checkbox.GetLabel()))

        # determine dropdown selections
        selected_property_type = self.property_type_dropdown.GetStringSelection()
        selected_room_type = self.room_type_dropdown.GetStringSelection()

        # filter for minimum rating, and ensure room type and property type are selected
        if min_rating:
            min_selected_rating = min(min_rating)
            filtered_data = filtered_data[filtered_data['review_scores_value'] >= min_selected_rating]
        if selected_property_type and selected_property_type != 'All':
            filtered_data = filtered_data[filtered_data['property_type'] == selected_property_type]
        if selected_room_type and selected_room_type != 'All':
            filtered_data = filtered_data[filtered_data['room_type'] == selected_room_type]

        columns_to_display = [
            'name', 'property_type', 'room_type', 'bedrooms', 'bathrooms', 'accommodates', 'review_scores_value',
            'price',
        ]

        self.populate_data_grid(filtered_data, columns_to_display)

    def populate_data_grid(self, filtered_data, columns_to_display):
        # Clear existing grid data
        self.main_data_grid.ClearGrid()

        # Check if there are any rows in the filtered data
        if len(filtered_data) == 0:
            return

        # Set the number of rows in the grid to match the number of filtered data rows
        num_rows = len(filtered_data)
        self.main_data_grid.DeleteRows(numRows=self.main_data_grid.GetNumberRows())
        self.main_data_grid.AppendRows(num_rows)

        # Populate grid rows with data from the filtered DataFrame
        for row_index, (_, row_data) in enumerate(filtered_data.iterrows()):
            for col_index, col_name in enumerate(columns_to_display):
                value = str(row_data[col_name])
                self.main_data_grid.SetCellValue(row_index, col_index, value)

    def priceDistSearch(self, event):
        try:
            run_price_distribution_chart()
            frame.Show()
        except Exception as e:
            wx.MessageBox(f"Error: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def keywordSearch(self, event):
        try:
            run_keyword_search()
            frame.Show()
        except Exception as e:
            wx.MessageBox(f"Error: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)

    def priceCustSearch(self, event):
        try:
            run_suburb_rating()
            frame.Show()
        except Exception as e:
            wx.MessageBox(f"Error: {str(e)}", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
