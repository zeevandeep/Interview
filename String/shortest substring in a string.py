def shortest_substring(s, char_set):
    substring = set()
    n = 0
    for c in s:
        substring.add(c)
        print substring
        
        n += 1
        if substring == char_set:
            n = s[0:n]
            print n
            m = shortest_substring(s[1:], char_set)
            return n if m is None or len(n) <= len(m) else m
    
    return None

print shortest_substring('cacabbbbacaaaaa', set(['a', 'b', 'c']))


