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


def filter_tags(text):
    filtered_text = []
    unwanted_tags = {"none;", "\"locator", "{\""}
    indiv_tag = ""

    # Doesn't append tags containing data in the unwanted_tags set #
    # and also stops appending tags past the copyright (near the end of the article) #
    for b in text:
        if "Copyright current_year BBC" in b:
            break
        elif not any(unwanted_tag in b for unwanted_tag in unwanted_tags):
            indiv_tag = b.strip("\"").replace("\\\"", "\"").replace("\\", "\"")

            indiv_tag = indiv_tag.replace("\",\"attributes", "")

            indiv_tag = indiv_tag.replace("\",\"blocks", "")

            indiv_tag = indiv_tag.strip(" ")

            """
            Missing two of the tags at the start of the article, think it might be with locator in unwanted_tags
            """

            # Doesn't append tag if its not a paragraph
            if indiv_tag[0].isupper():
                # Adds the first 15 characters of each tag appended to sorted_text
                # to unwanted_tags to avoid duplicate text blocks
                # Adds b instead of indiv_tag b/c data.txt is not filtered
                unwanted_tags.add(b[:15])

                filtered_text.append(indiv_tag)



    """
    for i in range(2, len(text)):
    if text[-i] not in remove_list:
        if text[-i] in text[:len(text) - i]:
            remove_list.append(text[-i])
        elif int(len(text[-i])) > 20 and int(len(text[-i + 1]) > 20):
            if text[-i][:15] == text[-i + 1][:15]:
                remove_list.append(text[-i])
    """
    """
    for i in range(0, len(text)):
    if text[i].endswith(",\"locator"):
        text[i] = text[i][:len(text[i]) - len(",\"locator")]
    """
    """
    for term in remove_list:
        if term in text:
            text.remove(term)    
    """
    """
    for i in range(len(text)):
        if text[i].endswith(",\"attributes\""):
            text[i] = text[i][:len(text[i]) - len(",\"attributes\"")]
        text[i] = text[i].strip('" ')    
    """


    return filtered_text

def parse_data(data):
    remove_rest = False
    remove_list = []
    append_data = False
    text = []
    parsed_data = data.split('":')
    # print(parsedData)
    for i in parsed_data:
        if append_data:
            # print(i)
            text.append(i)
            # print(text)
        if "text" in i:
            append_data = True
            # print(True)
        else:
            append_data = False

    for i in range(1, len(text)):
        if "www.bbc" in text[-i - 1]:
            text = text[len(text) - i:]
            break

    text = filter_tags(text)











    return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    headers = {
        'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'
    }

    test_data = open("testData.txt", 'r+', encoding="utf-8")

    if test_data.read() == "":
        rawData = requests.get('https://www.bbc.com/news/world-europe-68543919', headers=headers, verify=False).text
        print(rawData)
        test_data.write(rawData)

    test_data.seek(0)
    for i in parse_data(test_data.read()):
        print(i)
    test_data.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
