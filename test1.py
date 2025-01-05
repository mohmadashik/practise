int_str = "Rain"
in_list = ["Red","Run","Apple","India","Total"]
result = {}
for i in int_str:
    result [i] = []
    for word in in_list:
        if word[0].lower() == i.lower():
            result[i].append(word)

print(result)
# S&P Global 
