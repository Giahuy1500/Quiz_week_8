import pandas as pd
import wx.grid

review_data = pd.read_csv('reviews_dec18.csv')
listing_data = pd.read_csv('listings_dec18.csv')

merged_data = pd.merge(listing_data, review_data[['listing_id', 'comments']], left_on='id', right_on='listing_id', how='inner')

name = merged_data['name']
property_type = merged_data['property_type']
bedrooms = merged_data['bedrooms']
bathrooms = merged_data['bathrooms']
occupants = merged_data['accommodates']
rating = merged_data['review_scores_value']
price = merged_data['price'].str.replace('$', '').str.replace(',', '').astype(float)
amenities = merged_data['amenities'].str.replace('{', '').str.replace(',', ', ').str.replace('"', '')
reviews = merged_data['comments']  # Now includes comments from review_data
superhost = merged_data['host_is_superhost']

print(merged_data)

# Keywords for cleanliness
cleanliness_keywords = [
    "Clean", "Cleanliness", "Hygiene", "Tidy", "Tidiness", "Sanitary", "Neat",
    "Spotless", "Well-kept", "Dust", "Dirty", "Cleaned", "Unclean", "Dusty",
    "Unsanitary", "Messy", "Filthy", "Disgusting", "Shiny", "New"
]

# Keywords for pool
pool_keywords = [
    "Pool", "Swim", "Swimming", "Spa", "Jacuzzi"
]

# Keywords for parking
parking_keywords = [
    "Parking", "Garage", "Carport", "Vehicle", "Bike", "Automobile", "Parked",
    "Driveway", "Car", "Van", "Bus"
]

# Keywords for Wi-Fi
wifi_keywords = [
    "WiFi", "Wi-Fi", "Internet", "WLAN", "Wireless", "Network", "Online",
    "Web", "NBN", "Broadband", "Hotspot"
]

# Keywords for air conditioning
air_conditioning_keywords = [
    "Air conditioning", "Aircon", "AC", "A/C", "Heating", "Cooling", "Fans",
    "Cold", "Hot", "Temperature", "Climate", "Air"
]

from keyword_template import MyFrame4 as MyFrame1

class CalcFrame(MyFrame1):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Column labels
        self.KS_grid.SetColLabelValue(0, "Name")
        self.KS_grid.SetColLabelValue(1, "Property Type")
        self.KS_grid.SetColLabelValue(2, "Bedrooms")
        self.KS_grid.SetColLabelValue(3, "Bathrooms")
        self.KS_grid.SetColLabelValue(4, "Occupants")
        self.KS_grid.SetColLabelValue(5, "Rating")
        self.KS_grid.SetColLabelValue(6, "Price")
        self.KS_grid.SetColLabelValue(7, "Amenities")
        self.KS_grid.SetColLabelValue(8, "Reviews")
        self.KS_grid.SetColLabelValue(9, "Superhost")


if __name__ == "__main__":
    app = wx.App(False)
    frame = CalcFrame()
    frame.Show()
    app.MainLoop()
