def solution(phone_book):
    hash = set(phone_book)
    for p in phone_book:
        temp = ''
        for num in p:
            temp += num
            if temp in hash and p!=temp:
                return False
    return True