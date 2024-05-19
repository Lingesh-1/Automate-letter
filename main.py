# with open('starting_letter.txt','w') as f:
#     f.write("Dear [name],\nYou are invited to my brithday this Saturday.\nHope you can make it!\nLingesh")

# with open('name.txt','w') as f:
#     f.write("varsha\nselva\nmark\nsudar")
PLACEHOLDER="[name]"

with open('name.txt','r') as re:
    h=re.readlines()
    # print(h)
with open('starting_letter.txt','r') as j:
    k=j.read()
    for i in h:
        striped=i.strip()
        new=k.replace(PLACEHOLDER,striped)
        # print(new)
        with open(f'/Users/linge/Desktop/letterpy/letter_{striped}_b.txt','w') as s:
            s.write(new)











# names=['varsha','selva','mark','sudar']
# with open('starting_letter.txt') as f:
#     g=f.read()
#     for i in names:
#         new=g.replace(PLACEHOLDER,i)
#         # print(new)
#         with open(f'letter_{i}.txt','w') as j:
#             j.write(new)
            

