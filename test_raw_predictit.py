# Import the necessary libraries
import json
import requests
import boto3

# Define a function to scrape JSON data from a URL and save it to a file
def json_scraper(url, file_name, bucket) :
    # Print a message to indicate the function has started running
    print("start running")
    # Send a GET request to the provided URL
    response = requests.get(url)
    # Parse the response as JSON
    data = response.json()
    
    # Open the provided file in write mode
    with open(file_name, 'w', encoding='utf-8') as json_file:
        # Dump the JSON data into the file, formatted with an indent of 4 spaces
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    # Print a message to indicate the function has finished running
    print("finished running")
    
    # Create a boto3 client for S3
    # s3 = boto3.client('s3')
    
    # # Upload the file to the provided S3 bucket
    # s3.upload_file(file_name, bucket, file_name)

# Call the function with a specific URL, file name, and S3 bucket
json_scraper('https://www.predictit.org/api/marketdata/all', 'predictit_market.json', 'data-mbfr')
