import os
import sys
from astropy.io import ascii
from pylab import *
from random import *


dept_dict = {'RO' : 'Radio Observatory',
			 'RO / SDOS' : 'Radio Observatory',
			 'NOVA - METIS' : 'NOVA',
			 'R&D' : 'Research & Development',
			 'Radio Observatory' : 'Radio Observatory',
			 'AG' : 'Astronomy Group',
			 'Algemene Zaken' : 'Algemene Zaken',
			 'AZ' : 'Algemene Zaken',
			 'ATH/R&D' : 'Research & Development',
			 'FAZ' : 'Algemene Zaken', 
			 'NOVA Optical & IR Instrumentation Group' : 'NOVA',
			 'R&D, radio group' : 'Research & Development',
			 'ASTRON emeritii' : 'ASTRON Emeritii',
			 'DG' : 'Directie',
			 'SDOS' : 'Radio Observatory',
			 'Radio observatory (software support)' : 'Radio Observatory',
			 'Astronomy group': 'Astronomy Group',
			 'R&D / General Affairs' : 'Research & Development',
			 'General Affairs' : 'General Affairs',
			 'Astronomy Group' : 'Astronomy Group',
			 'Astronomy Group (AG)' : 'Astronomy Group',
			 'R&D Computing Group' : 'Research & Development',
			 'R&D DESP' : 'Research & Development',
			 'Radio Obs' : 'Radio Observatory'
}

d = ascii.read('Secret Sinta Enrolment Quiz! (Responses) - Form Responses 1.csv')
print(d.keys())

# Departments
#print(list(set(d['Which department do you work in?'])))

totnum = len(d)
print(totnum)

# Overall dict to measure distribution
odict = {}
loopnum = 1

for i in range(0,loopnum):

	matched = 0
	goodmatch = False

	counter = 0

	while goodmatch != True:

		print(counter)

		sintas = []
		sintaed = []
		mdict = {}

		# Assign everyone a secret sinta
		while matched != totnum:

			person1 = randint(0,len(d)-1)
			secretsinta = randint(0,len(d)-1)

			name1 = d['Please enter your name:'][person1]
			name2 = d['Please enter your name:'][secretsinta]

			#print(name1,name2)

			# First stage, must not be themselves
			if person1 != secretsinta:

				# Should not be in same department
				if (name1 not in sintaed) and (name2 not in sintas):
					mdict[person1] = secretsinta

					sintas.append(name2)
					sintaed.append(name1)
					matched+=1

			elif person1 == secretsinta and (matched == (totnum) or matched == (totnum-1)):
				print('Got stuck! Need to reset...')
				sintas = []
				sintaed = []
				mdict = {}	
				matched=0
			# else:
			# 	print('Some other kind of error...')
			# 	print(name1,name2,matched,totnum)		

			counter+=1

		# Now that it is matched, verify the matches
		diffdept = 0
		for key in mdict:
			dept1 = dept_dict[d['Which department do you work in?'][key]]
			dept2 = dept_dict[d['Which department do you work in?'][mdict[key]]]

			if dept1 != dept2:
				diffdept +=1

		# Reverse matches (e.g. who has each other)
		revmatch = 0
		for key in mdict:

			if key == mdict[mdict[key]]:
				revmatch+=1

		print('Number of reverse matches:',revmatch)
		print('Fraction of different departments: %.2f' % (diffdept/totnum))

		#print('Different department matches: %s' % diffdept)

		# Maybe not possible but aim for 85%
		if diffdept/totnum > 0.85 and revmatch == 0:
			goodmatch = True
			print(mdict)
		else:
			matched = 0

	for key in mdict:
		#print ('Secret Sinta %s has: %s' % (d['Please enter your name:'][mdict[key]],d['Please enter your name:'][key]))
		print ('Secret Sinta %s (%s) has: %s (%s)' % (mdict[key],dept_dict[d['Which department do you work in?'][mdict[key]]],key,dept_dict[d['Which department do you work in?'][key]]))
		if mdict[key] not in odict:
			odict[mdict[key]] = [key]
		else:
			odict[mdict[key]].append(key)

	print('ITERATION %i!!!' % i)

print (odict)
keys = list(odict.keys())
keys.sort()

out = open('sintamatches.txt','w')
out.write('sinta|sinta_email|sintee\n')

for key in keys:

	sinta = d['Please enter your name:'][key]
	sintee = d['Please enter your name:'][odict[key][0]]
	sinta_email = d['Email address:'][key]
	print('Sinta %s has Sintee %s' % (sinta,sintee))
	out.write('%s|%s|%s\n' % (sinta,sinta_email,sintee))
	out.flush()




# # Plot the results of looping
# keys = list(odict.keys())
# keys.sort()

# for i in range(0,len(keys)):
# 	scatter(keys[i]*ones(len(odict[keys[i]])),odict[keys[i]],marker='o',facecolor=cm.Spectral(i/len(keys)),edgecolor='k',alpha=0.5,linewidth=1)   

# xlabel('Secret Sinta')
# ylabel('Secret Sintee')
# grid(True,alpha=0.3)
# title('Distribution of Secret Sintas for %i loops' % loopnum)
# savefig('secretsinta_model.pdf',bbox_inches='tight')




