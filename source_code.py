'''
Convert any images to ASCII art using Python
'''

#import the necessary module!
import pywhatkit as kt

print("Let's convert images to ASCII art!")

#Input source path 
print("Enter file name to convert")
source_path = input()

#target_path 
target_path = 'asciify.text'


#call the method
kt.image_to_ascii_art(source_path, target_path)

#2 lines of code

import pywhatkit as kt
kt.image_to_ascii_art('source_path', 'target_path')

