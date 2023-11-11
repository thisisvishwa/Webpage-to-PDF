```python
import os
import tempfile

class TempStorage:
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()

    def store_webpage(self, webpage_content, webpage_name):
        temp_file_path = os.path.join(self.temp_dir, webpage_name)
        with open(temp_file_path, 'w') as temp_file:
            temp_file.write(webpage_content)
        return temp_file_path

    def clear_storage(self):
        for file_name in os.listdir(self.temp_dir):
            file_path = os.path.join(self.temp_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
```