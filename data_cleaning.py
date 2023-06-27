#Code to generate data for bubble plot of trash types
import pandas as pd
data = pd.read_csv('Onyx Data DataDNA Dataset Challenge - July 2023/Onyx Data DataDNA Dataset Challenge - July 2023.csv')
data.columns

#clean column names
col_dict = {'Food Wrappers (candy, chips, etc.)': 'Food Wrappers',
            'Lids (Plastic)': 'Lids', 
            'Rope (1 yard/meter = 1 piece)': 'Rope', 
            'Other Plastic Bottles (oil, bleach, etc.)': 'Other Plastic Bottles',
            'Other Packaging (Clean Swell)': 'Other Packaging',
            'Appliances (refrigerators, washers, etc.)': 'Appliances',
            'Other Trash (Clean Swell)': 'Other Trash',
            'Personal Hygiene (Clean Swell)': 'Personal Hygiene'}
data.rename(columns=col_dict, inplace=True)

#aggregate columns of same type
data['Take Out Containers'] = data['Take Out/Away Containers (Plastic)'] + data['Take Out/Away Containers (Foam)']
data['Bottle Caps'] = data['Bottle Caps (Plastic)'] + data['Bottle Caps (Metal)']
data['Beverage Bottles'] = data['Beverage Bottles (Plastic)'] + data['Beverage Bottles (Glass)']
data['Plastic Bags'] = data['Grocery Bags (Plastic)'] + data['Other Plastic Bags']
data['Cups, Plates'] = data['Cups, Plates (Paper)'] + data['Cups, Plates (Plastic)'] + data['Cups, Plates (Foam)']
data['Fishing Gear'] = data['Fishing Buoys, Pots & Traps'] + data['Fishing Net & Pieces'] + data['Fishing Line (1 yard/meter = 1 piece)'] + data['Fishing Gear (Clean Swell)']

#subset data for columns of interest
data_for_plot = data[['State', 'Cigarette Butts',
                       'Food Wrappers', 'Lids', 'Straws, Stirrers', 
                       'Forks, Knives, Spoons', 'Beverage Cans', 'Paper Bags', 'Rope', '6-Pack Holders', 
                       'Other Plastic/Foam Packaging', 'Other Plastic Bottles', 
                       'Strapping Bands', 'Tobacco Packaging/Wrap', 'Other Packaging', 
                       'Appliances', 'Balloons', 'Cigar Tips', 'Cigarette Lighters',
                       'Construction Materials', 'Fireworks', 'Tires', 'Toys', 'Other Trash', 
                       'Condoms', 'Diapers', 'Syringes', 'Tampons/Tampon Applicators', 
                       'Personal Hygiene', 'Foam Pieces', 'Glass Pieces', 'Plastic Pieces']]
#aggregate trash by state
data_for_plot = data_for_plot.groupby('State').sum()

#transpose so trash type in row and state is column
data_for_plot = data_for_plot.transpose()

#remove cols that are not states
data_for_plot.drop(columns=['Ontario, Canada', 'United States'], axis=1, inplace=True)

#total trash type across all states
data_for_plot['Total'] = data_for_plot[data_for_plot.columns].sum(axis=1)

#export
data_for_plot.to_csv('trash_categories.csv')

