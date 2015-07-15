import hashlib, An
from sys import argv

def md5Checksum(fname, md5_org = '', blockSize = 81920):
	m = hashlib.md5()
	b = 128 * blockSize
	
	try:
		with open(fname, 'rb') as f:
			data = f.read(b)
			while len(data) > 0:
				m.update(data)
				data = f.read(b)
	except IOError:
		print('Error: Can not open file!')
		
	md5 = An.trim(md5_org)
	if md5 == '':
		return m.hexdigest()
	else:
		return m.hexdigest() == md5

if __name__ == '__main__':
	l = len(argv)
	
	if l == 1:
		print('Error: no file input!')
	else:
		fname = argv[1]
		if l == 2:
			print(md5Checksum(fname))
		else:
			fname = argv[1]
			md5_org = argv[2]
			print(md5Checksum(fname, md5_org))