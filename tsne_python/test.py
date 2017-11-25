from PIL import Image 

a =Image.open("figure_2.png")
a=a.getdata()
for x in a:
	print(x) 