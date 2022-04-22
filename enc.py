import marshal, zlib, base64, os, sys

try:
    r = sys.argv[1]
except:
    exit('Usage: py2 enc.py file.py')

if not os.path.isfile(r):
    exit('File Not Found Error')

a = open(r).read()
b = marshal.dumps(a)
c = zlib.compress(b)
d = base64.b64encode(c)

sv = 'import marshal, zlib, base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("{}"))))'

open('hasil.py','w').write(sv.format(d))
exit('Compiled: saved to hasil.py')
