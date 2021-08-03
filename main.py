from treelib import Tree
from PIL import Image, ImageFont, ImageDraw

tree=Tree()
tree.create_node('1' , 1)

num=int(input('num: '))

def col(num):
      if num % 2 == 0:
          return num // 2
      else:
          return num * 3 + 1

def run(num):
    numlist=[]
    numlist.append(num)
    while num != 1:
        num = col(num)
        numlist.insert(0,num)

    for i in range(1 , len(numlist)):
        tree.create_node(str(numlist[i]) , numlist[i] , parent=numlist[i-1])

run(num)

text = str(tree)

selected_font = 'arial.ttf'
font_size = 30
fontcolor=(0,0,0)

img = Image.new('RGBA', (0,0), (255, 255, 255,0))
font = ImageFont.truetype(selected_font, font_size)
draw = ImageDraw.Draw(img)
text_size = draw.textsize(text, font)

img = img.resize(text_size)
draw = ImageDraw.Draw(img)
draw.text((0,0), text, fontcolor , font,)
img.save('outputTree.png')










