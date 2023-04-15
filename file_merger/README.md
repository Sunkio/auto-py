# File Merger
This Python script is an easy-to-use Command Line Interface (CLI) program that allows you to effortlessly combine multiple files of the same type into a single output file. It supports the following file types: CSV, XLSX, PDF, DOCX, and ODT. The script guides you through the input options by asking a series of questions, making it user-friendly and straightforward to use.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Important Notes and Warnings](#important-notes-and-warnings)
- [Troubleshooting](#troubleshooting)
- [Understanding the Code](#understanding-the-code)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Prerequisites

To use this script, you need to have Python 3.6 or higher installed on your system. You can download Python from the official website: https://www.python.org/downloads/

## Installation

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and then clone this repository:
   ```
   git clone https://github.com/<your username>/auto-py.git
   ```

2. Navigate to the directory containing the script.

   ```
   cd file_merger
   ```

3. Install the required dependencies using the following command:

   ```
   pip install pandas PyPDF2 odfpy
   ```

4. Install Pandoc from the official website: https://github.com/jgm/pandoc/releases/tag/3.1.2

   Follow the instructions for your operating system to install Pandoc. This is necessary for combining DOCX and ODT files.

## Usage

1. Run the script using the following command:

   ```
   python main.py
   ```

2. Follow the prompts to provide the necessary information:

   - Enter the working directory: This is the directory where the files to be combined are located. If left empty, the current working directory will be used.

   - Set index to true or false: This is applicable for CSV and XLSX files. If set to true, the index column will be included in the output file.

   - Enter the output directory: This is the directory where the combined files will be saved. If left empty, the current working directory will be used.

   - Enter the file type to be combined: Choose one of the supported file types (csv, xlsx, pdf, docx, odt), or enter "all" to combine all supported file types in the working directory.

   - Enter the specific file names to be combined: If you want to combine specific files instead of all files of the specified type in the working directory, enter the file names separated by commas.

3. The script will then combine the files and save the output files in the specified output directory. A message will be displayed to inform you whether the files were combined successfully or if there were any issues.

### Important Notes and Warnings

- When combining Word (DOCX), LibreOffice Writer (ODT), or PDF files, it is recommended to ensure that these files have the same layout settings, such as margins, page size, and font styles. Otherwise, the combined output file may have inconsistent formatting.

- When combining CSV or Excel files, the script concatenates the files. If the files have different column names or data structures, the resulting file may have missing or misaligned data. Make sure the files have consistent column names and data structures for accurate results.

## Troubleshooting

If you encounter any errors while running the script, please check the following:

1. Make sure you have installed all the required dependencies using the `pip install` command mentioned above.

2. Ensure that the provided working directory exists and contains the files you want to combine.

3. Verify that the specified file type is supported by the script.

If you still face any issues, please feel free to ask for help or create an issue in the repository.

## Understanding the Code

The `main.py` script is organized into several parts:

1. Importing required libraries: The script imports necessary libraries such as `os`, `glob`, `pandas`, `PyPDF2`, and `odf`.

2. Defining helper functions: The script defines several helper functions like `get_input`, `filter_files`, and `is_valid_pdf` for getting user input, filtering files based on user input, and checking if a PDF file is valid, respectively.

3. Getting user input: The script prompts the user for input, such as the working directory, output directory, file type to be combined, and specific file names.

4. Combining files: The script iterates through different file types and combines them using the appropriate methods depending on the file type (CSV, XLSX, PDF, DOCX, or ODT).

5. Displaying the result: The script displays a message to inform the user whether the files were combined successfully or if there were any issues.

## Resources
- Pandas documentation: https://pandas.pydata.org/docs/
- PyPDF2 documentation: https://pythonhosted.org/PyPDF2/
- Odfpy documentation: https://github.com/eea/odfpy
- Pandoc documentation: https://pandoc.org/documentation.html

## Contributing
Contributions are always welcome! If you'd like to contribute to this project or have any suggestions, feel free to create a new issue or submit a pull request. Please check the [Code of Conduct](./CODE_OF_CONDUCT.md) first.

To submit a pull request, follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## License

This project is open-source and available under the [MIT License](./LICENSE.md).

## Support
If you have any questions or need help getting started, please open an issue in the repository or contact me on Twitter: @tanja_codes
