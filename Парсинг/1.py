import re
from collections import Counter


def coutn_words(file_path, num_words):
    with open(file_path, 'r') as file:
        text = file.read()
        
    # Приводим текст к нижнему регистру и удаляем предлоги
    text = re.sub(r'\b\w{1,3}\b', '', text.lower())
    
    # Используем регулярное выражение для разделения текста на слова
    words = re.findall(r'\b\w+\b', text)
    
    # Считаем количество упоминаний каждого слова
    word_counts = Counter(words)
    
    # Возвращаем наиболее встречаемые слова
    return word_counts.most_common(num_words)
    
    
file_path = 'kolobok.txt'  # Путь к файлу с текстом сказки "Колобок"
num_words = 10  # Количество слов, которые нужно найти

print(count_words(file_path, num_words))