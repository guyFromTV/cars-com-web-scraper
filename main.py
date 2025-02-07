# Import necessary libraries
from bs4 import BeautifulSoup  # For parsing HTML
import requests  # For making HTTP requests
import pandas as pd  # For handling data in tabular format

# Initialize empty lists to store extracted data
name = []       
dealer = []
rating = []
reviews = []
price = []

# Loop through the first 10 pages of search results
for i in range(1, 11):

    # Construct the URL for each page
    website = 'https://www.cars.com/shopping/results/?makes[]=mercedes_benz&maximum_distance=all&models[]=&page=' + str(i) + '&stock_type=new&zip='

    # Define headers to mimic a real browser request and avoid getting blocked
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # Send an HTTP GET request to fetch the webpage
    response = requests.get(website, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all vehicle listings on the page
    cars = soup.find_all('div', {'class': 'vehicle-card'})

    # Extract information for each car listing
    for car in cars:
        try:
            # Extract car name (model)
            name.append(car.find('h2', {'class': 'title'}).get_text(strip=True))
        except:
            name.append("n/a")  # Append "n/a" if data is missing

        try:
            # Extract dealer name
            dealer.append(car.find('div', {'class': 'dealer-name'}).get_text(strip=True))
        except:
            dealer.append("n/a")

        try:
            # Extract rating (if available)
            rating.append(car.find('spark-rating').get('rating'))
        except:
            rating.append("n/a")

        try:
            # Extract number of reviews
            reviews.append(car.find('span', {'class': 'test1 sds-rating__link sds-button-link'}).get_text(strip=True))
        except:
            reviews.append("n/a")

        try:
            # Extract price of the car
            price.append(car.find('span', {'class': 'primary-price'}).get_text(strip=True))
        except:
            price.append("n/a")

# Create a DataFrame from the extracted data
cars_table = pd.DataFrame({
    'Name': name,
    'Dealer': dealer,
    'Rating': rating,
    'Reviews': reviews,
    'Price': price
}) 

# Clean the "Reviews" column by removing unwanted characters
cars_table['Reviews'] = cars_table['Reviews'].apply(lambda x: x.strip('reviews)').strip('('))

# Save the data to an Excel file
cars_table.to_excel('cars_dataset.xlsx', index=False)
