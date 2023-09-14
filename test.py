import random

def SendWord(String):
    ListWord = ["기차", "차도", "도지", "지박"]
    for index in ListWord:
        if String[int(str.__len__(String) - 1)] == index[0]:
            print(index)
            return index
          
class Real:
    ListWord = ["기차", "차도"]
    UsedWord = {"nah"}
    CurrentWord = ListWord[random.randint(0, 1)]
    print("저먼저 할게요 " + CurrentWord)
    GetInput = input()
    if GetInput[0] == CurrentWord[int(str.__len__(GetInput) - 1)]:
        for index in UsedWord:
            if index == GetInput:
                print("이미 사용한 단어입니다.")
                break
        SendWord(GetInput)
        UsedWord.add(GetInput)

Real()
