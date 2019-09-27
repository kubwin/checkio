def between_markers(text: str, begin: str, end: str) -> str:
    s=text.find(begin)
    t=text.find(end)
    q=len(begin)
    if s==-1:
        s = 0
        q=0
    if t==-1:
        t = len(text)
    if s>t:
        return ''
    return text[(s+q):t]
print(between_markers('No[/b] hi', '[b]', '[/b]'))