from os import listdir
from os.path import isfile, join
import re

BEGIN_TOKEN = '<%='
END_TOKEN = '%>'

nl = "\n"

conditions = {' ': '', '"': '', "<%=": '', '%>': ''}

inc_files = {}

def trim(include, conditions):
	rep = dict((re.escape(k), v) for k, v in conditions.items())
	pattern = re.compile("|".join(rep.keys()))
	text = pattern.sub(lambda m: rep[re.escape(m.group(0))], include)
	text = text.strip()
	return text

def getlines(f):
	main = open('{0}/{1}'.format(inc_path, f))
	lines = main.readlines()
	main.close()

	print("Got lines for {0}".format(f))

	return lines

def parsehtml(lines):
	line_c = 0
	for line in lines:
		if BEGIN_TOKEN in line and END_TOKEN in line:
			f = trim(line, conditions)
			print("Found Include File: {0}".format(f))
			with open('{0}/includes/{1}'.format(inc_path, f), 'r') as f:
				inc_files[line_c] = f.read()
			lines[line_c] = inc_files[line_c]
			#print(file)
		line_c += 1

inc_path = 'templates~'
files = [f for f in listdir(inc_path) if isfile(join(inc_path, f))]

print(nl)
print("Include Path: {0}".format(inc_path))
print("Parse Conditions: {0}".format(conditions))
print("Files: {0}".format(files))
print(nl)

for f in files:
	lines = getlines(f)
	parsehtml(lines)

	with open(f, 'w') as f:
		f.writelines(lines)