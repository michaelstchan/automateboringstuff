#! python3
 # mcb.pyw - Saves and loads pieces of text to the clipboard.
 # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword. 
 #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 #        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

if len(sys.argv) > 1: #got tired of typing sys.argv, so made these variables late
    arg1 = sys.argv[1]  
    if len(sys.argv) > 2:   #kept getting out of range errors so only assign if they exist
        arg2 = sys.argv[2]

if len(sys.argv) > 3:
    print('Usage: python mcb.pyw save/list/chosen-keyword')
if (len(sys.argv) == 3) and (sys.argv[1] == 'save'):
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print('saved')

elif (len(sys.argv) == 2) and (sys.argv[1] in mcbShelf):
    pyperclip.copy(mcbShelf[sys.argv[1]])
    print('arg found')
elif (len(sys.argv) == 2 and sys.argv[1] == 'list'):
    pyperclip.copy(str(list(mcbShelf.keys())))

#bonus: create a delete and deleteall command
elif (len(sys.argv) == 3 and sys.argv[1] == 'delete'):
    del mcbShelf[sys.argv[2]]
    print('deleted %s' % arg2)    
elif len(sys.argv) == 2 and arg1 == 'trash':
    mcbShelf.clear()        #shelves behave like dicts, so clear() works here. calling 'list' afterwards will paste and empty list
    print('deleted all')
else:
    print('something happened')
mcbShelf.close()
