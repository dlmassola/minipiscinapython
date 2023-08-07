import sys, settings, os

def createCV(nameFile):

    if(os.path.exists(nameFile + '.template') == False):
        print('The file ' + nameFile + '.template doesn\'t exist.') 
        return
    
    templateFile = open(nameFile + '.template', 'r')
    contentFile = templateFile.read()
    templateFile.close()

    contentFile = contentFile.replace('{title}', settings.title)
    contentFile = contentFile.replace('{surname}', settings.surname)
    contentFile = contentFile.replace('{name}', settings.name)
    contentFile = contentFile.replace('{age}', settings.age)
    contentFile = contentFile.replace('{profession}', settings.profession)

    templateFile = open(nameFile + '.html', 'w')
    templateFile.write(contentFile)
    templateFile.close()

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        fileName = sys.argv[1].split('.')

        if len(fileName) == 2:
            if fileName[1] == 'template':
                createCV(fileName[0])
            else:
                print('The file extension must be ".template".')
        else:
            print('The file name must be in the format "*.template".')
    else:
        print('You must provide just one argument.')