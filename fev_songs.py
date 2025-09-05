#file input/output
list_songs = {
        "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber"

        }
def write_songs_file(list_songs , file_name):
    with open(file_name , 'w') as file:
        file.write("Liked Songs:\n")
        for title, artist in sorted(list_songs.items()):
            file.write(f"{title} by {artist}\n")

write_songs_file(list_songs , "songs.txt")  
