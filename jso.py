import json
with open(r'E:\.Học\VS code\project\json\2a.json','r') as a_file:
    caua = json.load(a_file)
print('Ten: ',caua['ten'],' Tuoi: ',caua['tuoi'],' Thanh pho: ',caua['thanhpho'])

movies = [
    {"title": "Inception", "year": 2010, "director": "Christopher Nolan", "revenue": 828.4},
    {"title": "The Dark Knight", "year": 2008, "director": "Christopher Nolan", "revenue": 1005},
    {"title": "The Shawshank Redemption", "year": 1994, "director": "Frank Darabont", "revenue": 58.3},
    {"title": "Pulp Fiction", "year": 1994, "director": "Quentin Tarantino", "revenue": 213.9},
    {"title": "The Godfather", "year": 1972, "director": "Francis Ford Coppola", "revenue": 245},
    {"title": "The Godfather Part II", "year": 1974, "director": "Francis Ford Coppola", "revenue": 48},
    {"title": "The Lord of the Rings: The Return of the King", "year": 2003, "director": "Peter Jackson", "revenue": 1140},
    {"title": "Forrest Gump", "year": 1994, "director": "Robert Zemeckis", "revenue": 678.2},
    {"title": "The Matrix", "year": 1999, "director": "The Wachowskis", "revenue": 463.5},
    {"title": "Interstellar", "year": 2014, "director": "Christopher Nolan", "revenue": 677.5}
]
trungbinh=0
max=0
for i in range(len(movies)):
    print(movies[i].get('title'),': ',movies[i].get('revenue'))
    if int(movies[i].get('year'))>=max: max=int(movies[i].get('year'))
    else: max = max
    trungbinh+=movies[i].get('revenue')
trungbinh/=len(movies)
print('Doanh thu trung binh cac bo phim',trungbinh)
print('Bo phim cong chieu gan nhat: ', max)

import json
with open('need_to_process.json','r') as json_file:
    cauc=json.load(json_file)
output=[]
for annotation in cauc["annotations"]:
    for result in annotation["result"]:
        if result["from_name"] == "transcription":
            a = result["value"]["text"][0]
            b = result["value"]["points"]
            dict = {
                "transcription":a,
                "points":b
            }
            output.append(dict)
with open('2c.txt','w') as w_file:
    w_file.write(str(output))


