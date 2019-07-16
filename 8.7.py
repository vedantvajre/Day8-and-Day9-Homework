def make_album(artist_name, album_title):
    album = {'Artist Name': artist_name, 'Album Title': album_title}
    return(album)


Music = make_album('Michael Jackson', 'Thriller')
print(Music)

Music = make_album(album_title = 'Bad', artist_name = 'Michael Jackson')
print(Music)

Music = make_album('Bruno Mars', '24K Magic')
print(Music)


def make_album(artist_name, album_title, tracks = 0):
    album = {'Artist Name': artist_name, 'Album Title': album_title}
    if tracks:
        album['tracks'] = tracks
    return(album)


Music = make_album('Michael Jackson', 'Thriller')
print(Music)

Music = make_album(album_title='Purpose', artist_name='Justin Bieber', tracks=4)
print(Music)

Music = make_album('Bruno Mars', '24K Magic')
print(Music)