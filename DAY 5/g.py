import requests
from bs4 import BeautifulSoup

def scrape_flight_data(departure, arrival, date):
    # URL of the page containing the form
    url = "https://secure.flydanaair.com/Sched/schedule_popup.asp"
    
    # Form data to be sent with the POST request
    data = {
        "DeptCity": departure,
        "ArrCity": arrival,
        "deptdate": date
    }

    # Send a POST request with form data
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant information
        # Example:
        # flight_elements = soup.find_all('div', class_='flight-info')
        # for flight_element in flight_elements:
        #     flight_details = flight_element.find('div', class_='details').text.strip()
        #     print(flight_details)

        # Dummy output for demonstration
        print("Dummy flight data for", departure, "to", arrival, "on", date)
    else:
        print("Failed to retrieve data from the website")

# Collect user input
departure = input("Enter departure location: ")
arrival = input("Enter arrival location: ")
date = input("Enter date (YYYY-MM-DD): ")

# Scrape flight data based on user input
scrape_flight_data(departure, arrival, date)
