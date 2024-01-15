import pandas as pd 
from collections import Counter

members_df = pd.read_csv('membersClean.csv')
open_counts = {}
click_counts = {}
attendance_records = {}
# files
csv_open_files = ['aggregate_activity/aggregate_open/fall23_3.csv', 'aggregate_activity/aggregate_open/fall23_4_2.csv', 'aggregate_activity/aggregate_open/fall23_4.csv', 'aggregate_activity/aggregate_open/fall23_6.csv', 'aggregate_activity/aggregate_open/fall23_7.csv', 'aggregate_activity/aggregate_open/fall23_8.csv', 'aggregate_activity/aggregate_open/fall23_9_2.csv', 'aggregate_activity/aggregate_open/fall23_9.csv','aggregate_activity/aggregate_open/fall23_10.csv', 'aggregate_activity/aggregate_open/fall23_11.csv', 'aggregate_activity/aggregate_open/fall23_12.csv']
csv_click_files = ['aggregate_activity/aggregate_click/fall23_3.csv', 'aggregate_activity/aggregate_click/fall23_4_2.csv', 'aggregate_activity/aggregate_click/fall23_4.csv', 'aggregate_activity/aggregate_click/fall23_6.csv', 'aggregate_activity/aggregate_click/fall23_7.csv', 'aggregate_activity/aggregate_click/fall23_8.csv', 'aggregate_activity/aggregate_click/fall23_9_2.csv', 'aggregate_activity/aggregate_click/fall23_9.csv', 'aggregate_activity/aggregate_click/fall23_10.csv', 'aggregate_activity/aggregate_click/fall23_11.csv', 'aggregate_activity/aggregate_click/fall23_12.csv']
csv_attendance_files = ['events_attendance/fall23_careerPanel.csv', 'events_attendance/fall23_gbm1.csv', 'events_attendance/fall23_gbm2.csv', 'events_attendance/fall23_interviewPrep.csv', 'events_attendance/fall23_linkedinWksp.csv', 'events_attendance/fall23_resumeNight.csv', 'events_attendance/fall23_speeddating.csv', 'events_attendance/fall23_sqlWksp.csv']
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

print(open_counts)


# Email Clicks Using Dict
for file in csv_click_files:
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        email = row['BU Email']
        clicks = row['Clicks'] 
        click_counts[email] = click_counts.get(email, 0) + 1
print(click_counts)

# Event Attendance Update
for file in csv_attendance_files:
    df = pd.read_csv(file)
    for email in df['Email']:
        attendance_records[email] = attendance_records.get(email, 0) + 1

print(attendance_records)   
# Ratings Update
def update_rating(row):
    return open_counts.get(row['BU Email'], 0) + click_counts.get(row['BU Email'], 0)*2 + attendance_records.get(row['BU Email'], 0)*5

members_df['Rating'] = members_df.apply(update_rating, axis=1)

# Export csv
members_df.to_csv('updated_members_rating.csv', index=False)




