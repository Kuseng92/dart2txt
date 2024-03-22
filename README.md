# Dart to Text File Converter

This Python script is designed to automatically convert files from Dart (.dart) format to plain text (.txt) format. It is particularly useful for developers working with Dart files who need to quickly generate text versions for documentation, analysis, or any other purpose where plain text is required.

## Features

- **Bulk Conversion**: Easily convert all `.dart` files in a specified source directory.
- **Customizable Destination**: Specify a destination directory where all converted `.txt` files will be stored.
- **Preserves File Names**: The original file names are preserved, only the file extension is changed to `.txt`.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Usage

1. **Clone or download this repository** to your local machine.

2. **Place your `.dart` files** in a source directory if they are not already organized.

3. **Open the script** (`convert_dart_to_txt.py`) in your favorite text editor or IDE and set the `source_folder` and `destination_folder` variables to your source and destination directories, respectively.

    ```python
    source_folder = '/path/to/your/source/folder'  # Update this with the path to your .dart files
    destination_folder = '/path/to/your/destination/folder'  # Update this with your desired destination
    ```

4. **Run the script** in your terminal or command prompt:

    ```bash
    python convert_dart_to_txt.py
    ```

5. **Check your destination folder** for the `.txt` files.

## Contributing

Contributions are welcome! If you have suggestions for improving this script, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
