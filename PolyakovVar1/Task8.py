letters = ['А', 'В', 'Д', 'П', 'Р']
s = 'AААА'
counter = 0

def check(s):
    return not(s.count('A') == 0 and (s.count('В') == 1 and s.count('Д') == 0 and s.count('П') == 0 and s.count('Р')))

while check(s) == True:
    s = s[1
          :]
    s += letters[counter]
    print(s)
    counter += 1
    if counter == 4:
        counter = 0
