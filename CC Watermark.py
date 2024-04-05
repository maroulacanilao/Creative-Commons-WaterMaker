import os
from PIL import Image, ImageDraw, ImageFont

font = 'arial.ttf'
fontColor = (255, 255, 255, 250) #rgba
fontDividerByImageSize = 60
margin = 10 

def add_watermark(fileName, inputFolder, outputFolder, text):
    try:
        image = Image.open(os.path.join(inputFolder, fileName))
        width, height = image.size

        font_size = width // fontDividerByImageSize
        fontType = ImageFont.truetype(font, font_size)

        draw = ImageDraw.Draw(image)

        text_width, text_height = draw.textbbox((0, 0), text, font=fontType)[2:]
        x = width - text_width - margin
        y = height - text_height - margin

        draw.text((x, y), text, font=fontType, fill=(fontColor))

        image.save(os.path.join(outputFolder, fileName))
        print('Finished with ' + fileName + '\n')
        
    except Exception as e:
        print(f"Error: {str(e)}")

def get_input_bool(text):
    while True:
        user_input = input(text)

        if user_input.lower() in ["yes", "y"]:
            return True
        elif user_input.lower() in ["no", "n"]:
            return False
        
def getCreativeCommonText():
    useWholeText = get_input_bool('Use Full Text For CC? (y/n): ')
    print('1. CC BY')
    print('2. CC BY-SA')
    print('3. CC BY-NC')
    print('4. CC BY-NC-SA')
    print('5. CC BY-ND')
    print('6. CC BY-NC-ND')

    while True:
        print('\n')
        userInput = input('What CC is going to be used? (1/2/3/4/5/6): ')
        text = ''

        if userInput == '1':
            text = 'CC BY 4.0 Deed'

            if useWholeText:
                text += '\n' + 'Attribution 4.0 International'

            return text
        
        elif userInput == '2':
            text = 'CC BY-SA 4.0 Deed'

            if(useWholeText):
                text += '\n' + 'Attribution-ShareAlike 4.0 International'

            return text
        
        elif userInput == '3':
            text = 'CC BY-NC 4.0 Deed'

            if(useWholeText):
                text += '\n' + 'Attribution-NonCommercial 4.0 International'

            return text
        
        elif userInput == '4':
            text = 'CC BY-NC-SA 4.0 Deed'

            if(useWholeText):
                text += '\n' + 'Attribution-NonCommercial-ShareAlike 4.0 International'

            return text
        
        elif userInput == '5':
            text = 'CC BY-ND 4.0 Deed'

            if(useWholeText):
                text += '\n' + 'Attribution-NoDerivs 4.0 International'

            return text

        elif userInput == '6':
            text = 'CC BY-NC-ND 4.0 Deed'

            if(useWholeText):
                text += '\n' + 'Attribution-NonCommercial-NoDerivs 4.0 International'

            return text
    
    

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    inputFolder = os.path.join(script_dir, 'Input')
    outputFolder = os.path.join(script_dir, 'Output')
    
    useLabel = get_input_bool('Use label? (y/n): ')
    useFileNameAsTitle = get_input_bool('Use file name as title? (y/n): ')

    titleTxt = 'Title: ' if useLabel else ''

    creatorTxt = 'Creator: ' if useLabel else ''
    creatorTxt += input('creator: ')

    sourceTxt = 'Source: ' if useLabel else ''
    sourceTxt +=  input('source: ')

    creativeCommonsTxt = 'Creative Commons:\n' if useLabel else ''
    creativeCommonsTxt += getCreativeCommonText()

    for filename in os.listdir(inputFolder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):

            print(os.path.join(inputFolder, filename))

            if(useFileNameAsTitle):
                titleTxt += filename + '\n'
            else:
                titleTxt += input('Title for ' + '"' + filename + '"' + ': ') + '\n'

            text = titleTxt
            text += creatorTxt + '\n'
            text += sourceTxt + '\n'
            text += creativeCommonsTxt + '\n'

            add_watermark(filename, inputFolder, outputFolder, text)

    input("Press Enter to exit...")
