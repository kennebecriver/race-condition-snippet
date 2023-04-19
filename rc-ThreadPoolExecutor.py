import concurrent.futures
import requests

max_workers = 10

def process_url(url):
    # payload={}
    headers = {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Cookie': 'session=eyJ0b...',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    return requests.post('http://example.com/get-bonus',headers=headers).status_code

with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
    results = [executor.submit(process_url, url) for url in range(max_workers)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())
        
