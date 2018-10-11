import re

def sortquestions():
    pd = {}
    y=re.split(r"(Q\d+\))", open('Python_Assignment.txt').read())
    for index, txt in enumerate(y):
        #print('#############',index,txt)
        if "".join(re.findall(r'^Q(\d+)(?=\))', txt)).isdigit():
            pd[int("".join(re.findall(r'^Q(\d+)(?=\))', txt)))] = txt + y[index+1] if index<len(y) else ""

    data = ""
   # print('Hiiiiiiiiii',data)
    for q in range(1, len(pd)+1):
        #print('&&&&&&&&&&&&&&&&',q)
        data += pd[q]
        #print('$$$$$$$$$$$$$$$$$',data)
        with open("sortedquestions.txt", "wb+") as f:
            f.write(data)

if __name__=='__main__':
    sortquestions()
