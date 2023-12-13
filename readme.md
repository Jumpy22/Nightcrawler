
![Logo](https://i.imgur.com/znY8NN5.png)

# Nightcrawler

Nightcrawler is a Python script designed for web crawling and extracting links from a given webpage up to a specified depth.

## Description

Nightcrawler utilizes `requests`, `BeautifulSoup`, `fake_useragent`, and `urllib` Python libraries to traverse through web pages and collect links. It allows users to specify the URL and the depth of the crawl either via command-line arguments or interactive prompts.

Current pentesting features include sorting urls that have parameters to a seperate text file. (That's it for right now)

## Requirements

- Python 3.x
- Install required packages using `pip install -r requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jumpy22/Nightcrawler.git
   cd Nightcrawler
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Launch (CMDLINE/INTERACTIVE)**

    ```bash
    python nightcrawler.py
    OR
    python nightcrawler.py <URL> <depth>
    ```

## Eclipse

Eclipse takes a list of URLs from a text file, then initiates a multi-threaded web crawling process (using the 'nightcrawler.py' script) to scan those URLs at a specified depth, utilizing the specified number of threads for concurrent processing.

    ```bash
    python eclipse.py
    ```