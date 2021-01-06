from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import json
import io

from PIL import Image

import numpy as np

import cv2
kernel = np.ones((5,5),np.uint8)
# Create your views here.





def index(request):
    context={'a':1}
    return render(request,'index.html')
def predictImage(request):
    if request.method == 'POST':

        file=request.FILES['filePath']
        img_bytes = file.read()
        #img=Image.open(request.FILES["fi"])
        #img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        fs=FileSystemStorage()
        filePathName=fs.save(file.name,file)

        #img = cv2.imread('filePathName',0)
        filePathName=fs.url(filePathName)
        testimage='.'+filePathName
        if 'gray' in request.POST:


            img = cv2.imread(testimage,1)
            print(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            l=cv2.imwrite('media/file.png',gray)
            context={'a':"Gray"}
        if 'blur' in request.POST:


            img = cv2.imread(testimage,1)
            print(img)
            blur = cv2.blur(img, (9, 9))
            l=cv2.imwrite('media/file.png',blur)
            context={'a':"blur"}
        #img = cv2.imread('filePathName',0)
        #filePathNameg="C:/Users/Ibrahim Kholil (ICT)/dja/file.png"
        if 'median' in request.POST:


            img = cv2.imread(testimage,1)
            print(img)
            median = cv2.medianBlur(img, 5)
            l=cv2.imwrite('media/file.png',median)
            context={'a':"median filter"}
        if 'thresholding' in request.POST:


            img = cv2.imread(testimage,1)
            print(img)
            ret,median = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
            l=cv2.imwrite('media/file.png',median)
            context={'a':"threshoded"}
        if 'grad' in request.POST:


            img = cv2.imread(testimage,1)
            print(img)
            median = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
            l=cv2.imwrite('media/file.png',median)
            context={'a':"Gradient"}
        if 'eq' in request.POST:


            img = cv2.imread(testimage,0)
            print(img)
            median = cv2.equalizeHist(img)
            #res = np.hstack((img,median))
            l=cv2.imwrite('media/file.png',median)
            context={'a':"Histogram Equlization"}
    return render(request,'index.html',context)

    #images = testimage.reshape(-1, 224*224)
#    outputs = model(image)
        # max returns (value ,index)
#    _, predicted = torch.max(outputs.data, 1)





def viewDataBase(request):
    import os
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context)
