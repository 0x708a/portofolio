class PuApp():
    def __init__(self, name, debug=True, preScript=None):
        if debug: print("[" + name + "] Creating App...")

        self.__name = name
        self.__debug = debug
        self.__v = "Beta 1.0.0"

        try:
            import os
        except ImportError as e:
            if debug:
                print(e)
                exit()
        
        if debug: print("[" + self.__name + "] Successfully created app!")

    def getFolder(self):
        f = __file__.split("\\")[1]
        return f
    
    def getAppName(self):
        return self.__name
    
    def setAppVersion(self, v):
        self.__v = v
        if self.__debug: print("[" + self.__name + "] Set version to: " + self.__v)
    
    def getAppVersion(self):
        return self.__v

    def log(self, msg):
        if not self.__debug: return None

        print("[" + self.__name + "] " + msg)

    def setPreScript(self, script):

        self.preScript = [r'' + self.getFolder() + '\\' + script + '.bat']
        f = open(self.getFolder() + "preferences.txt", "a")
        f.write("prescript: " + str(self.preScript) + "\n")
        return
