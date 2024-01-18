import pandas as pd

# Чтение данных из таблицы (предпологается, что данные находятся в формате CSV)
df = pd.read_csv('data.csv')

# Фильтрация цитат, выпущенных после 1995 года
filtered_quotes = df[df['Year'] > 1995]['Quote'].tolist()

# Вывод списка цитат
for quote in filtered_quotes:
    print(quote)
    
    """
    Предпологается, что данные о фильмах находятся в таблице CSV, которая содержит столбцы Year (год выпуска фильма) и Quotes (цитата из фильма)
    """