import re

class TagManipulator():    
    def parse_string(self, tags, regex=","):
        result = []

        tempResult = re.split( regex, tags )

        trimmedResult = []
        for item in tempResult:
            tmp = item.strip()
            print(tmp)
            if len(tmp) > 0:
                trimmedResult.append(tmp)

        return trimmedResult