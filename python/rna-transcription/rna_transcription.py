def to_rna(inputsequence):
    resultlist = []
    for i in inputsequence:
        if i == 'C':
            resultlist.append('G')
        elif i == 'G':
            resultlist.append('C')
        elif i == 'T':
            resultlist.append('A')
        elif i == 'A':
            resultlist.append('U')
    return ''.join(resultlist)

