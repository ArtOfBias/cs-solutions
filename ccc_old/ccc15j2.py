# 15 j2

s = input()
a = s.count(':-)')
b = s.count(':-(')
if a > b:
    print('happy')
elif a == 0 and b == 0:
    print('none')
elif a < b:
    print('sad')
elif a == b:
    print('unsure')
