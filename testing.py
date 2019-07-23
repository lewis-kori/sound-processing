import sound
import comp110_psa2

#uncomment the sections to play

# remove vocals section
love=sound.Sound('love.wav')

new_love=comp110_psa2.remove_vocals(love)

new_love.play()
new_love.save()
new_love.stop()

# fade in for the first 4 seconds
"""water=sound.Sound('water.wav')
new_water = comp110_psa2.fade_in(water,176400)
new_water.play()
new_water.save()
new_water.stop()"""

# fade out the last 4 seconds, you can set the value to however long you want

"""rain=sound.Sound('rain.wav')

new_rain=comp110_psa2.fade_out(rain,int(len(love)-176400))

new_love.play()
new_love.save()
new_love.stop()"""

