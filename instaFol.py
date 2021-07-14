#/usr/bin/env python3
#############
#           #
# RentixEli #
#           #
#############
with open('followingme.txt', 'r') as followers:
	with open('ifollow.txt', 'r') as following:
		following = following.readlines()
		followers = followers.readlines()
		
		fol = []
		ifol = []
		for i in followers:
			fol.append(i.strip('\n'))

		for i in following:
			ifol.append(i.strip('\n'))


fol_new = []
ifol_new = []
for i in fol:
	if i not in ifol:
		fol_new.append(i)
for i in ifol:
	if i not in fol:
		ifol_new.append(i)


		
print ('Following me but I don\'t follow them: ', len(fol_new), '\n', ', '.join(fol_new))
print ('\n')
print ('I follow them but they not me: ', len(ifol_new), '\n', ', '.join(ifol_new))
