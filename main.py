import requests
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {name}")  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hello')

def getHTML(link):
   return requests.get(link)

def parseData(data):
    addContent = False
    parsedData = data.split('<')

    for i in parsedData:
        if "text-block" not in i:
            parsedData.remove(i)
        else:
            print(i)

    return parsedData



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }

    testData = open("testData.txt", 'r+')

    if testData.read() == "":
        rawData = requests.get('https://www.bbc.com/news/world-europe-68435163', headers=headers, verify=False).text
        testData.writelines(rawData)

    testData.seek(0)
    parseData(testData.read())
    testData.close()






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
