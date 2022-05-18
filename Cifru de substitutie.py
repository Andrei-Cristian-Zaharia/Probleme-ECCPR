decoded_text = input()
coded_text = ""

list_of_codes = list(map(str, input().split()))
codes = {}

for code in list_of_codes:
    split_code = list(code.split(","))

    codes[split_code[0]] = split_code[1]

for character in decoded_text:
    if character not in codes:
        coded_text += character
    else:
        coded_text += codes[character]

print(coded_text)
