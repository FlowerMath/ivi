import numpy as np
import pandas as pd

col_names = ["user_id", "operator_name", "content_id", "content_title", "show_duration"]

# читаем из подготовленного csv
content_watch = pd.read_csv('./content_watch.csv',
                            sep='\t',
                            header=None,  # можно не передавать, если в файле есть заголовки столбцов
                            names=col_names)

male_prob = 0.4
content_watch["gender"] = np.random.binomial(1, male_prob, content_watch.shape[0])

content_watch['content_id'] = content_watch['content_id'].astype('object')
content_watch['user_id'] = content_watch['user_id'].astype('object')
content_watch['show_duration'] = content_watch['show_duration'].replace({'None': 0})
content_watch['show_duration'] = content_watch['show_duration'].astype('int')

# Определяем самые популярные фильмы
print(content_watch[content_watch['show_duration'] != 0].groupby(by='content_title')['user_id'] \
      .agg('nunique') \
      .sort_values(ascending=False).head(5))
# Определяем пользователей с наибольшим числом просмотров
print(content_watch[content_watch['show_duration'] != 0].groupby(by='user_id')['content_title'] \
      .agg('nunique') \
      .sort_values(ascending=False).head(5))

# Определяем самых популярных операторов
print(content_watch.groupby('operator_name')['user_id'] \
      .agg('nunique') \
      .sort_values(ascending=False).head(5))

# Определяем средний показатель просмотров среди мужчин - пользователей Rostelecom
print(content_watch[(content_watch['gender'] == 1) & (content_watch['operator_name'] == 'Rostelecom')] \
      .groupby('user_id')['content_title'].agg('count').mean())

# Строим user_item
user_item = pd.DataFrame(content_watch.groupby('user_id')['content_id'] \
                         .apply(lambda x: list(np.unique(x))))

print(user_item.head(5))
