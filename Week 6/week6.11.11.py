s = ' ' + input('Enter a string: ').strip()
for i in range(len(s)):
 if s[i] == ' ':
    s = s[:i + 1] + s[i + 1].upper() + s[i + 2:]
    print('Capitalized: ', s.strip())