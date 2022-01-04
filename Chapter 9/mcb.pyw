import shelve,pyperclip,sys

mcbshelf = shelve.open('mcb')


if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 3 and sys.argv[1].lower() =='delete' and sys.argv[2] in mcbshelf.keys():
    del mcbshelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    if sys.argv[1].lower() == 'delete':
        mcbshelf.clear()
    if sys.argv[1] in mcbshelf.keys():
        pyperclip.copy(str(mcbshelf[sys.argv[1]]))

mcbshelf.close()