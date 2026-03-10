from langdetect import detect
import yake


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"


def extract_topics(text):

    extractor = yake.KeywordExtractor(
        lan="en",
        n=2,
        top=6
    )

    keywords = extractor.extract_keywords(text)

    return [k[0] for k in keywords]


def chunk_content(text, chunk_size=400):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def calculate_trust_score(source):

    scores = {
        "blog": 0.6,
        "youtube": 0.75,
        "pubmed": 0.95
    }

    return scores.get(source, 0.5)