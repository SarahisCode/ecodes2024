def toCoord(textpair):
    return [int(i.split("=")[1]) for i in textpair.strip().split(" ")]

with open("input3.txt", "r") as a:
    snails = [toCoord(line) for line in a.readlines()]

mod_list = [(i[1]-1, i[0]+i[1]-1) for i in snails]
cur_num = mod_list[0][0]
cur_mod = mod_list[0][1]
for new_mod in mod_list[1:]:
    num_to_hit = new_mod[0]
    modulus = new_mod[1]
    while cur_num%modulus != num_to_hit:
        cur_num += cur_mod
    cur_mod *= modulus

print(cur_num)