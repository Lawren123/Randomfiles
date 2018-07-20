# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(any_img):
    any_img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(any_img, filename):
    any_img.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def lawren(any_img):
    new_img = Image.new("RGB",any_img.size)

    #In the Obamicon filter:
    # lighter colors get set to yellow.intensity > 546
    yellow = (247, 240, 42)
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    lightBlue = (66,238,244)
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (244,65,65)
    # Dark colors get set to dark blue.intensity < 182
    darkBlue = (65,83,244)

    # Gather data into a list
    newPixels = []
    #Get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue
    # lighter colors get set to yellow.intensity > 546
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue.intensity < 182
        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364:
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)
def lawren1(any_img):
    new_img = Image.new("RGB",any_img.size)

    #In the Obamicon filter:
    # lighter colors get set to yellow.intensity > 546
    yellow = (255, 242, 0)
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    lightBlue = (41,104,206)
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (249,54,0)
    # Dark colors get set to dark blue.intensity < 182
    darkBlue = (41,43,206)

    # Gather data into a list
    newPixels = []
    #Get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue
    # lighter colors get set to yellow.intensity > 546
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue.intensity < 182
        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364:
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)

def lawren2(any_img):
    new_img = Image.new("RGB",any_img.size)

    #In the Obamicon filter:
    # lighter colors get set to yellow.intensity > 546
    yellow = (242, 226, 9)
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    lightBlue = (7, 239, 169)
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (96, 11, 14)
    # Dark colors get set to dark blue.intensity < 182
    darkBlue = (14, 16, 79)

    # Gather data into a list
    newPixels = []
    #Get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue
    # lighter colors get set to yellow.intensity > 546
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue.intensity < 182
        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364:
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)

def lawren3(any_img):
    new_img = Image.new("RGB",any_img.size)

    #In the Obamicon filter:
    # lighter colors get set to yellow.intensity > 546
    yellow = (255,255,7)
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    lightBlue = (20,153,170)
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    red = (242,25,9)
    # Dark colors get set to dark blue.intensity < 182
    darkBlue = (19,65,173)

    # Gather data into a list
    newPixels = []
    #Get data/list of pixels from original image
    imagePixels = list(any_img.getdata())

    for individualPixel in imagePixels:
        redValue = individualPixel[0]
        greenValue = individualPixel[1]
        blueValue = individualPixel[2]

        intensity = redValue + greenValue + blueValue
    # lighter colors get set to yellow.intensity > 546
    # Medium-light colors get coded as light blue.364 <= intensity <= 546
    # Medium-dark colors get set to red. 182 <= intensity <= 364
    # Dark colors get set to dark blue.intensity < 182
        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364 and intensity >= 182:
            newPixels.append(red)
        elif intensity < 546 and intensity >= 364:
            newPixels.append(lightBlue)
        else :
            newPixels.append(yellow)
    new_img.putdata(newPixels)
    return new_img
