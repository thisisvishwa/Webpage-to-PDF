```python
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import Qt

class ProgressIndicator(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setAlignment(Qt.AlignCenter)

    def update_progress(self, value):
        self.setValue(value)

    def reset_progress(self):
        self.reset()
```