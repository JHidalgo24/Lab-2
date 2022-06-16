import Character

char_list = []
def load_list():
    try:
        filename="data.txt"
        in_file = open(filename,"r")
    except FileNotFoundError:
        print("File not found " + filename)
        raise
    except IOError:
        print("Could not open the file " + filename)
        raise
    else:
        for line in in_file.readlines():
            element = line.split(',')
            if "Ranger" in element[0]:
                char_list.append(Character.Ranger(element[1].replace('"',''),element[2].replace('"',''),element[3].replace('"','').replace("\r","").replace("\n","")))
            elif "Wizard" in element[0]:
                char_list.append(Character.Wizard(element[1].replace('"',''),element[2].replace('"',''),element[3].replace('"','').replace("\r","").replace("\n","")))
            elif "Bard" in element[0]:
                char_list.append(Character.Bard(element[1].replace('"',''),element[2].replace('"',''),element[3].replace('"','').replace("\r","").replace("\n","")))
            elif "Paladin" in element[0]:
                char_list.append(Character.Paladin(element[1].replace('"',''),element[2].replace('"',''),element[3].replace('"','').replace("\r","").replace("\n","")))
            elif "Barbarian" in element[0]:
                char_list.append(Character.Barbarian(element[1].replace('"',''),element[2].replace('"',''),element[3].replace('"','').replace("\r","").replace("\n","")))
            else:
                char_list.append(Character.Character(element[1].replace('"',''),element[2].replace('"','')))
        in_file.close()
def print_list():
    for chr in char_list:
        if isinstance(chr, Character.Ranger):
            print("Ranger " + chr.name + " of family " + chr.family)
        elif isinstance(chr, Character.Wizard):
            print("Wizard " + chr.name + " of the magic family " + str(chr.family))
        elif isinstance(chr, Character.Bard):
            print(chr.name + ' the ' + chr.family + ' Bard')
        elif isinstance(chr, Character.Paladin):
            print(chr.name + ' the Paladin of ' + chr.family)
        elif isinstance(chr, Character.Barbarian):
            print(chr.name + ' the Barbarian of family ' + chr.family)
        else:
            print(chr.name)

if __name__ == '__main__':
    load_list()
    print_list()