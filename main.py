from os import listdir
from os.path import isfile, join
import re

BEGIN_TOKEN = '<%='
END_TOKEN = '<%='

conditions = {' ': '', '"': '', "<%=": '', '%>': ''}

inc_files = {}

def trim(include, conditions):
	rep = dict((re.escape(k), v) for k, v in conditions.iteritems())
	pattern = re.compile("|".join(rep.keys()))
	text = pattern.sub(lambda m: rep[re.escape(m.group(0))], include)
	text = text.strip()
	return text

def getlines(file):
	main = open('templates/{0}'.format(file))
	lines = main.readlines()
	main.close()

	return lines

def parsehtml(lines):
	line_c = 0
	for line in lines:
		if BEGIN_TOKEN in line and END_TOKEN in line:
			file = trim(line, conditions)
			with open('templates/includes/{0}'.format(file), 'r') as f:
				inc_files[line_c] = f.read()
			lines[line_c] = inc_files[line_c]
			#print(file)
		line_c += 1

inc_path = 'templates'
files = [f for f in listdir(inc_path) if isfile(join(inc_path, f))]

for file in files:
	lines = getlines(file)
	parsehtml(lines)

	with open(file, 'w') as f:
		f.writelines(lines)