import requests
from bs4 import BeautifulSoup

from utils import detect_language, extract_topics, chunk_content
from trust_score import compute_trust_score


def scrape_pubmed(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.find("h1").get_text()

    abstract_tag = soup.find("div", class_="abstract")

    abstract = ""

    if abstract_tag:
        abstract = abstract_tag.get_text()

    authors = soup.find_all("a", class_="full-name")

    author_names = [a.get_text() for a in authors]

    text = title + " " + abstract

    language = detect_language(text)

    topics = extract_topics(text)

    chunks = chunk_content(text)

    trust = compute_trust_score(
        url,
        author_names,
        "pubmed",
        None,
        text
    )

    data = {
        "source_url": url,
        "source_type": "pubmed",
        "author": ", ".join(author_names),
        "published_date": "Unknown",
        "language": language,
        "region": "Global",
        "topic_tags": topics,
        "trust_score": trust,
        "content_chunks": chunks
    }

    return data