import pyperclip


def format(tabs):
    lines = tabs.split('\n')
    title = ''
    links = []
    for (i,line) in enumerate(lines):
        m = i%3
        if m == 0:
            title = line
            continue
        if m == 1:
            links.append('[[%s|%s]]' % (title, (line)))
            continue
    return ('\n').join(links)




tabs = pyperclip.paste()   # Copy from the clipboard.
pyperclip.copy(format(tabs))   # Copy to the clipboard.