def remove_tags(string):
    while string != '<p>':
        open_tag = string.find('<')
        close_tag = string.find('>')
        open_no_tag = string.find('>',open_tag)
        close_no_tag = string.find('<',close_tag)
        no_tag = string[open_no_tag : close_no_tag]
        print no_tag
        string = string[string.find('<')]
        
print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')