# This function takes a parameter for melakartha raaga number x between 1 and 72, and returns a list of notes like sa, ri2, ga3, ma1, pa, da1, ni2
def melakartha_raaga_number_to_notes(x):
    if isinstance(x, int) and x>=1 and x<=72:
        notes=['sa', '', '', '', 'pa', '', '']
        if x>36:
            notes[3]='ma2'
        else:
            notes[3]='ma1'

        q=x//6;r=x%6

        if r == 1:
            notes[5]='da1'
            notes[6]='ni1'
        elif r == 2:
            notes[5]='da1'
            notes[6]='ni2'
        elif r==3:
            notes[5]='da1'
            notes[6]='ni3'
        elif r == 4:
            notes[5]='da2'
            notes[6]='ni2'
        elif  r==5:
            notes[5]='da2'
            notes[6]='ni3'
        else:
            notes[5]='da3'
            notes[6]='ni3'

        if r==0:
            chakra=q
        else:
            chakra=q+1

        if chakra<=6:
            ri_ga_number=chakra
        else:
            ri_ga_number=chakra-6

        if ri_ga_number==1:
            notes[1]='ri1'
            notes[2]='ga1'
        elif ri_ga_number==2:
            notes[1]='ri1'
            notes[2]='ga2'
        elif ri_ga_number==3:
            notes[1]='ri1'
            notes[2]='ga3'
        elif ri_ga_number==4:
            notes[1]='ri2'
            notes[2]='ga2'
        elif ri_ga_number==5:
            notes[1]='ri2'
            notes[2]='ga3'
        else:
            notes[1] = 'ri3'
            notes[2] = 'ga3'
    else:
        print('Give correct raaga number (integer) from 1 and 72, not ', x)
        return

    print('Notes for raaga number', x , ' : ', notes)
    return notes


# Given the notes like sa, ri2, ga3, ma1, pa, da1, ni2  the function returns melakartha raaga number (sa, pa there are no variations, so do not need to pass parameters)
def notes_to_melakarta_raaga_number(ri, ga, ma, da, ni):

    if ma==1 or ma==2:
        ma_number = ma
    else:
        print('give correct ma notes. ')
        return

    if ri ==1 and ga == 1:
        ri_ga_number = 1
    elif ri ==1 and ga == 2:
        ri_ga_number = 2
    elif ri == 1 and ga == 3:
        ri_ga_number = 3
    elif ri == 2 and ga == 2:
        ri_ga_number = 4
    elif ri == 2 and ga == 3:
        ri_ga_number = 5
    elif ri == 3 and ga == 3:
        ri_ga_number = 6
    else:
        print('give correct ri, ga notes. '  )
        return

    if da==1 and ni == 1:
        da_ni_number = 1
    elif da ==1 and ni == 2:
        da_ni_number = 2
    elif da ==1 and ni == 3:
        da_ni_number = 3
    elif da ==2 and ni == 2:
        da_ni_number = 4
    elif da ==2 and ni == 3:
        da_ni_number = 5
    elif da == 3 and ni == 3:
        da_ni_number = 6
    else:
        print('give correct da, ni notes. ')
        return


    raaga_number = (ma_number-1)*36+(ri_ga_number-1)*6+da_ni_number
    print('raaga_number =', raaga_number)
    return raaga_number


melakartha_raaga_number_to_notes(73)
melakartha_raaga_number_to_notes(72)
melakartha_raaga_number_to_notes(13)
melakartha_raaga_number_to_notes(36)
melakartha_raaga_number_to_notes(37)

notes_to_melakarta_raaga_number(ri=2, ga=1, ma=1, da=3, ni=3)
notes_to_melakarta_raaga_number(ri=3, ga=3, ma=2, da=3, ni=3)
notes_to_melakarta_raaga_number(ri=1, ga=3, ma=1, da=1, ni=1)
notes_to_melakarta_raaga_number(ri=3, ga=3, ma=1, da=3, ni=3)
notes_to_melakarta_raaga_number(ri=1, ga=1, ma=2, da=1, ni=1)

