def get_next_target(page):
    start_link = page.find('<')
    start_quote = page.find('>', start_link)
    end_quote = page.find('<', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
 

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
        
print_all_links('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>''')
        #>>> ['Title','This','is','a','link','.']
        
print_all_links('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
        #>>> ['Hello','World!']
        
print_all_links("<hello><goodbye>")
        #>>> []  
        

print_all_links('this <a href="test1">link 1</a> is <a href="test2">link 2</a> a <a href="test3">link 3</a>')