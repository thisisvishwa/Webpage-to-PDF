```python
import unittest
from PyQt5.QtWidgets import QApplication
from src.main import MainApp

app = QApplication([])

class UserAcceptanceTests(unittest.TestCase):

    def setUp(self):
        self.gui = MainApp()

    def test_download_webpage(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.download_button.click()
        self.assertEqual(self.gui.download_status.text(), "Download successful")

    def test_convert_to_pdf(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.download_button.click()
        self.gui.convert_button.click()
        self.assertEqual(self.gui.conversion_status.text(), "Conversion successful")

    def test_edit_pdf(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.download_button.click()
        self.gui.convert_button.click()
        self.gui.edit_button.click()
        self.assertEqual(self.gui.edit_status.text(), "Edit successful")

    def test_output_settings(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.download_button.click()
        self.gui.page_size_input.setText("A4")
        self.gui.orientation_input.setText("Portrait")
        self.gui.margin_input.setText("1cm")
        self.gui.header_input.setText("Header")
        self.gui.footer_input.setText("Footer")
        self.gui.convert_button.click()
        self.assertEqual(self.gui.output_settings_status.text(), "Output settings applied successfully")

    def test_progress_indicator(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.download_button.click()
        self.assertNotEqual(self.gui.progress_indicator.value(), 0)

    def test_preview_pane(self):
        self.gui.url_input.setText("https://www.example.com")
        self.gui.preview_button.click()
        self.assertEqual(self.gui.preview_pane_status.text(), "Preview successful")

if __name__ == "__main__":
    unittest.main()
```