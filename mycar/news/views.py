import os
from django.shortcuts import render
import aiohttp

from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('API_KEY')


async def news_list(request):
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='
           + api_key)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            news = await response.json()

    a = news['articles']
    author = []
    desc = []
    title = []
    img = []
    cont = []
    for i in range(len(a)):
        f = a[i]
        author.append(f['author'])
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        cont.append(f['content'])

    mylist = zip(author, title, desc, img, cont)
    context = {'mylist': mylist}

    return render(request, 'news/news_list.html', context)
