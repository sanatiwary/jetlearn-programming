import cv2
import os
from PIL import Image

print("i am inside", os.getcwd())
os.chdir("//Users/sana/Desktop/vsc/jetlearn/opencv/l3/images/collageimages")
path = "/Users/sana/Desktop/vsc/jetlearn/opencv/l3/images/collageimages"

meanWidth = 0
meanHeight = 0
numOfImgs = len(os.listdir('.'))
print(numOfImgs)

for file in os.listdir('.'):
    if file.endswith('jpg') or file.endswith('.png'):
        im = Image.open(os.path.join(path, file))
        imresize = im.resize((1200, 800))
        imresize.save(file, 'JPEG', quality = 95)

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    meanWidth += width
    meanHeight += height

meanWidth = int(meanWidth/numOfImgs)
meanHeight = int(meanHeight/numOfImgs)

def generateVideo():
    imageFolder = "/Users/sana/Desktop/vsc/jetlearn/opencv/l3/images/collageimages"
    videoName = "collage.avi"
    os.chdir("//Users/sana/Desktop/vsc/jetlearn/opencv/l3/images/collageimages")

    images = [img for img in os.listdir(imageFolder) if img.endswith('.jpg')]
    frame = cv2.imread(os.path.join(imageFolder, images[0]))

    height, width, layers = frame.shape
    video = cv2.VideoWriter(videoName, 0, 1, (width, height))

    for img in images:
        video.write(cv2.imread(os.path.join(imageFolder, img)))
    
    video.release()
    cv2.destroyAllWindows()


generateVideo()