
def word_count(s):
    count_items={}
    for i in s:
        count_items[i]=s.count(i)
    return count_items
print(word_count("programming"))