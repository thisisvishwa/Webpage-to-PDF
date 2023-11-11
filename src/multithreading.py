```python
import threading
from src.downloader import download_webpage
from src.converter import convert_to_pdf

class DownloadThread(threading.Thread):
    def __init__(self, url, output_directory):
        threading.Thread.__init__(self)
        self.url = url
        self.output_directory = output_directory

    def run(self):
        download_webpage(self.url, self.output_directory)


class ConversionThread(threading.Thread):
    def __init__(self, webpage_file, output_directory):
        threading.Thread.__init__(self)
        self.webpage_file = webpage_file
        self.output_directory = output_directory

    def run(self):
        convert_to_pdf(self.webpage_file, self.output_directory)
```