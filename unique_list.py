movies = [
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "3 Idiots",
    "Dangal",
    "Drishyam",
    "12th Fail",
    "The Martian",
    "Parasite",
    "Shutter Island",
    "The Martian",
    "The Martian",
    "12th Fail",
    "12th Fail",
    "The Dark Knight",
    "The Dark Knight",
    "Interstellar",
    "Interstellar"
]

unique_list= []

for unique_movie in movies:
    if not unique_movie in unique_list:
        unique_list.append(unique_movie)

print(unique_list)
print(len(unique_list))