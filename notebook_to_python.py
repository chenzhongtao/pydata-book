

a =s["worksheets"][0]["cells"]

f=open("output","w+")

for i in a:
	if i['cell_type'] == "heading":
		f.write("heading:\n")
		f.write("".join(i["source"]))
		f.write("\n\n")
	elif i['cell_type'] == "code":
		f.write("".join(i["input"]))
		f.write("\n\n")
