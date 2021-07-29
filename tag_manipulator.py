import re

class TagManipulator():    
    def parse_string(self, tags, regex=""):
        result = []

        tempResult = re.split( regex, tags )
        if( len(tempResult[0]) > 0 ):
            result = tempResult  

        trimmedResult = []
        for item in result:
            tmp = item.strip()
            print(tmp)
            if len(tmp) > 0:
                trimmedResult.append(tmp)

        return trimmedResult