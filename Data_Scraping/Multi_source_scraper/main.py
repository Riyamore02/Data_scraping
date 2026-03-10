import json

from scrapers.blog_scraper import scrape_blog
from scrapers.youtube_scraper import scrape_youtube
from scrapers.pubmed_scraper import scrape_pubmed


# Use scrape-friendly articles
blog_urls = [
    "https://towardsdatascience.com/what-is-machine-learning-4f87f4c3b7d1",
    "https://machinelearningmastery.com/what-is-deep-learning/",
    "https://www.analyticsvidhya.com/blog/2021/03/introduction-to-machine-learning/"
]

youtube_urls = [
    "https://www.youtube.com/watch?v=aircAruvnKk",
    "https://www.youtube.com/watch?v=7eh4d6sabA0"
]

pubmed_urls = [
    "https://pubmed.ncbi.nlm.nih.gov/31452104/"
]


blogs = []
youtube = []
pubmed = []


# Blog scraping
for url in blog_urls:

    result = scrape_blog(url)

    if result:
        blogs.append(result)


# YouTube scraping
for url in youtube_urls:

    try:
        youtube.append(scrape_youtube(url))
    except Exception as e:
        print("YouTube scraping failed:", url)


# PubMed scraping
for url in pubmed_urls:

    try:
        pubmed.append(scrape_pubmed(url))
    except Exception as e:
        print("PubMed scraping failed:", url)


# Save results

with open("scraped_data/blogs.json", "w") as f:
    json.dump(blogs, f, indent=4)

with open("scraped_data/youtube.json", "w") as f:
    json.dump(youtube, f, indent=4)

with open("scraped_data/pubmed.json", "w") as f:
    json.dump(pubmed, f, indent=4)


print("Scraping Completed Successfully")