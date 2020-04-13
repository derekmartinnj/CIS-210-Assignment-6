'''
Alphapin encoding
CIS 210 W19 Project 4-1

Author: [Solution]

Credits:  N/A

Encode PINs and other numbers into
easier to remember tone syllables.
'''
import doctest

# shared by multiple functions in this file
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwyz'

def alphapinEncode(pin):
    '''(int) -> str

    converts pin # to an
    easier-to-remember string,
    which is returned

    >>> alphapinEncode(27)
    'hi'
    >>> alphapinEncode(43)
    'lo'
    >>> alphapinEncode(3464408)
    'bomeluco'
    >>> alphapinEncode(3464140)
    'bomelela'
    '''
    tone = ''
    
    wkpin = pin
    while wkpin > 0:
        #retrieve rightmost 2 digits
        plain = wkpin % 100
        wkpin = wkpin // 100

        #get the vowel sound
        vowel = plain % 5
        vsound = vowels[vowel]

        #and the consonant sound
        cons = plain // 5
        csound = consonants[cons]

        #update tone
        tone = csound + vsound + tone

    return tone

def even(i):
    '''
    (int) -> Boolean
    
    Return True if i is an even number.

    >>> even(2)
    True
    >>> even(9)
    False
    '''
    return i % 2 == 0

def checkTone(tone):
    '''(str) -> bool

    Return True if tone is
    in correct (consonant-vowel)
    format, else return False.

    called by: alphapinDecode

    >>> checkTone('lohi')
    True
    >>> checkTone('olih')
    False
    >>> checkTone('')
    False
    >>> checkTone('z')
    False
    '''
    if tone == '':
        return False

    cons_letters = vowel_letters = ''
    
    for i in range(len(tone)):
        if even(i):
            cons_letters += tone[i]
        else:
            vowel_letters += tone[i]
    
    for letter in cons_letters:
        if letter not in consonants:
            return False

    for letter in vowel_letters:
        if letter not in vowels:
            return False

    return True

def checkTone2(tone):
    '''(str) -> bool

    called by: alphapinDecode

    This version - use Python slice
    to create the cons and vowel lists.
    
    Return True if tone is
    in correct (consonant-vowel)
    format, else return False.

    >>> checkTone2('lohi')
    True
    >>> checkTone2('olih')
    False
    >>> checkTone2('')
    False
    >>> checkTone2('z')
    False
    '''
    if tone == '':                      
        return False                    
    
    cons_letters = tone[0:len(tone):2]
    vowel_letters = tone[1:len(tone):2]

    for letter in cons_letters:
        if letter not in consonants:
            return False

    for letter in vowel_letters:
        if letter not in vowels:
            return False

    return True

def alphapinDecode(tone):
    '''(str) -> int

    Decode encoded number tone,
    back to the original number.
    Return the original number.
    If the tone is not correctly
    formatted, print an error
    message and return -1.

    calls: checkTone

    >>> alphapinDecode('lo')
    43
    >>> alphapinDecode('hi')
    27
    >>> alphapinDecode('bomelela')
    3464140
    >>> alphapinDecode('bomeluco')
    3464408
    >>> alphapinDecode('')
    Tone is not in correct format.
    -1
    >>> alphapinDecode('abcd')
    Tone is not in correct format.
    -1
    '''
    phone_num = ''
    
    if checkTone(tone):         #or checkTone2
        while len(tone) > 0:

            # retrieve the first tone
            next_tone = tone[0:2]
            tone = tone[2:]

            # find its position
            cons = next_tone[0]
            vow = next_tone[1]

            num1 = consonants.find(cons)
            num2 = vowels.find(vow)

            # reconstruct this part of the number -
            # multiply (was divided) and add back
            # the remainder from the encryption division.
            phone = (num1 * 5) + num2

            # recreate the number
            # by treating it as a string
            phone = str(phone)
            
            # if single digit, not leading digit, add 0
            if len(phone) == 1 and phone_num != '':
                phone = '0' + phone
            
            phone_num = phone_num + phone

        # but return in original format
        phone_num = int(phone_num)

    else:
        print('Tone is not in correct format.')
        phone_num = -1
    
    return phone_num

def alphapinDecode2(tone):
    '''(str) -> int

    This version: Reconstructing the
    number as an integer - avoid using
    string - yields cleaner code,
    including no special case.
    
    Decode encoded number tone,
    back to the original number.
    Return the original number.
    If the tone is not correctly
    formatted, print an error
    message and return 0.

    calls: checkTone

    >>> alphapinDecode2('lo')
    43
    >>> alphapinDecode2('hi')
    27
    >>> alphapinDecode2('bomelela')
    3464140
    >>> alphapinDecode2('bomeluco')
    3464408
    >>> alphapinDecode2('')
    Tone is not in correct format.
    -1
    >>> alphapinDecode2('abcd')
    Tone is not in correct format.
    -1
    '''
    phone_num = 0
    
    if checkTone2(tone):         #or checkTone
        while len(tone) > 0:

            # retrieve the first tone
            next_tone = tone[0:2]
            tone = tone[2:]

            # find its position
            cons = next_tone[0]
            vow = next_tone[1]

            num1 = consonants.find(cons)
            num2 = vowels.find(vow)

            # reconstruct this part of the number -
            # multiply (was divided) and add back
            # the remainder from the encryption division.
            phone = (num1 * 5) + num2
            phone_num = phone_num * 100 + phone

    else:
        print('Tone is not in correct format.')
        phone_num = -1
    
    return phone_num

def main():
    '''driver for alphapin encode/decode'''
    pin = input('What number would you like to encode? ')
    pin = int(pin)
    
    code = alphapinEncode(pin)
    print(code)
    
    print(alphapinDecode(code))     #or alphapinDecode2
    return None

if __name__ == '__main__':
    main()

#print(doctest.testmod())

#print(alphapinDecode(alphapinEncode(3464140)))
#print(alphapinDecode2(alphapinEncode(3464408)))



        
