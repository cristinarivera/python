print remove_tags('''<h1>Title</h1><p>This is a<a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'><tr><td>Hello</td><td>World!</td></tr></table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []
