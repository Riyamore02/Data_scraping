import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

from utils import detect_language, extract_topics, chunk_content
from trust_score import compute_trust_score


def get_video_id(url):
    return url.split("v=")[1]


def scrape_youtube(url):

    video_id = get_video_id(url)

    transcript = ""

    try:
        data = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([x["text"] for x in data])
    except:
        transcript = ""

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.title.string if soup.title else ""

    language = detect_language(transcript)

    topics = extract_topics(transcript)

    chunks = chunk_content(transcript)

    trust = compute_trust_score(
        url,
        "YouTube Channel",
        "youtube",
        None,
        transcript
    )

    result = {
        "source_url": url,
        "source_type": "youtube",
        "author": "YouTube Channel",
        "published_date": "Unknown",
        "language": language,
        "region": "Global",
        "topic_tags": topics,
        "trust_score": trust,
        "content_chunks": chunks
    }

    return result