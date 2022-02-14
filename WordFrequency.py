ai_text_file = open('AI.txt', 'r')

ai_text = list(ai_text_file)
ai_text_list = ai_text[0].split()
word_list = []

# use .isalnum() to remove all special chars
for word in ai_text_list:
    temp_str = ''
    if word.isalnum():
        temp_str += word
    else:
        for char in word:
            if char.isalnum():
                temp_str += char
    word = temp_str
    word_list.append(word.lower())

print(word_list)
