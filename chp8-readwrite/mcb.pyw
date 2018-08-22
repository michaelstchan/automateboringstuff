#! python3
 # mcb.pyw - Saves and loads pieces of text to the clipboard.
 # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword. 
 #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 #        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
print (sys.argv, len(sys.argv))

if len(sys.argv) > 3:
    print('Usage: python mcb.pyw save/list/chosen-keyword')
if (len(sys.argv) == 3) and (sys.argv[1] == 'save'):
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('saved')

elif (len(sys.argv) == 2) and (sys.argv[1] in mcbShelf):
    pyperclip.copy(mcbShelf[sys.argv[1]])
    print('arg found')
elif (len(sys.argv) == 2 and sys.argv[1] == 'list'):
    pyperclip.copy(str(list(mcbShelf.values())))
else:
    print('something happened')
mcbShelf.close()
