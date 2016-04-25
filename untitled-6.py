def get_next_tag(page):
    end_tag = page.find('>')
    start_tag=page.find('<',end_tag)
    word = page[end_tag+1:start_tag]
    return word, start_tag
    
 
def remove_tags(page):
    while True:
        word, start_tag=get_next_tag(page)
        if word:
            print word
            page=page[start_tag:]
        


        
print remove_tags('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']