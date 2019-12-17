import os

class FileManager:
    def __init__(self, path=r"C:\Users\ASUS"):
        self.basepath = path
        self.extensions = [
            '.py',
            '.txt',
            '.xls'
        ]
        self.files = {}

    def allFiles(self, path):
        try:
            fs = [f for f in os.listdir(path)]
            #print (fs)
        except Exception as err:
            # print ('ERR: {}'.format(err))
            return
        myP = path + '\{}'
        for f in fs:
            try:
                if os.path.isfile(myP.format(f)) and any(ext in f for ext in self.extensions):
                    self.files[f] = os.path.abspath(myP.format(f))
                    #print ('FILE: {}'.format(f))
                else:
                    self.allFiles(myP.format(f))
            except Exception as err:
                # print (err)
                return
    def display(self):
        for f in self.files:
            print (f, self.files[f])
    
#fm = FileManager()
#fm.allFiles(fm.basepath)
#fm.display()

