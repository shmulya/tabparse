import re

def loop_input(msg): # Loop user unput. You can't input empty string
    str = ""
    while str.strip() == "":
        str=raw_input(msg)
    return str

dat = loop_input('Input date as MM.YYYY: ')
while len(dat) != 7:
	dat = loop_input('Invalid date, try again: ')
list = {1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
try:
	file = open(list[int(dat.split('.')[0])]+'.tab','r')
except IOError:
	print 'File with this date is not exist'
else:
	n = 0
	sum = {}

	for str in file:
		if len(str) > 2:
			srch = re.search('\d',str[1])
			if srch != None:
				n = n + 1
				p = re.compile(r'\s{1,5}')
				sum.update ([(n,p.split(str[2:])[1:25])])

	out = open(list[int(dat.split('.')[0])]+'.csv','w')
	out.write('DATE;TIME;RAD\n')
	str = ''

	for k,v in sum.items():
		cn = 0
		while cn<=len(v)-1:
			str = '%s.%s;'%(k,dat)
			if v[cn] == '':
				str = str + '%s:00;0\n'%cn
			else:
				str = str + '%s:00;%s\n'%(cn,v[cn])
			cn = cn + 1
			out.write(str)
	out.close()
