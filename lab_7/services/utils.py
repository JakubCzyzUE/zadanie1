def read_file(file):
    f = open(file, 'r',encoding = 'utf8')
    data = f.read()
    f.close()
    return data
