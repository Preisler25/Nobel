class Adatok:
    def __init__(self, line):
        self.year = int(line[0])
        self.type = line[1]
        self.k_name = line[2]
        self.v_name = line[3]

def ImportFromTXT(filename):
    temp = []
    f = open(filename, "r", encoding="utf-8").read()
    lines = f.strip().split("\n")
    for i in range(1, len(lines)):
        temp.append(Adatok(lines[i].split(";")))
    return temp

def f3(list):
    for i in list:
        if i.k_name == "Arthur B.":
            return i.type

def f4(list):
    for i in list:
        if i.year == 2017 and i.type == "irodalmi":
            return f"{i.k_name} {i.v_name}"

def f5(list):
    temp = ""
    for i in list:
        if i.year > 1990 and i.type == "béke" and i.v_name == "":
            temp += f"\n\t{i.year}: {i.k_name}"
    return temp

def f6(list):
    temp = ""
    for i in list:
        if "Curie" in i.v_name:
            temp += f"\n\t{i.year}: {i.k_name} {i.v_name}({i.type})"
    return temp

def f7(list):
    temp = f""
    typeMap = dict()
    for i in list:
        if i.type not in typeMap:
            typeMap[i.type] = 0
        typeMap[i.type] += 1
    for key in typeMap:
        temp += f"\n\t{key}:             {typeMap[key]} db"
    return temp

def f8(list):
    temp = ""
    for i in list:
        if i.type == "orvosi":
            temp += f"{i.year}: {i.k_name} {i.v_name}\n"
    WriteToTXT("orvosi.txt", temp)

def WriteToTXT(filename, text):
    f = open(filename, "w", encoding="utf-8")
    f.write(text)

def main():
    lines = ImportFromTXT("nobel.csv")
    print(f"3. feladat: {f3(lines)}")
    print(f"4. feladat: {f4(lines)}")
    print(f"5. feladat: {f5(lines)}")
    print(f"6. feladat: {f6(lines)}")
    print(f"7. feladat: {f7(lines)}")
    print(f"8. feladat: orvosi.txt")
    f8(lines)
main()