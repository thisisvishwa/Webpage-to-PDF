```python
import sys
from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from downloader import Downloader
from converter import Converter
from settings import Settings
from progress_indicator import ProgressIndicator
from multithreading import ThreadManager
from temp_storage import TempStorage
from output_directory import OutputDirectory
from preview_pane import PreviewPane

class MainApp(QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)
        self.main_window = MainWindow()
        self.settings = Settings()
        self.downloader = Downloader()
        self.converter = Converter()
        self.progress_indicator = ProgressIndicator()
        self.thread_manager = ThreadManager()
        self.temp_storage = TempStorage()
        self.output_directory = OutputDirectory()
        self.preview_pane = PreviewPane()

        self.setup_connections()

    def setup_connections(self):
        self.main_window.url_input.connect(self.downloader.download_webpage)
        self.downloader.download_finished.connect(self.converter.convert_to_pdf)
        self.converter.conversion_finished.connect(self.output_directory.save_pdf)
        self.downloader.download_progress.connect(self.progress_indicator.update_download_progress)
        self.converter.conversion_progress.connect(self.progress_indicator.update_conversion_progress)
        self.main_window.preview_request.connect(self.preview_pane.show_preview)

if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
```