# -*- coding: utf-8 -*-

def is_pangram(input):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in input.lower():
        if str(i) in alphabet:
            alphabet.remove(i)
    if alphabet!=[]:
        return False
    else:
        return True

