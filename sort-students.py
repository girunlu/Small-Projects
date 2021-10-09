lstd=[{"Name":"zahmet","Department":"Chemistry"}
             ,{"Name":"esra","Department":"Physics"}, {"Name":"melih", "Department":"EE"}
             ,{"Name":"asli","Department":"Chemistry"},{"Name":"bilge","Department":"Physics"}
             ,{"Name":"pazartesi", "Department":"EE"},{"Name":"sali", "Department":"EE"}
             ,{"Name":"leyla", "Department":"Physics"},{"Name":"giray", "Department":"Chemistry"}]

## deps list
deps = [i["Department"] for i in lstd]
deps = set(deps)

## students to dep file func
def addfile(dic):
    flex = ".txt"
    flnme = dic["Department"]
    with open(flnme+flex,"a") as f:
        f.write(dic["Name"]+"\n")

#for each dep file, sort students
def sortfile(dep):
    flex = ".txt"
    with open(dep+flex,"r") as f:
        lines = f.readlines()
        lines.sort()
        open(dep+flex,"w")
        for i in lines:
            f2 = open(dep+flex,"a")
            f2.write(i)
    
##for each element in stu list
for i in lstd:
    addfile(i)

##sort for each dep file
for i in deps:
    sortfile(i)
