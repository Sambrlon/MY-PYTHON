class Article():
    def __init__(self, content):
        self.content = content


class ArticleExtended(Article):
    def count_symbols(self):
        return len(self.content)

    def count_words(self):
        words = self.content.split()
        return len(words)
    

article = ArticleExtended("""
Ваш баланс равен минималкам - 100 рублей
Ваш номер заблокирован.
Следуйте инструкцуиям для того чтобы передвигать одну ногу за другой,
и вернуть долг обратно в наш замечательный банк.                 
""")


print(article.count_symbols())
print(article.count_words())