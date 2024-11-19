# .1 מיון לפי key
# "Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai" :הבא ברשימה .א
# השתמש ב sort וב - lambda כדי למיין לפי:
import statistics
from operator import index
from os.path import split
from random import random

l: list = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

# a. לפי אורך שם העיר
print(list(sorted(l, key= lambda c: len(c))))

# b. לפי מספר המילים בשם העיר
print(list(sorted(l, key= lambda c: (len(c.split())))))

# c. לפי האות האחרונה של שם העיר
print(list(sorted(l, key= lambda c: c[-1])))

# d. שם העיר בסדר אותיות הפוך
print(list(sorted(l, key=lambda c: c[::-1])))

# e.** בונוס: מספר הפעמים שבה מופיעה האות a
print(list(sorted(l, key=lambda c: "a" in c)))

# f. הוסף את המרחק במיילים מישראל ואת שם היבשת. לדוגמא:
l1: list= [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"],
           ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
           ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]


# א. מיין לפי המרחק מישראל
print(list(sorted(l1, key=lambda s: s[1])))
# ב. מיין לפי המרחק מישראל מהגדול לקטן
print(list(sorted(l1, key=lambda s: s[1], reverse=True)))
# ג. מיין לפי שם היבשת
print(list(sorted(l1, key=lambda s: s[2])))
# ד. מיין לפי שם היבשת ובמיון השני לפי המרחק. רמז )מיון,2 מיון1(
print(list(sorted(l1, key=lambda s: (s[2], s[1]))))

import random
# ב. צור רשימה של 50 מספרים אקראיים בין ,1-100
l2: list[int]= [random.randint(1,100) for _ in range(20)]
print(l2)
# .1 מ יין והדפס את הרשימה בסדר עולה
print(list(sorted(l2, key=lambda x: x)))
# .2 מיין והדפס את המספרים לפי המרחק שלהם מהממוצע
avg: float = statistics.mean(l2)
print(avg)
print(f"average is {avg} sort numbers by distances from the average: {list(sorted(l2, key=lambda x: abs(avg-x)))}")


# .2 מילון מילולי
# לפניך הקטע הבא:

text =("This chocolate cake is rich, moist, and full of delicious chocolate flavor."
 " To make the cake, you will need chocolate, flour, sugar, eggs, and butter. "
 "After baking the chocolate cake, let the cake cool before adding the chocolate frosting.")
words: list[str] = text.split()
print(words)
# a. ספור כמה פעמים כל מילה חוזרת על עצמה , ואז הדפס את כל המילים שהופיעו וכמה
# פעמים כל מילה הופיעה .. . מה המילה שחזרה על עצמה הכי הרבה פעמים?
dict_count_word: dict[str, int] = dict()
for word in words:
    if word.isalpha():
        word = word.lower()

        if word in dict_count_word:
            dict_count_word[word] += 1
        else:
            dict_count_word[word] = 1
print(dict_count_word)
print(max(dict_count_word))

# b. ספור כמה פעמים כל אות חוזרת ע ל עצמה, ואז הדפס את כל האותיות שהופיעו וכמה
# פעמים כל אות הופיעה... מה האות שחזרה על עצמה הכי פחות פעמים?
dict_count_letter: dict[str, int] = dict()


for letter in text:
    if letter.isalpha():
        letter = letter.lower()

        if letter in dict_count_letter:
            dict_count_letter[letter] += 1
        else:
            dict_count_letter[letter] = 1
print(dict_count_letter)
print(min(dict_count_letter))

# .3 מילון מספרי
# צור מילון שבו יופי ע חזקה של כל מספר ב- ,3 מ- 1 ועד 20
# המפתח יהיה המספר )בסיס(, והערך יהיה המספר בחזקת 3
# לדוגמא {... 27 3: 8, 2: 1, 1: }
# הסבר: 1 בחזקת 3 =< ,1 2 בחזקת 3 =< ,8 3 בחזקת 3 = 27 וכו'
# כעת קלוט מספר מהמשתמש והדפס את תוצאת החזקה של המספר ב - 3
# לדוגמא אם נקלט המספר 2 התשובה שתודפס תהיה 8
# אם המספר לא קיים במילון , הדפס exist not

dict_power_3: dict[int, int] = {}
for key in range(1,20):
    dict_power_3[key] = key ** 3
print(dict_power_3)

x: int = int(input("enter a number: "))
if x in dict_power_3:
    print(dict_power_3[x])
else:
    print("not exist")