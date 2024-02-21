import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title : str
    Original_title: str 
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json ='''
{
 "title":"O Senhor Do Anéis: A Sociedade do Anel",
 "Original_title": "The Lord of The Rings:The Fellowship of the Ring",
 "is_movie": true,
 "imdb_rating":8.8,
 "year": 2001,
 "characters":["Frodo","Sam","Gandald","Legolas","Boromir"],
 "budget": null
}
'''
filme:Movie = json.loads(string_json)
# pprint(filme)
# print(filme['title'])
# print(filme['characters'][0])
# print(filme['year']+10)
json_string = json.dumps(filme,ensure_ascii=False,indent=2)
print(json_string)