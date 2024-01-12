import pandas as pd 
from collections import Counter

members_df = pd.read_csv('membersClean.csv')
open_counts = Counter()
click_counts = {}
# files
csv_open_files = ['aggregate_activity/aggregate_open/fall23_3.csv', 'aggregate_activity/aggregate_open/fall23_4_2.csv', 'aggregate_activity/aggregate_open/fall23_4.csv', 'aggregate_activity/aggregate_open/fall23_6.csv', 'aggregate_activity/aggregate_open/fall23_7.csv', 'aggregate_activity/aggregate_open/fall23_8.csv', 'aggregate_activity/aggregate_open/fall23_9_2.csv', 'aggregate_activity/aggregate_open/fall23_9.csv','aggregate_activity/aggregate_open/fall23_10.csv', 'aggregate_activity/aggregate_open/fall23_11.csv', 'aggregate_activity/aggregate_open/fall23_12.csv']
csv_click_files = ['aggregate_activity/aggregate_click/fall23_3.csv', 'aggregate_activity/aggregate_click/fall23_4_2.csv', 'aggregate_activity/aggregate_click/fall23_4.csv', 'aggregate_activity/aggregate_click/fall23_6.csv', 'aggregate_activity/aggregate_click/fall23_7.csv', 'aggregate_activity/aggregate_click/fall23_8.csv', 'aggregate_activity/aggregate_click/fall23_9_2.csv', 'aggregate_activity/aggregate_click/fall23_9.csv', 'aggregate_activity/aggregate_click/fall23_10.csv', 'aggregate_activity/aggregate_click/fall23_11.csv', 'aggregate_activity/aggregate_click/fall23_12.csv']
# # Email Opens Counter (Doesnt work)
# for file in csv_files:
#     df = pd.read_csv(file)
#     email_counts.update(df['BU Email'].count())

# print(list(email_counts.items())[:10])

# Email Opens Using Dict
for file in csv_open_files:
    df = pd.read_csv(file)
    for email in df['BU Email']:
        open_counts[email] = open_counts.get(email, 0) + 1


# Email Clicks Using Dict
for file in csv_click_files:
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        email = row['BU Email']
        clicks = row['Clicks']  # Replace 'clicks' with the actual column name if different
        click_counts[email] = click_counts.get(email, 0) + clicks


# Email Opens Update
def update_rating(row):
    return open_counts.get(row['BU Email'], 0) + click_counts.get(row['BU Email'], 0)*3 + row['Rating']

members_df['Rating'] = members_df.apply(update_rating, axis=1)

# Export csv
members_df.to_csv('updated_members_total.csv', index=False)




