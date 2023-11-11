```python
import os

class OutputDirectory:
    def __init__(self):
        self.output_directory = os.path.join(os.path.expanduser("~"), "PDF_Converter_Output")

    def set_output_directory(self, directory):
        if os.path.isdir(directory):
            self.output_directory = directory
        else:
            print("Invalid directory. Using default output directory.")

    def get_output_directory(self):
        return self.output_directory

    def create_directory_if_not_exists(self):
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
```