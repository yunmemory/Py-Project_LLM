data = """
类别	名称	专业类文档编号
C09-01	实体围墙	(EB)1-2,4；(EC)1-2；(ED)1-8；(EE-01)2-3；(EF)1,10-11,6，14-17
		(PC)2-4
		(CL)1-10; (CB)1-13;
C09-02	铁艺围墙	(EB)1-2,4；(EC)1-2；(ED)1-8；(EE-01)2-3；(EF)1,10-11,6，14-17
		(PC)2-4
		(CL)1-10; (CB)1-13;
C09-03	挡土墙	(EB)1-2,4；(EC)1-2；(ED)1-8；(EE-01)2-3；(EF)1,10-11,6，14-17
		(PC)2、4
		(CL)1-10; (CB)1-13;
C09-04	护坡	(EB)1-2,4；(EC)1-2；(ED)1-8；(EE-01)2-3；(EF)1,10-11,6，14-17
		(PC)2-4
		(CL)1-10; (CB)1-13;
"""

lines = data.split("\n")
key = None
for line in lines:
    if not line.strip():
        continue
    if "类别" in line:
        continue
    if "\t" in line:
        parts = line.split("\t")
        key = parts[:2]
        line = parts[2]
    line = line.replace('；', ';')
    parts = line.split(";")
    for part in parts:
        if not part.strip():
            continue
        id, value = part.strip('()').split(')', 1)
        print(f"{key[0]} {key[1]} {id} {value}")
