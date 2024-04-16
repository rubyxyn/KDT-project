from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import platform
import matplotlib.pyplot as plt

text = open('test.csv', encoding='utf-8').read()

okt = Okt()
text_tag = []
text_tag = okt.pos(text, norm=True, stem=False)

# print(text_tag)

noun_adj_list = []
for word, tag in text_tag:
    if tag in ['Noun', 'Adjective']: # tag가 명사이거나 형용사인 단어들
        noun_adj_list.append(word)
# print(noun_adj_list)

counts = Counter(noun_adj_list)
print(len(counts))
tags = counts.most_common(300)

if platform.system() == 'Windows':
    path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':	 # Mac OS
    path = r'/System/Library/Fonts/AppleGothic'


wc = WordCloud(font_path=path, background_color='black', colormap='viridis', max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10,8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

