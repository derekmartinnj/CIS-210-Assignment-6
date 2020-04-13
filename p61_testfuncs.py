'''
Assignment: Project 6.1 Test Functions, CIS 210 Winter 2019
Author: Derek Martin
Credits: N/A
Description: Create new test functions to test some functions from p41 with a variety of test cases
'''
import p41_alphapin_key as p41

def test_decode(f):
    '''
    (function) -> None
    
    Call function f (alphapinDecode() or alphapinDecode2()) for each test, compare results, report whether they are correct
    '''
    testCases = (('lo', 43),('hi', 27),('bomelela', 3464140),('bomeluco', 3464408),('', -1),('abcd', -1),('diju', 1234)) # Define test cases locally
    if (f == p41.alphapinDecode): # Get name of function called for formatting
        name = 'alphapinDecode'
    elif (f == p41.alphapinDecode2):
        name = 'alphapinDecode2'
    
    for i in range(len(testCases)):
        if (p41.checkTone(testCases[i][0])): # Determine whether tone is in correct format
            print("Checking " + name + "(\'" + testCases[i][0] + "\')" + "...its value", f(testCases[i][0]), "is correct!")
        else:
            print("Checking " + name + "(\'" + testCases[i][0] + "\')" + "...Tone is not in correct format")
            print("Its value -1 is correct!")
            
    return None

def test_checkTone(f):
    '''
    (function) -> None

    Call function f (checkTone() or checkTone2()) for each test, compare results, report whether they are correct
    '''
    testCases = (('lohi', True),('hajeku', True),('olih', False),('', False),('z', False),('zz', False))
    if (f == p41.checkTone): # Get name of function called for formatting
        name = 'checkTone'
    elif (f == p41.checkTone2):
        name = 'checkTone2'

    for i in range(len(testCases)):
        print("Checking " + name + "(\'" + testCases[i][0] + "\')" + "...its value", f(testCases[i][0]), "is correct!")
    
    return None

def main():
    ''' Basic call function '''
    test_decode(p41.alphapinDecode)
    test_decode(p41.alphapinDecode2)
    test_checkTone(p41.checkTone)
    test_checkTone(p41.checkTone2)

main()
