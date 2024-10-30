class Song:
        #! Track total number of songs created using class attributes, use COUNT
    count = 0        #!""Track the total number of songs""  

    # ! List of genre and artist for songs craeted might need 
    genres = []       #!""This is to track unique genre""
    
    # #! Count how many songs belong to each genre, how many songs each artist []
    artists = [] #!""This is to track a list of artist"""

    # #! {} Dictionary for number of songs for genre
    genre_count = {}

    # #! {} Dictionary for number of songs for artist count
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)

  
    @classmethod
    def add_to_artists(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
        cls.artists.append(artist)     

    @classmethod
    def add_to_genres(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
             cls.genre_count[genre] = 1
        if genre not in cls.genres:
            cls.genres.append(genre)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1 #! Incrementing this on count 
        return cls.count
        
    

# problems = Song("99 Problems", "Jay Z", "Rap")
# halo = Song("Halo", "Beyonce", "Pop")
# spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
print("hello")