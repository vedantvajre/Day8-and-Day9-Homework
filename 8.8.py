def make_album(artist_name, album_title, tracks=0):
    album = {'Artist Name': artist_name, 'Album Title': album_title}
    if tracks:
        album['tracks'] = tracks
    return(album)


artist_prompt = "\nPlease enter an artist."
album_prompt = "\nWhat album has this artist made?"
track_prompt = "\nHow many tracks does this album have?"
print("Type quit at any time to stop.")
while True:
    artist_input = input(artist_prompt)
    if artist_input == 'quit' or 'Quit':
        break
    else:
        print("Ok!")

    album_input = input(album_prompt)
    if album_input == 'quit' or 'Quit':
        break
    else:
        print("Ok!")

    track_input = input(track_prompt)
    track_input = int(track_input)
    if track_input == 'quit' or 'Quit':
        break
    else:
        print("Ok!")

    finished_album = make_album(artist_input, album_input, track_input)
    print(finished_album)
