ai_text_file = open('AI.txt', 'r')

ai_text = list(ai_text_file)
ai_text_list = ai_text[0].split()
word_list = []

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

word_counter_dict = {}

for word in word_list:
    word_count = word_list.count(word)
    word_counter_dict[word] = word_count

for word in word_counter_dict:
    print(word, word_counter_dict[word])
