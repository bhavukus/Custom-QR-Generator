# QR Code Generator

This is a simple Python script that generates a QR code for any given URL and allows you to customize the color of the QR code. The script also saves the QR code as an image file and prints the platform/domain name extracted from the URL.

## Features

- Generate a QR code from any URL.
- Choose a custom color for the QR code.
- Automatically extracts and prints the platform name from the URL.
- Save the QR code in an image format of your choice (e.g., .jpg, .png).
- Easy-to-use command-line interface.

## Prerequisites

Before running the program, make sure you have Python installed. You will also need to install the `qrcode` and `Pillow` libraries.

### Install the required dependencies:

```bash
pip install qrcode[pil]
```

## How to Run

1. Clone or download the repository.
2. Navigate to the folder where the script is located.
3. Run the script using Python.

### Example command to run:

```bash
python main.py
```

### Inputs

- **URL**: The URL for which you want to generate a QR code.
- **File Name**: The name of the file (e.g., `qrcode.jpg`) where you want to save the generated QR code.
- **Color**: Choose the color for the QR code (e.g., 'black', '#FF0000' for red). The background is always white.

### Output

The script will create and save a QR code with the specified color and print a message like:

```bash
The QR code for Youtube is saved as qrcode.jpg!
```

## Customization

- **Box Size**: The size of each box in the QR code can be customized by changing the `box_size` value in the code.
- **Border Thickness**: The thickness of the border around the QR code can be adjusted via the `border` parameter.
- **Error Correction**: You can add error correction by uncommenting the `error_correction` parameter in the `QRCode` instance and setting an appropriate level.

## Requirements

- Python 3.x
- qrcode
- Pillow (automatically installed with `qrcode[pil]`)

## License

This project is open-source and available under the MIT License. You are free to use, modify, and distribute this code as you wish.
