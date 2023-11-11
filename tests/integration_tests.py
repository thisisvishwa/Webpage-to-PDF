```python
import unittest
from src import main, downloader, converter, settings, progress_indicator, multithreading, temp_storage, output_directory, preview_pane

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.main = main.Main()
        self.downloader = downloader.Downloader()
        self.converter = converter.Converter()
        self.settings = settings.Settings()
        self.progress_indicator = progress_indicator.ProgressIndicator()
        self.multithreading = multithreading.Multithreading()
        self.temp_storage = temp_storage.TempStorage()
        self.output_directory = output_directory.OutputDirectory()
        self.preview_pane = preview_pane.PreviewPane()

    def test_download_and_conversion(self):
        url = "https://www.example.com"
        self.downloader.download_webpage(url)
        self.converter.convert_to_pdf()
        self.assertTrue(self.output_directory.check_file_exists("example.pdf"))

    def test_settings_change(self):
        self.settings.change_page_size("A4")
        self.settings.change_orientation("Landscape")
        self.assertEqual(self.settings.page_size, "A4")
        self.assertEqual(self.settings.orientation, "Landscape")

    def test_progress_indicator(self):
        url = "https://www.example.com"
        self.downloader.download_webpage(url)
        self.assertTrue(self.progress_indicator.download_status)
        self.converter.convert_to_pdf()
        self.assertTrue(self.progress_indicator.conversion_status)

    def test_multithreading(self):
        url1 = "https://www.example1.com"
        url2 = "https://www.example2.com"
        self.multithreading.start_new_thread(self.downloader.download_webpage, (url1,))
        self.multithreading.start_new_thread(self.downloader.download_webpage, (url2,))
        self.assertTrue(self.output_directory.check_file_exists("example1.pdf"))
        self.assertTrue(self.output_directory.check_file_exists("example2.pdf"))

    def test_preview_pane(self):
        url = "https://www.example.com"
        self.downloader.download_webpage(url)
        self.preview_pane.show_preview()
        self.assertTrue(self.preview_pane.preview_status)

if __name__ == "__main__":
    unittest.main()
```