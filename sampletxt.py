fw = open('sample.txt','w')
fw.write('testing file concept using python... writing something\n')
fw.write('hey ya !\n')
fw.close()

fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
