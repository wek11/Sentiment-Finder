import requests, sys
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hello')
    print("hi")

def getHTML(link):
   return requests.get(link)

def parseData(data):
    removeRest = False
    removeList = []
    appendData = False
    text = []
    ind = 0
    parsedData = data.split(':')
    # print(parsedData)
    for i in parsedData:
        if appendData:
            # print(i)
            text.append(i)
            # print(text)
        if "text" in i:
            appendData = True
            # print(True)
        else:
            appendData = False

    for b in text:
        if removeRest:
            removeList.append(b)
        else:
            if '"blocks"' in b:
                removeList.append(b)
            elif "none;" in b:
                # print(b)
                removeList.append(b)
            elif "Copyright current_year BBC" in b:
                removeRest = True
                removeList.append(b)
        b.strip("'")
        b.strip("")
    for term in removeList:
        text.remove(term)
    # print(text)
    return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }

    testData = open("testData.txt", 'r+', encoding="utf-8")

    if testData.read() == "":
        rawData = requests.get('https://www.bbc.com/news/world-us-canada-68510250', headers=headers, verify=False).text
        print(rawData)
        testData.write(rawData)

    testData.seek(0)
    for i in parseData(testData.read()):
        print(i)
    testData.close()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
