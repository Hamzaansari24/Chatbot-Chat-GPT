import requests
from bs4 import BeautifulSoup
import openai

# Set up ChatGPT API credentials
openai.api_key = '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'

# Fetch the website content
def fetch_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Extract relevant information from the website using web scraping
def extract_information(html_content):
    # Use Beautiful Soup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract relevant information from the parsed content
    # Customize this based on the structure of the website and the information you want to extract

    # Example: Extract the title of the website
    title = soup.title.text.strip()

    # Example: Extract the paragraph text from a specific element with a given class
    div_element = soup.find('div', class_='my-class')
    paragraph = div_element.p.text.strip() if div_element else ""

    # Example: Extract a list of items from an ordered or unordered list
    ul_elements = soup.find_all('ul')
    items = [li.text.strip() for ul in ul_elements for li in ul.find_all('li')]

    # Combine the extracted information into suitable format
    extracted_info = f"Title: {title}\nParagraph: {paragraph}\nItems: {items}"

    return extracted_info


# Generate a response using the ChatGPT API
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# function to interact with the chatbot
def chat_with_bot():
    # website URL
    website_url = 'https://botpenguin.com/'

    # Fetch the website content
    html_content = fetch_website_content(website_url)

    if html_content:
        # Extract relevant information from the website
        extracted_info = extract_information(html_content)

        while True:
            # Get user input
            user_input = input('User: ')

            # Process user input and combine with extracted information
            prompt = f'User: {user_input}\nWebsite Info: {extracted_info}\nBot:'

            # Generate a response using the ChatGPT API
            bot_response = generate_response(prompt)

            # Print the bot's response
            print('Bot:', bot_response)

            # Break the loop if the conversation ends
            if 'Goodbye' in bot_response:
                break
    else:
        print('Failed to fetch website content.')

# Run the chatbot
chat_with_bot()
