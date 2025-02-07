# Cars.com Web Scraper

A Python-based web scraper designed to extract data from [Cars.com](https://www.cars.com) listings, specifically focusing on Mercedes-Benz cars. The scraper collects key details about car listings, including car names, dealer names, ratings, reviews, and prices. The extracted data is saved in a structured Excel file for easy analysis.

## Features:
- Scrapes information about Mercedes-Benz cars from Cars.com.
- Extracts the following details:
  - Car model names
  - Dealer names
  - Car ratings (if available)
  - Number of reviews
  - Car prices
- Collects data from the first 10 pages of the search results.
- Saves the extracted data into an Excel file.

## Installation

### Prerequisites
Ensure that Python 3.x is installed on your system. You'll also need the following Python libraries:
- `requests` - For making HTTP requests to fetch web pages.
- `beautifulsoup4` - For parsing HTML content and extracting the required information.
- `pandas` - For managing and exporting the extracted data into a structured format (Excel).

### Setup
1. Clone the repository:

   ```bash
   git clone https://github.com/guyFromTV/cars-com-web-scraper.git


2. Navigate to the project directory:

   ```bash
   cd cars-com-web-scraper


3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'


4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt


5. To run the scraper, simply execute the script using Python:

   ```bash
   python main.py


This will start scraping the Cars.com listings for Mercedes-Benz cars. After the script runs, the extracted data will be saved in a file called cars_dataset.xlsx in the project directory.


## Output Format
The extracted data will be saved in an Excel file with the following columns:

- `Name`: The car model name.
- `Dealer`: The dealer's name.
- `Rating`: The car's rating.
- `Reviews`: The number of reviews.
- `Price`: The price of the car.
