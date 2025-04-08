# QR Code Generator

This Python script allows users to generate QR codes from text or URLs and save them as image files. It is a simple tool for creating QR codes quickly and efficiently.

---

## Features

- Converts text or URLs into QR codes.
- Saves the generated QR code as a `.png` file.
- User-friendly input prompts for text/URL and output file name.

---

## Requirements

Before running the script, ensure that the following are installed:

1. **Python**: Version 3.x or higher.
2. **Required Python Package**: `qrcode`

---

## Installation

Follow these steps to set up the environment:

1. Clone this repository:

```bash
git clone 
cd 

```

2. Install the required Python package using pip:

```python
pip3 install qrcode[pil]

```
---

## Usage

To run the script, execute the following command in your terminal:
```python

python qr_main.py
```

### Script Inputs:
1. **Text or URL**: Enter the text or URL you want to convert into a QR code.
2. **Output File Name**: Specify the name for the output file (without extension).

### Example:
Enter The Text or URL to be converted into QR code: https://github.com
Enter the name of the output file (without extension): github_qr
QR code generated and saved as github_qr.png


---

## Error Handling

If you encounter the error `ModuleNotFoundError: No module named 'qrcode'`, ensure you have installed the `qrcode` package correctly by running:
``` python
pip install qrcode[pil]
```
---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Author

Created by Asitha Kanchana Palliyaguru . Contributions are welcome!
