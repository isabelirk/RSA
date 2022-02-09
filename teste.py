
        usuarioArquivo = open(usuarioArquivo,'r')
        letterList = []
        codeList = []
        line = usuarioArquivo.readline()
        while line != '':
            line = line.rstrip() 
            letterList.append(line[0]) # append the first character of the line to the letterList 
            codeList.append(line[2:]) # append the 3rd to last character of the line to the codeList
            line = usuarioArquivo.readline()
        usuarioArquivo.close()

        print('------')
        print(letterList)
        print(codeList)
        print('-------')

        try:
            print("Enter a string to convert to morse code or press <enter> to quit")    
            userInput = input("")     
            while userInput: 
                userInput = userInput.replace(' ', '')
                userInput = userInput.upper()
                accumulateLetters = ''
                for x in userInput:
                    index = letterList.index(x)
                    value = codeList[index]
                    accumulateLetters += value
                    print(accumulateLetters)
                    print("Try again or press <enter> to quit")
                    userInput = input("")
        except ValueError:
            print("Error in input. Only alphanumeric characters, a comma, and period allowed")


        #for linha in usuarioArquivo:
         #   linha = linha.rstrip()
          #  for char in usuarioArquivo:
           #     print(char, '-')

        #usuarioArquivo.write("teste")
        #usuarioArquivo.readlines()
        #print(char)

        #if(not char):