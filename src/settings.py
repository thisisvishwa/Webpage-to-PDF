```python
from PyQt5.QtWidgets import QFileDialog

class Settings:
    def __init__(self):
        self.page_size = 'A4'
        self.orientation = 'Portrait'
        self.margin = {'top': '10mm', 'bottom': '10mm', 'left': '10mm', 'right': '10mm'}
        self.header = ''
        self.footer = ''
        self.output_directory = ''

    def set_page_size(self, size):
        self.page_size = size

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_margin(self, top, bottom, left, right):
        self.margin = {'top': top, 'bottom': bottom, 'left': left, 'right': right}

    def set_header(self, header):
        self.header = header

    def set_footer(self, footer):
        self.footer = footer

    def set_output_directory(self):
        self.output_directory = QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QFileDialog.ShowDirsOnly)

    def get_settings(self):
        return {
            'page_size': self.page_size,
            'orientation': self.orientation,
            'margin': self.margin,
            'header': self.header,
            'footer': self.footer,
            'output_directory': self.output_directory
        }
```