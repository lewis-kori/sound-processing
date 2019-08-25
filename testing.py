import sound
import comp110_psa2

#uncomment the sections to play

# remove vocals section
"""love=sound.Sound('love.wav')
love.play()
new_love=comp110_psa2.remove_vocals(love)
love.stop()
new_love.play()
new_love.save()
new_love.stop()"""

"""# fade in for the first 4 seconds
water=sound.Sound('water.wav')
new_water = comp110_psa2.fade_in(water,176400)
new_water.play()
new_water.save()
new_water.stop()"""

# fade out the last 4 seconds, you can set the value to however long you want

"""rain=sound.Sound('rain.wav')

new_rain=comp110_psa2.fade_out(rain,176400)

new_rain.play()
new_rain.save()
new_rain.stop()"""

# fade the entire song
"""grace=sound.Sound('grace.wav')

new_rain=comp110_psa2.fade(grace,176400)

new_rain.play()
new_rain.save()
new_rain.stop()"""

#pan left_right
"""
airplane = sound.Sound('airplane.wav')
new_plane =comp110_psa2.left_to_right(airplane,len(airplane))
new_plane.play()
new_plane.save()
new_plane.stop()"""
