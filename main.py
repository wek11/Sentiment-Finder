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

    for i in range(1, len(text)):
        if "www.bbc" in text[-i - 1]:
            text = text[len(text) - i:]
            break

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

    for i in range(2, len(text)):
        if text[-i] not in removeList:
            if text[-i] in text[:len(text) - i]:
                removeList.append(text[-i])
            elif int(len(text[-i])) > 20 and int(len(text[-i+1]) > 20):
                if text[-i][:15] == text[-i+1][:15]:
                    removeList.append(text[-i])

    for i in range(0, len(text)):
        if text[i].endswith(",\"locator"):
            text[i] = text[i][:len(text[i]) - len(",\"locator")]

    for term in removeList:
        if term in text:
            text.remove(term)
    # print(text)
    for i in range(len(text)):
        if text[i].endswith(",\"attributes\""):
            text[i] = text[i][:len(text[i]) - len(",\"attributes\"")]
        text[i] = text[i].strip('" ')


 
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
        rawData = requests.get('https://www.bbc.com/news/uk-68542187', headers=headers, verify=False).text
        print(rawData)
        testData.write(rawData)

    testData.seek(0)
    for i in parseData(testData.read()):
        print(i)
    testData.close()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
