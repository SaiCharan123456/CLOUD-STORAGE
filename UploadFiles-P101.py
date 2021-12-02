import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, folder_from, folder_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        for root , dirs , files in os.walk(folder_from):

            for filename in files:

                local_path = os.path.join(root,filename)
                               
                relative_path = os.path.relpath(local_path,folder_from)
                dropbox_path = os.path.join(folder_to ,relative_path)
                
                with open(local_path, 'rb') as f:
                        dbx.files_upload(f.read(), dropbox_path , mode=WriteMode("overwrite"))

def main():
    access_token = 'sl.A9Zfx00_7nIlEv26uFtg6z-OMqNTUF9NXnJlv9JtIVkL_LvROWQf52IFpcLXPi3W9rxdJOgEkE42El6WBc8oaBK2bgD7K5M4LCgJD2p6Ar2lDt0e72MUAHjOOxEi3VzWNt4wwx5pZjCf'
    transferData = TransferData(access_token)

    folder_from = input("Enter the folder path :- ")
    folder_to = input("Enter the destination path :- ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(folder_from, folder_to)


main()
print("uploaded")