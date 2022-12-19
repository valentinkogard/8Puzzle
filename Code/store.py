
class store:

    def writeToTxt(filename, content):
        """
        appends content to file

        Parameters:
            filename (String): path to file
            content (String): data that should be written to file

        Returns:
            -
        """
        with open(filename, "a") as file:
            file.write(content)