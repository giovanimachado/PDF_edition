#! python 3x
# loc.py - Launches "Localizador de Pessoas" in the browser using 
# an address from the command line or clipboard.
# To understando sys: http://devfuria.com.br/python/sys-argv/

import webbrowser, sys, pyperclip, requests
if len(sys.argv) > 1:
    # Get adress form command line.
    # sys.argv[1:] to chop off the first element (program name) 
    # of the array.
    name = ' '.join(sys.argv[1:]) 
else:
    # Get address from clipboard.
    name = pyperclip.paste()

webbrowser.open('http://portalpetrobras.petrobras.com.br/PetrobrasPortal/appmanager/portal/desktop?_nfpb=true&_pageLabel=dctm_landing_page_localizador_de_pessoas_a_petrobras&origem=buscalope&unico=' + name)

print("working")
print("Finding: " + name)
print()