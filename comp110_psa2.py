"""
Module: comp110_psa2

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
    applies a fade out to the end of the sound file.
    the sound will diminish slowly and evenly till the end of the
    file. pass in the number of seconds to be affected as the second argument
    to this function(fade_lenghth)
    """
    new_snd = sound.copy(snd)
    fade_length2=int(len(snd)-fade_length)
    factor = 0
    
    for sample in new_snd:
        snd_index = sound.get_index(sample)
        snd_samp = sound.get_sample(new_snd, snd_index)
        if snd_index >=fade_length2:
            sound.set_left(sample,int(sound.get_left(sample)*factor))
            sound.set_right(sample,int(sound.get_right(sample)*factor))
            factor = fade_length2/snd_index
            
        else:
            left = sound.get_left(sample)
            right = sound.get_right(sample)
            sound.set_values(sample, int(left), int(right))

    return new_snd


def fade(snd, fade_length):
    """
    fades in the first part of the song
    and applies a fade out towards the end of the song
    """
    new_snd = sound.copy(snd)
    first=fade_in(new_snd,fade_length)
    new_snd=fade_out(first,fade_length)
    return new_snd


def fade_in_right(snd, fade_length):
    """
    fades in the right channel in the sample continously
    till the end of the sound file.

    """

    new_snd = sound.copy(snd)
    factor = 0

    for sample in new_snd:
        snd_index = sound.get_index(sample)
        snd_samp = sound.get_sample(snd, snd_index)
        if snd_index <= fade_length:
            
            sound.set_right(sample,int(sound.get_right(sample)))
            factor = snd_index/fade_length
            
        else:
            left = sound.get_left(sample)
            right = sound.get_right(sample)
            sound.set_values(sample, int(left), int(right))

    return new_snd

def fade_out_left(snd, fade_length):
    """
    fades out the left channel continuously till the end
    of the sound file.
    """
    new_snd = sound.copy(snd)
    fade_length2=int(len(snd)-fade_length)
    factor = 0
    
    for sample in new_snd:
        snd_index = sound.get_index(sample)
        snd_samp = sound.get_sample(new_snd, snd_index)
        if snd_index >=fade_length2:
            
            sound.set_left(sample,int(sound.get_left(sample)*factor))
            factor = fade_length2/snd_index
            
        else:
            left = sound.get_left(sample)
            right = sound.get_right(sample)
            sound.set_values(sample, int(left), int(right))

    return new_snd


def left_to_right(snd, pan_length):
    """
    The function pans the entire sound starting with a low volume 
    rising to a higher pitch then falling again
    pass in the entire length of the sound as the second argument
    for the function to work.
    """
    new_snd = sound.copy(snd)
    pan_length2 = pan_length-1
    first=fade_out_left(new_snd,pan_length2)
    
    new_snd=fade_in_right(first,pan_length)
    return new_snd
    
