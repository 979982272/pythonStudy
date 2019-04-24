import json


class FileUtils:
    def saveFile(self, fileName, contens, operateType):
        with open(fileName, operateType, encoding="utf-8") as f:
            for content in contens:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
