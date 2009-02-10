def join(parent, child):
    return parent.rstrip("/") + "/" + child.lstrip("/")
    
def fixslash(url, relative=True):
    url = url.strip("/")
    if relative:
        url = "/" + url
    return url