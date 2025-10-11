# The program print out the dates of the bank holidays that happen in northern Ireland.
# Author:Joanna Mnich


import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# All events in UK
eng_wales_events = {event['title'] for event in data['england-and-wales']['events']}
scotland_events = {event['title'] for event in data['scotland']['events']}
other_regions = eng_wales_events.union(scotland_events)

# Only Northern Ireland
ni_events = data['northern-ireland']['events']

# Events only exist in Northern Ireland
unique_ni_events = [event for event in ni_events if event['title'] not in other_regions]
for event in unique_ni_events:
    print(f"{event['date']}: {event['title']}")

