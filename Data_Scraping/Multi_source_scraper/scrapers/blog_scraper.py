from newspaper import Article, Config
from utils import detect_language, extract_topics, chunk_content
from trust_score import compute_trust_score


def scrape_blog(url):

    try:

        config = Config()
        config.browser_user_agent = "Mozilla/5.0"

        article = Article(url, config=config)

        article.download()
        article.parse()

        text = article.text

        language = detect_language(text)

        topics = extract_topics(text)

        chunks = chunk_content(text)

        trust = compute_trust_score(
            url,
            article.authors,
            "blog",
            article.publish_date,
            text
        )

        data = {
            "source_url": url,
            "source_type": "blog",
            "author": article.authors,
            "published_date": str(article.publish_date),
            "language": language,
            "region": "Global",
            "topic_tags": topics,
            "trust_score": trust,
            "content_chunks": chunks
        }

        return data

    except Exception as e:

        print("Blog scraping failed:", url)
        print(e)

        return None

    except Exception as e:

        print("Blog scraping failed:", url)
        print("Error:", e)

        return None