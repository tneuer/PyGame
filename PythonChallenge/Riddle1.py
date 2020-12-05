# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:09:33 2016

@author: Spider Schwein
"""

#Move every letter by two steps

def decode(text):
    readable = ""
    key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in text:
        if letter not in key:
            readable += letter
        else:
            readable += key[(key.index(letter)+2)%26]
    return readable
    
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(decode(text))
print(decode("pythonchallenge.com/pc/def/map"))

#Solution http://www.pythonchallenge.com/pc/def/ocr.html