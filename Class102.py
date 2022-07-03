
import cv2 
import dropbox 
import time
import random

starttime = time.time()
def snapshot():
    number = random.randint(0, 100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videocaptureobject.read()
        image_names = "img"+str(number)+".png"
        cv2.imwrite(image_names , frame)
        starttime = time.time
        result = False
    return image_names
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()
def upload_file(image_names):
    accesstoken = "sl.BKp1S3slXWgiafuyZPvI_IHmIeNe8ZGenHLoxfNnjR1qaNL7WTGRsVL7D-1yvmNkjCKvEq3XaYCvUjmUZRETwd7Zyt7iyskjLrV7-vzipdqh05Bhmly4pKR2eM3DUzNk2s3sqL846AC4"
    file = image_names
    file_from = file
    file_to = "/testfolder"+(image_names)
    dbx = dropbox.Dropbox(accesstoken)
    with open (file_from,"rb") as f:
        dbx.files_upload(f.read(), file_to , mode = dropbox.files.WriteMode.overwrite)
        print("files uploaded successfully")

def main():
    while(True):
        if ((time.time()-starttime)>=5):
            name = snapshot()
            upload_file(name)



main()





