import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)
        #os.walk will list all the files
        for root, dirs, files in os.walk(file_from):
            #we are moving the files
            for file_name in files:
                #root is C:/Users/ryank/Desktop/python/py
                #file_name is your first file in the folder
                #local path = C:/Users/ryank/Desktop/python/py/C101.py
                local_path = os.path.join(root,file_name)
                print('local_path is', local_path)
                #relative path = local_path file_from
                relative_path = os.path.relpath(local_path, file_from)
                print('relative_path is', relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print('dropbox_path is',dropbox_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite')) 
                


def main():
    access_token = 'sl.Atsgs3KUATF_2wWNrTr3EUbEDW4X749xDQ3UPsrBUDVyIhEALsCa-kqDm2z7mAlS9kGYCtzD_VW1tHs8Q1xlTbeq7Wa6MuAA4upwyKeZ9spt6V7qIfIadGxXDMCh4c70SZY8atH9'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.


    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()


