import qrcode
from urllib.parse import urlparse #to extract the domain name from the url

url = input(str("Enter the URL to generate the QR: ")).strip()
filename = input(str("Enter the File name where you want the QR code to get saved (Ex: file.jpg): ")).strip()

# Function to get a valid color input from the user
def get_color_input():
    while True:
        color = input("Enter the color for the QR code (e.g., 'black', '#FF0000' for red): ").strip()
        # Check if the input is a valid color name or hex code
        if color.startswith('#') and len(color) == 7:
            return color
        elif color in ['black', 'white', 'red', 'green', 'blue', 'yellow']:
            return color
        else:
            print("Invalid color input. Please enter a valid color name or hex code.")

qr = qrcode.QRCode(
    # version=1,
    # error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, # size of each box in pixels
    border=2, # thickness of the border (in boxes)
)

qr.add_data(url) #adding URL(data) to the QR code
# qr.make(fit=True) #to autmoatically adjust the size of the data

img = qr.make_image(fill_color=get_color_input(), back_color="white") #creating img from the QR code insance

img.save(filename)
platform_name = urlparse(url).netloc.split('.')[1] #to extract the platform/domain name from the URL

print(f"The QR code for {platform_name.capitalize()} is saved as {filename}!")