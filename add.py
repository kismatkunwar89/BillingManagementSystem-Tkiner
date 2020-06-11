from subprocess import call

class CallPy(object):
    def __init__(self,path="/Users/kismat/Desktop/PROJECT/mainpage.py"):
        self.path=path
    def call_pythonfile(self):
        call(["Python3","{}".format(self.path)])

if __name__=="__main__":
    c=CallPy()
    c.call_pythonfile()
