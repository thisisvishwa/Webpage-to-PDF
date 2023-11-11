# Developer Documentation

## Project Structure

The project is structured into several Python files and directories, each serving a specific purpose:

- `src/main.py`: This is the entry point of the application. It initializes the GUI and handles the main application logic.
- `src/gui.py`: This file contains the code for the GUI built using PyQt5.
- `src/downloader.py`: This file contains the code for downloading web pages.
- `src/converter.py`: This file contains the code for converting the downloaded web pages into PDFs using `pdfkit` and `wkhtmltopdf`.
- `src/settings.py`: This file contains the code for handling the settings of the PDF output.
- `src/progress_indicator.py`: This file contains the code for showing the progress of the download and conversion processes.
- `src/multithreading.py`: This file contains the code for handling multiple downloads and conversions simultaneously using Python's built-in multi-threading library.
- `src/temp_storage.py`: This file contains the code for temporarily storing the downloaded web pages.
- `src/output_directory.py`: This file contains the code for specifying the output directory for the PDFs.
- `src/preview_pane.py`: This file contains the code for the preview pane to view the web page before conversion.
- `tests/unit_tests.py`: This file contains the unit tests for the individual components of the application.
- `tests/integration_tests.py`: This file contains the integration tests to ensure all components work together.
- `tests/user_acceptance_tests.py`: This file contains the user acceptance tests to ensure the application meets user requirements.
- `docs/user_manual.md`: This file contains the user manual providing a detailed guide on using the application.
- `docs/faqs_and_troubleshooting.md`: This file contains the FAQs and troubleshooting guide for common issues and their resolutions.

## Shared Dependencies

The shared dependencies across the project include:

- Libraries and Modules: PyQt5, pdfkit, wkhtmltopdf, and Python's built-in multi-threading library.
- Functions: `download_webpage()`, `convert_to_pdf()`, `edit_pdf()`, `show_progress()`, `handle_errors()`, and `secure_download()`.
- Data Schemas: The data schema for the downloaded web page and the converted PDF file.
- Variables: `download_status`, `conversion_status`, `output_directory`, `page_size`, `orientation`, `margin`, `header`, and `footer`.
- GUI Elements: URL input field, output settings, conversion controls, progress indicators, and preview pane.
- Test Cases: Test cases for unit testing, integration testing, and user acceptance testing.
- Documentation: Documentation guidelines and content.

## Development Guidelines

When developing for this project, please adhere to the following guidelines:

- Follow the Python PEP 8 style guide for writing your code.
- Make sure to write docstrings for all your functions and classes.
- Keep your functions and classes small and focused on a single task.
- Write tests for your code and make sure all tests pass before committing your changes.
- Document any changes you make in the code and update the user manual and FAQs and troubleshooting guide as necessary.