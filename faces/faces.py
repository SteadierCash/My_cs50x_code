text = input()

happy = '🙂'

sad = '🙁'

out = ''

for i in range(len(text) - 1):
    if text[i:i+2] == ':)':
        out += '🙂'
    elif text[i:i+2] == ':(':
        out += '🙁'
    elif not (text[i] == ':' and (text[i+1] == '(' or text[i+1] == ')')) and not (text[i - 1] == ':' and (text[i] == '(' or text[i] == ')')):
        out += text[i]

print(out)
