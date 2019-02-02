from PIL import Image

def convertToBlackandWhite(input_path,output_path):
    colour_image=Image.open(input_path)

    bw=colour_image.convert('L')
    bw.save(output_path)

convertToBlackandWhite("image.jpeg","output_image.jpeg")
    