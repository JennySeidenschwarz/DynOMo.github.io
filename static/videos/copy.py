import os
import glob
import shutil


p = 'Visualization/iphone/*/*/*'
p = 'Visualization/panoptic_sport/*/*/*'
p = 'Visualization/davis/*/*/*'

for f in glob.glob(p):
	try:
		print(f)
		print('../../../' + '/'.join(f.split('/')[:-2]) + '/eval/' + '/'.join(f.split('/')[-2:]))
		print()
		shutil.copyfile('../../../' + '/'.join(f.split('/')[:-2]) + '/eval/' + '/'.join(f.split('/')[-2:]), f)
	except:
		pass


