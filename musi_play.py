import musicalbeeps

player = musicalbeeps.Player(volume = 0.3, mute_output = True)
music_notes = 'G-B-C5-B-C5-B-C5-G-C5-F-G-B-C5-B-C5-B-C5-G-C5-F-E-F-G-E-D-C5-B-C5-G-C5-D5-E5-E5-F5-G5-F5-E5-D5-C5-B-C5-B-C5-G-C5-F-E-F-G-E5-D5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-D5-E5-F5-G5-F5-E5-C5-D5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-D5-E5-F5-G5-F5-E5-C5-D5-C5-B-C5-B-C5-G-C5-F-E-F-G-E-D-G-B-C5-B-C5-B-C5-G-C5-F-E-F-G-E5-D5-E5-D5-C5-B-C5-G-C5-D5-E5-G-E5-F5-G5-F5-E5-D5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-D5-E5-F5-G5-F5-E5-C5-D5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-C5-D5-C5-B-C5-D5-E5-F5-G5-F5-E5-C5-D5'
music_arr = music_notes.split('-')
for i in music_arr:
    # 4 (default) to 5, 5 to 6
    input("Press to play")
    # if len(i) == 1:
    #     i += str(5)
    # else:
    #     i = i[0]+str(6)
    player.play_note(i,0.1)