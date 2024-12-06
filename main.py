def  all_variants(text):
    for j in range (len(text)):
        for k in range (j, len (text)):
            yield text [j : k + 1]

a = all_variants("abc")
for i in a:
    print(i)
