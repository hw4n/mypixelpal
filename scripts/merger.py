hexLocation = "./artkal_c_colorhex.txt"
nameLocation = "./artkal_c_name.txt"
outputLocation = "../palettes/artkal-c"

result = []

with open(nameLocation) as namefile:
    for line in namefile.readlines():
        result.append(line.rstrip())

idx = 0

with open(hexLocation) as hexfile:
    for line in hexfile.readlines():
        result[idx] += ',' + line.rstrip()
        idx += 1

with open(outputLocation, 'w') as outputfile:
    for namecolor in result:
        outputfile.write("%s\n" % namecolor)
