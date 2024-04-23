import sys
import locale

PY2 = sys.version_info[0] == 2

if PY2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

try:
    reload(sys)
except NameError:  # Python 3
    pass


def main():
   if PY2:
       encoding = locale.getdefaultlocale()[1]
   else:
       encoding = locale.getencoding()

   if not encoding:
       return False

   textmap = {
       "cp936": "\u4e2d\u6587",
       "cp1252": "Lat\u012Bna",
       "cp932": "\u306b\u307b\u3093\u3054",
   }

   if encoding in textmap:
       print(textmap[encoding])
   return True


if __name__ == "__main__":
    print(main())
