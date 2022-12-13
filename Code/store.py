
class store:

    def writeToTxt(filename, content):
        with open(filename, "a") as file:
            file.write(content)