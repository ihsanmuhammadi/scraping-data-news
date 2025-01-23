from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_news():
    url = "https://www.kompas.com"
    # Send a GET request to the website and store the response
    response = requests.get(url)
    # Parse the response content
    element = BeautifulSoup(response.content, "html.parser")
    # Find all news elements on the page by their container class
    many_news = element.find_all("div", class_="wSpec-box")

    data = []
    for news in many_news:
        # Extract the title, subtitle, and time
        title = news.find("h4", class_="wSpec-title")
        subtitle = news.find("p", class_="wSpec-subtitle")
        postTime = news.find("span")
        
        # Use .text and strip() to clean up extracted text and handle missing elements safely
        title_text = title.text.strip() if title else "N/A" 
        theme = subtitle.contents[0].strip() if subtitle and subtitle.contents else "N/A"
        post_time_text = postTime.text.strip() if postTime else "N/A"
        
        # Append the extracted data as a dictionary, ensuring column names align
        data.append({
            "Title": title_text,
            "Theme": theme,
            "Posting time": post_time_text
        })

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('news.csv', index=False)

    print('Saved to news.csv')

scrape_news()
