# The program prints out the dates of the bank holidays that happen in Northern Ireland.
# Author:Joanna Mnich
# https://www.w3schools.com/PYTHON/ref_requests_get.asp
# https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content

import requests # To make HTTP requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url) # Make a GET request to the URL    
data = response.json() # Analyse the JSON response

# All events in the UK
eng_wales_events = {event['title'] for event in data['england-and-wales']['events']} # Set comprehension to get titles
scotland_events = {event['title'] for event in data['scotland']['events']}
other_regions = eng_wales_events.union(scotland_events) # Combine titles from other regions

# Only Northern Ireland
ni_events = data['northern-ireland']['events'] # List of events in Northern Ireland

# Events only exist in Northern Ireland
unique_ni_events = [event for event in ni_events if event['title'] not in other_regions] # List comprehension to filter unique events
# Print unique events
for event in unique_ni_events: # Loop through unique events
    print(f"{event['date']}: {event['title']}")

