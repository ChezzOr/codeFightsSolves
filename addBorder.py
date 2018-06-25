def addBorder(picture):
    lenght = len(picture[0])
    charB = ''
    for y in range(lenght+2):
    	charB += '*' 
    
    for row in range(len(picture)):
        picture[row] = '*' + picture[row] + '*'
    picture.append(charB)
    picture = [charB] + picture
    return picture

if __name__ == '__main__':
	print(addBorder(['ab', 'bc']))