```python
import requests
from src.progress_indicator import show_progress

def download_webpage(url, output_directory):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        download_status = "Downloading..."
        show_progress(download_status)

        with open(output_directory, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=1024):
                fd.write(chunk)

        download_status = "Download Complete"
        show_progress(download_status)

    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else Happened",err)
        download_status = "Download Failed"
        show_progress(download_status)

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        download_status = "Download Failed"
        show_progress(download_status)

    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        download_status = "Download Failed"
        show_progress(download_status)

    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        download_status = "Download Failed"
        show_progress(download_status)
```