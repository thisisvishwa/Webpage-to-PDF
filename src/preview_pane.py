```python
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class PreviewPane(QWebEngineView):
    def __init__(self, parent=None):
        super(PreviewPane, self).__init__(parent)

    def load_url(self, url):
        self.load(QUrl(url))

    def clear(self):
        self.load(QUrl('about:blank'))
```