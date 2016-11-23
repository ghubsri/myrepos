text = "TELUGU"
rev = ''
print "Given string:", text
print "Length: ", len(text)
for i in range(len(text), 0, -1):
   rev = rev + text[i-1]
print "Reversed string: ", rev
