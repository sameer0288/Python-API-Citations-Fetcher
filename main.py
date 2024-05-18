import requests
import time
import logging
import difflib

logging.basicConfig(level=logging.INFO)

def fetch_all_data():
    base_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    page = 1
    all_data = []

    while True:
        response = requests.get(base_url, params={"page": page})
        if response.status_code != 200:
            logging.error(f"HTTP error occurred: {response.status_code} {response.reason}")
            break

        data = response.json().get('data', {}).get('data', [])
        if not data:
            break

        all_data.extend(data)
        page += 1
        time.sleep(1)  # to prevent hitting rate limits

    return all_data

def match_response_to_sources(response_text, sources):
    citations = []
    for source in sources:
        context = source['context']
        if difflib.SequenceMatcher(None, response_text, context).ratio() > 0.5:
            citations.append({
                "id": source["id"],
                "link": source.get("link", "")
            })
    return citations

def process_data(data):
    results = []
    for item in data:
        response_text = item['response']
        sources = item['source']
        citations = match_response_to_sources(response_text, sources)
        results.append({"citations": citations})
    return results

def main():
    data = fetch_all_data()
    if data:
        results = process_data(data)
        citations = []
        for result in results:
            citations.extend(result["citations"])
        
        print(citations)
    else:
        logging.info("No data fetched from the API.")


if __name__ == "__main__":
    main()
