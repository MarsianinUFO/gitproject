def dec_message(message):
    dict={
'Z':'A',
'Y':'B',
'X': 'C',
'W':'D',
'V':'E',
'U': 'F',
'T': 'G',
'S': 'H',
'R': 'I',
'Q': 'J',
'P': 'K',
'O': 'L',
'N': 'M',
'M': 'N',
'L': 'O',
'K': 'P',
'J': 'Q',
'I': 'R',
'H': 'S',
'G': 'T',
'F':'U',
'E': 'V',
'D': 'W',
'C': 'X',
'B':'Y',
'A':'Z',
    }
    result= ''
    for char in message:
       result+= dict[char.upper()]
    return result