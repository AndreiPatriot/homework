def all_variants(text):
    j = len(text)
    for i in range(j):
        for end in range(i + 1, j + 1):
            yield text[i:end]


# a = all_variants("abc")
# for start in a:
#     print(start)
a = all_variants("abc")
for i in a:
    print(i)
