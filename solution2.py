class Solution:
    def __init__(self):
        self.count = 0

    def countWords(self):
        with open("input.txt", "r", encoding="utf8") as fileObj:
            for line in fileObj:
                lst = line.split()

                if len(lst) == 0:   #to handle new line
                    continue

                for elem in lst:
                    if elem[0].isupper():
                        self.count += 1
                    elif elem[0].isalpha() == False:
                        if len(elem) > 1 and elem[1].isupper() == True:
                            self.count += 1


if __name__ == "__main__":
    obj1 = Solution()
    obj1.countWords()
    print(obj1.count)