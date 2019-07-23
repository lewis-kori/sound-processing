"""
Module: comp110_psa2

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

import sound

def remove_vocals(snd):
    """
    This function removes the vocals from a song and returns a new sound with only the 
    instrumentals playing in the background.

    By setting both the left and right samples from the original sound to a floor division
    of the difference(subtraction) in left and right samples from the original sound, 
    the function is able to achieve this.

    All this is done without altering the original sound.it insteads makes a copy of the original 
    and returns an altered version of this copy.
    """
    new_snd=sound.copy(snd)
    for sample in new_snd:
        sound.set_left(sample,int((sound.get_left(sample)-sound.get_right(sample))//2))
        sound.set_right(sample,int((sound.get_left(sample)-sound.get_right(sample))//2))

    return new_snd

    
def fade_in (snd, fade_length):
    """
    The function applies a fade to the beginning of the sound file
    upto the specified number of seconds(index). This is the second argument to 
    the function(fade_lenght). 
    the sound then returns the volume to normal volume.

    """

    new_snd = sound.copy(snd)
    factor = 0

    for sample in new_snd:
        snd_index = sound.get_index(sample)
        snd_samp = sound.get_sample(snd, snd_index)
        if snd_index <= fade_length:
            sound.set_left(sample,int(sound.get_left(sample)*factor))
            sound.set_right(sample,int(sound.get_right(sample)*factor))
            factor = snd_index/fade_length
            
        else:
            left = sound.get_left(sample)
            right = sound.get_right(sample)
            sound.set_values(sample, int(left), int(right))

    return new_snd

def fade_out(snd, fade_length):
    """
    Replace this with a good docstring comment.
    """
    new_snd = sound.copy(snd)
    factor = 0

    for sample in new_snd:
        snd_index = sound.get_index(sample)
        snd_samp = sound.get_sample(new_snd, snd_index)
        if snd_index >=fade_length:
            sound.set_left(sample,int(sound.get_left(sample)*factor))
            sound.set_right(sample,int(sound.get_right(sample)*factor))
            factor = fade_length/snd_index 
            
        else:
            left = sound.get_left(sample)
            right = sound.get_right(sample)
            sound.set_values(sample, int(left), int(right))

    return new_snd


def fade(snd, fade_length):
    """
    Replace this with a good docstring comment.
    """

    # Remove this comment and the next line and put your function
    # implemtnation here.
    return None


def left_to_right(snd, pan_length):
    """
    Replace this with a good docstring comment.
    """

    return None


# Your final submission should NOT contain any "top level" code.
# In other words, it should only contain the function definitions above.
# Use the REPL to test your code instead.
