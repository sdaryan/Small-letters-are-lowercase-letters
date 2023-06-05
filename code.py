#Small letters are lowercase letters.
#اگر کلمه ای تعداد حروف بزرگش از تعداد حروف کوچیکش بیشتر بود کل کلمه رو با حروف بزرگ می نویسه در غیر این صورت کل کلمه رو با حروف کوچیک می نویسه.

def change_case(word):
    count_upper = 0
    count_lower = 0
    for char in word:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    if count_upper > count_lower:
        return word.upper() # کلمه را با حروف بزرگ نمایش دهیم
    else:
        return word.lower() # کلمه را با حروف کوچک نمایش دهیم

print(change_case(input()))