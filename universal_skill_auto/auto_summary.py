from newspaper import Article

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()  # 触发 NLP，生成 summary/keywords
    return {
        "title": article.title,
        "summary": article.summary,
        "keywords": article.keywords
    }

if __name__ == "__main__":
    url = input("Enter article URL: ")
    result = summarize_article(url)
    print("Title:", result["title"])
    print("Summary:", result["summary"])
    print("Keywords:", result["keywords"])