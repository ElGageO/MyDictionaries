ai_text_file = open('AI.txt', 'r')

ai_text = list(ai_text_file)
ai_text_list = ai_text[0].split()

for word in ai_text_list:
    word = word.rstrip('.')
    word = word.rstrip(',')
    word = word.rstrip(':')
    word = word.rstrip('!')
    word = word.rstrip('?')
    word = word.strip('"')
    
print(ai_text_list)
