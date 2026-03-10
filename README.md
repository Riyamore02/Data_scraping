Multi-Source Web Scraper with Trust Score System

Overview

This project implements a multi-source web scraping system that extracts structured information from different types of online sources and evaluates their reliability using a Trust Score Algorithm.

The system collects metadata and content from:

- Blog articles
- YouTube videos
- PubMed research articles

The extracted data is processed, analyzed, and stored in structured JSON format for further analysis.

---

Features

Multi-Source Data Extraction

The scraper collects structured content from three types of sources:

1. Blog Posts

- Article text
- Author
- Publication date
- Metadata
- Cleaned article content

2. YouTube Videos

- Channel name
- Video description
- Transcript (if available)
- Video metadata

3. PubMed Research Articles

- Article title
- Authors
- Abstract
- Journal information
- Publication year

---

Trust Score System

The project includes a Trust Score Algorithm that estimates the credibility of each source.

The trust score ranges from:

0 → Unreliable source
1 → Highly reliable source

Trust Score Formula

Trust Score is calculated using the following weighted factors:

Trust Score =
0.25 × Author Credibility

+ 0.20 × Citation Count
+ 0.20 × Domain Authority
+ 0.20 × Recency
+ 0.15 × Medical Disclaimer Presence

---

Trust Score Factors

Author Credibility

Evaluates the reliability of the author.

- Known experts receive higher scores
- Unknown authors receive lower scores
- Multiple authors are averaged

---

Citation Count

Evaluates if the content references scientific or credible information.

- PubMed articles receive higher citation scores
- Blogs receive moderate scores
- YouTube receives lower citation weight

---

Domain Authority

Evaluates the credibility of the source domain.

Examples:

Domain| Authority Score
PubMed| 0.98
WHO| 0.97
CDC| 0.97
TowardsDataScience| 0.75
Unknown blogs| 0.40

---

Recency

More recent content receives higher scores.

Age of Article| Score
≤1 year| 1.0
≤3 years| 0.8
≤5 years| 0.6
>5 years| 0.3

---

Medical Disclaimer Detection

The system checks for keywords like:

- "medical advice"
- "consult a doctor"
- "healthcare professional"

Presence of these keywords increases credibility.

---

Abuse Prevention Logic

The system prevents manipulation using several safeguards:

Fake Authors

Author names are checked against a list of known credible experts.

---

SEO Spam Blogs

Unknown or low-authority domains receive a domain penalty.

---

Misleading Medical Content

Articles without medical disclaimers receive lower credibility.

---

Outdated Information

Older content is penalized through the recency factor.

---

Content Processing Pipeline

The system processes content in several steps:

1. Web scraping
2. Metadata extraction
3. Language detection
4. Topic keyword extraction
5. Content chunking
6. Trust score calculation
7. JSON data storage

---

Project Structure

Multi_source_scraper
│
├── main.py
├── utils.py
├── trust_score.py
├── requirements.txt
│
├── scrapers
│   ├── __init__.py
│   ├── blog_scraper.py
│   ├── youtube_scraper.py
│   └── pubmed_scraper.py
│
└── scraped_data
    ├── blogs.json
    ├── youtube.json
    └── pubmed.json

---

Installation

Install required libraries:

pip install -r requirements.txt

If required:

pip install lxml_html_clean

---

Running the Project

Navigate to the project folder:

cd Multi_source_scraper

Run the scraper:

python main.py

---

Output

The system generates structured JSON files:

scraped_data/

Files created:

- blogs.json
- youtube.json
- pubmed.json

Example output:

{
 "source_url": "...",
 "source_type": "blog",
 "author": ["Author Name"],
 "published_date": "2023-08-10",
 "language": "en",
 "region": "Global",
 "topic_tags": ["machine learning", "AI"],
 "trust_score": 0.78,
 "content_chunks": [...]
}

---

Technologies Used

- Python
- BeautifulSoup
- Newspaper3k
- YouTube Transcript API
- LangDetect
- YAKE Keyword Extraction
- JSON Data Storage
- lmxl

---

Author 
Riya More


