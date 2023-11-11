```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar, QFileDialog
from PyQt5.QtCore import Qt
from src.downloader import download_webpage
from src.converter import convert_to_pdf
from src.settings import Settings
from src.preview_pane import PreviewPane

class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Advanced Website-to-PDF Converter')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.url_label = QLabel('Enter URL:')
        self.layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        self.layout.addWidget(self.url_input)

        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.download)
        self.layout.addWidget(self.download_button)

        self.progress_label = QLabel('Progress:')
        self.layout.addWidget(self.progress_label)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.settings_button = QPushButton('Settings')
        self.settings_button.clicked.connect(self.open_settings)
        self.layout.addWidget(self.settings_button)

        self.preview_pane = PreviewPane()
        self.layout.addWidget(self.preview_pane)

        self.convert_button = QPushButton('Convert to PDF')
        self.convert_button.clicked.connect(self.convert)
        self.layout.addWidget(self.convert_button)

    def download(self):
        url = self.url_input.text()
        download_webpage(url)

    def convert(self):
        convert_to_pdf()

    def open_settings(self):
        self.settings = Settings()
        self.settings.show()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GUI()
    gui.show()

    sys.exit(app.exec_())
```