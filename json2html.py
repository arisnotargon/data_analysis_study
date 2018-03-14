import json
import datetime
import re


def htmlBuilder(inputDict):
    """
    复原html
    传入dict,递归生成html字符串并返回
    TODO:加入定位属性
    """
    __selfCloesing = [
        "meta", "base", "br", "br", "img", "input", "col", "frame", "link", "area", "param", "object", "embed",
        "keygen", "source"
    ]

    htmlStr = ""
    # if upLevelStr is None:
    #     htmlStr = ""
    # else:
    #     htmlStr = upLevelStr
    if isinstance(inputDict, list):
        for temp in inputDict:
            htmlStr += htmlBuilder(temp)
    elif isinstance(inputDict, dict):
        if "nodeType" in inputDict:
            if inputDict["nodeType"] is 10 and "name" in inputDict:
                htmlStr += "<!Doctype " + str(inputDict["name"]) + ">"

            if "tagName" in inputDict:
                htmlStr += "<" + inputDict["tagName"] + " "
                if "attributes" in inputDict:
                    for attr in inputDict['attributes']:
                        inputDict['attributes'][attr] = re.sub("\"", "'", inputDict['attributes'][attr])
                        htmlStr += attr + "=\"" + inputDict['attributes'][attr] + "\" "

                if "id" in inputDict:
                    htmlStr += " nobot_analysis_id = " + str(inputDict["id"])

                if inputDict["tagName"] in __selfCloesing:
                    htmlStr += " /"

                htmlStr += ">"

            if "textContent" in inputDict:
                htmlStr += inputDict["textContent"]

            if "childNodes" in inputDict:
                for childNode in inputDict["childNodes"]:
                    htmlStr += htmlBuilder(inputDict=childNode)

            if "tagName" in inputDict and not inputDict["tagName"] in __selfCloesing:
                # 加闭合标签
                htmlStr = htmlStr + "</" + inputDict["tagName"] + ">"

    htmlStr += "\n"
    return htmlStr


if __name__ == "__main__":
    print(__name__)
    f = open('demo.json', "r")
    jsonStr = f.read()
    f.close()

    contentDict = json.loads(jsonStr)

    htmlstr = htmlBuilder(contentDict)
    fw = open('html_restore' + datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S') + ".html", "w")
    fw.write(htmlstr)
    fw.close()
