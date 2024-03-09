# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#date.py Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def imdb55(movies):
    return movies["imdb"] > 5.5
print(imdb55(movies[int(input())]))



#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def above_5_5_movies(movies):
    above55_list = []
    for x in movies:
        if x['imdb'] > 5.5:
            above55_list.append(x['name'])
    return above55_list
list = above_5_5_movies(movies)
for x in list:
    print(x)


#Write a function that takes a category name and returns just those movies under that category.
def category_selector(movies, a):
    category_list = []
    for x in movies:
        if a == x['category']:
            category_list.append(x['name'])
    return category_list
category = category_selector(movies, input("Select category:"))
for x in category:
    print(x)

#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb(movies):
    cnt = 0
    for x in movies:
        cnt += x['imdb']
    cnt = cnt / len(movies)
    return round(cnt,2)
print("Average IMDB:",average_imdb(movies))

#Write a function that takes a category and computes the average IMDB score.
def category_imdb(movies, a):
    cnt = 0
    lencnt = 0
    for x in movies:
        if a == x['category']:
            cnt += x['imdb']
            lencnt += 1
    cnt = cnt / lencnt
    return (cnt)
a = input("Select category")
print("Average IMDB:", category_imdb(movies, a))