from datetime import datetime
from urllib.parse import urlparse


TRUSTED_DOMAINS = {
    "nature.com": 0.95,
    "pubmed.ncbi.nlm.nih.gov": 0.98,
    "who.int": 0.97,
    "cdc.gov": 0.97,
    "towardsdatascience.com": 0.75,
    "analyticsvidhya.com": 0.72,
    "machinelearningmastery.com": 0.80,
    "medium.com": 0.70,
    "youtube.com": 0.65
}


KNOWN_AUTHORS = {
    "Andrew Ng": 0.95,
    "Yann LeCun": 0.95,
    "Geoffrey Hinton": 0.95
}


def author_credibility(author):

    if not author:
        return 0.4

    if isinstance(author, list):

        scores = []

        for a in author:
            scores.append(KNOWN_AUTHORS.get(a, 0.6))

        return sum(scores) / len(scores)

    return KNOWN_AUTHORS.get(author, 0.6)


def citation_score(source_type):

    if source_type == "pubmed":
        return 0.95

    if source_type == "youtube":
        return 0.5

    return 0.6


def domain_authority(url):

    domain = urlparse(url).netloc

    for trusted in TRUSTED_DOMAINS:

        if trusted in domain:
            return TRUSTED_DOMAINS[trusted]

    return 0.4


def recency_score(published_date):

    if not published_date or published_date == "None":
        return 0.5

    try:

        year = int(str(published_date)[:4])

        current_year = datetime.now().year

        age = current_year - year

        if age <= 1:
            return 1.0
        elif age <= 3:
            return 0.8
        elif age <= 5:
            return 0.6
        else:
            return 0.3

    except:
        return 0.5


def medical_disclaimer_score(text):

    keywords = [
        "medical advice",
        "consult a doctor",
        "healthcare professional",
        "for educational purposes"
    ]

    text = text.lower()

    for k in keywords:

        if k in text:
            return 1.0

    return 0.5


def compute_trust_score(url, author, source_type, published_date, text):

    a = author_credibility(author)
    c = citation_score(source_type)
    d = domain_authority(url)
    r = recency_score(published_date)
    m = medical_disclaimer_score(text)

    score = (
        0.25 * a +
        0.20 * c +
        0.20 * d +
        0.20 * r +
        0.15 * m
    )

    return round(score, 3)