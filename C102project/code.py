import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot ():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)

    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    
    return img_name

    print('Snapshot taken..')

    videoCaptureObject.release()
    cv2.destroyAllWinodows()

def upload_file (img_name):
    access_token = 'Rpi3eCHnkHUAAAAAAAAAAU0ikUB96DfHfHQ33ljfENBQdcjWn1mwV_lYDjjLGcue'
    file = img_name
    file_from = file
    file_to = '/'+(img_name)
    dbx = dropbox.Dropbox(access_token)
    
    f = open(file_from , 'rb')
    dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
    print('file Uploaded')

def main():
    while(True) :
        if((time.time() - start_time)>= 15):
            name = take_snapshot()
            upload_file(name)

main()
