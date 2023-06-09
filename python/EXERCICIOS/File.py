def readFile(filename):
    # abre o arquivo teste.txt no modo leitura e atribui o arquivo a var infile
    infile = open(filename, 'r')

    # a função .read le o arquivo inteiro e atribui o conteúdo a var content
    content = infile.read()

    # fecha o arquivo
    infile.close()

    # a função .split separa as palavras do arquivo `teste.txt` e armazena na var wordlist
    wordList = content.split()

    print(wordList)

    # retorna a quantidade de palavras e caracteres
    return len(wordList), len(content)

n_words, n_chars = readFile('teste.txt')