invitList = ['mom', 'dad', 'brother', 'sister1', 'sister2']

print(f"\n\t {invitList[0].upper()} you are invited to dinner")
print(f"\n\t {invitList[1].upper()} you are inited to dinner as well")
print(f"\n\t {invitList[2].upper()} you are also invited to dinner")
print(f"\n\t {invitList[3].upper()} mark you day, you're invited!")
print(f"\n\t {invitList[4].upper()} I understand that you will not be able to make it to the part")

#removed sister2 from list
invitList.remove('sister2')

#aunt going to be indexed where sister2 used to be "4"
invitList.insert(4, 'aunt')
print(f"\n\t {invitList[4].upper()} I will be inviting you instead, due to sister2 not being able to attend")


#string varaible is used for invite message
messageInvi = "notification that you are attending my dinner"

print(f"\n\n\n")

print(f"\n\t {invitList[0].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[1].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[2].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[3].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[4].upper()} {messageInvi.title()}")


print(f"\n\t We will need a bigger table")

invitList.insert(0, 'cousin1')


invitList.insert(3, 'step cousin')
invitList.append('Jason')


print(f"\n\n\nSo this is the final list of people")
print(f"\n\t {invitList[0].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[1].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[2].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[3].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[4].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[5].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[6].upper()} {messageInvi.title()}")
print(f"\n\t {invitList[7].upper()} {messageInvi.title()}")





