import json
import requests
import threading

link_file = open("./other_files/links.txt", "r")

def check_urls_from_file(url, data):

    try:
        request = requests.get(url)
        payload = {
                     "url": url,
                     "is_ok": request.status_code == requests.codes.ok,
                     "status_code": request.status_code
                }
        data.append(payload)

    except ConnectionError:
        pass
    except:
        import sys
        # prints `type(e), e` where `e` is the last exception
        print(sys.exc_info()[:2])

def write_data_in_json_file(results):
    with open('./other_files/data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

results = []
file_line = link_file.read().splitlines()
threads = [threading.Thread(target=check_urls_from_file, args=(url, results))
           for url in
           file_line]


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

for result in results:
    print(result)

write_data_in_json_file(results)



