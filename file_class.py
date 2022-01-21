import os


class file_class():
    def __init__(self):
        self.self_files=None

    #get files from directory and select by chars
    def get_files(self,dir_in,selected=None):
        files=os.listdir(dir_in)
        if selected:
            files=[i for i in files if selected in i]
        return files


if __name__ == "__main__":
    print('file_class main')
