import pandas as pd
import wx.grid


def run_keyword_search():
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
        "Driveway", "Car", "Van"
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


    def get_filter_for_keywords(keywords):
        pattern = '|'.join('(?<![a-zA-Z])' + keyword + '(?![a-zA-Z])' for keyword in keywords)
        return merged_data['comments'].str.contains(pattern, case=False, na=False, regex=True)


    cleanliness_filter = get_filter_for_keywords(cleanliness_keywords)
    pool_filter = get_filter_for_keywords(pool_keywords)
    parking_filter = get_filter_for_keywords(parking_keywords)
    wifi_filter = get_filter_for_keywords(wifi_keywords)
    air_conditioning_filter = get_filter_for_keywords(air_conditioning_keywords)

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

        def KS_Search(self, event):
            filtered_data = merged_data

            keyword = self.KS_keyword_text.GetValue()

            if keyword.strip():
                keyword_filter = merged_data['comments'].str.contains(keyword, case=False, na=False, regex=True)
                filtered_data = merged_data[keyword_filter]

            if self.KS_cleanliness_tick.IsChecked():
                filtered_data = filtered_data[cleanliness_filter]

            if self.KS_pool_tick.IsChecked():
                filtered_data = filtered_data[pool_filter]

            if self.KS_wifi_tick.IsChecked():
                filtered_data = filtered_data[wifi_filter]

            if self.KS_Parking_tick.IsChecked():
                filtered_data = filtered_data[parking_filter]

            if self.KS_ac_tick.IsChecked():
                filtered_data = filtered_data[air_conditioning_filter]

            self.KS_grid.DeleteRows(0, self.KS_grid.GetNumberRows(), True)
            self.KS_grid.AppendRows(len(filtered_data))

            for i, (index, row) in enumerate(filtered_data.iterrows()):

                self.KS_grid.SetCellValue(i, 0, str(row['name']))
                self.KS_grid.SetCellValue(i, 1, str(row['property_type']))
                self.KS_grid.SetCellValue(i, 2, str(row['bedrooms']))
                self.KS_grid.SetCellValue(i, 3, str(row['bathrooms']))
                self.KS_grid.SetCellValue(i, 4, str(row['accommodates']))
                self.KS_grid.SetCellValue(i, 5, str(row['review_scores_value']))
                self.KS_grid.SetCellValue(i, 6, str(row['price']))
                self.KS_grid.SetCellValue(i, 7, str(row['amenities']))
                self.KS_grid.SetCellValue(i, 8, str(row['comments']))
                self.KS_grid.SetCellValue(i, 9, str(row['host_is_superhost']))

    return CalcFrame()

