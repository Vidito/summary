from newspaper import Article
import nltk
nltk.download('punkt')

print('Enter URL here: ')
url = input('')
print('\n+++++++++++++++++++++\n')
article = Article(url)
article.download()
article.parse()
author = article.authors
article.nlp()

keywords = article.keywords
summary = article.summary

print("Author: ",author)
print('\n+++++++++++++++++++++\n')
print("Keywords: ",keywords)
print('\n+++++++++++++++++++++\n')
print("Summary: ",summary)





















# print('Enter URL here: ')

# url = input('')
# print('++++++++++++++++++++++++++++++++\n')
# article = Article(url)
# article.download()
# article.parse()
# print("Authors : ",article.authors,'\n')
# print('++++++++++++++++++++++++++++++++\n')
# # print(article.publish_date)
# article.nlp()
# print("Keywords : ",article.keywords,'\n')
# print('++++++++++++++++++++++++++++++++\n')
# print("Summary : ",article.summary)