import sys

def createTable():

    txt = open('periodic_table.txt', 'r')
    lines = txt.readlines()

    result = ''

    last = 0
    next = 0

    for line in lines :
        elemento = line.split(' = ')

        str = elemento[1]
  
        dictionary = dict(subString.split(':') for subString in str.split(','))     
        
        if dictionary['position'] == '0':
            result += '<tr>\n'

        if last < int(dictionary['position']):
            next = int(dictionary['position']) - last - 1

            for i in range(next):
                result += '<td></td>\n'
        
        last = int(dictionary['position'])

        result += '<td class="td">\n<h4>' + elemento[0] + '</h4>\n'

        result += '<ul>\n'
        
        result += '<li>No ' + dictionary[" number"] + '</li>\n'
        
        result += '<li>' + dictionary[" small"] + '</li>\n'
        
        result += '<li>' + dictionary[" molar"] + '</li>\n'
        
        result += '<li>' + dictionary[" electron"] + ' electron</li>\n'
        
        result += '</ul>\n</td>\n'

        if dictionary["position"] == "17":
            result += '</tr>\n'

    txt.close()

    createCSS()
    createHTML(result)

def createHTML(content):
    exitText = '<!DOCTYPE html>\n'
    exitText += '<html lang="en">\n'
    exitText += '   <head>\n'
    exitText += '       <meta charset="UTF-8">\n'
    exitText += '       <link rel="stylesheet" href="./style.css">\n'
    exitText += '       <title>Tabela Periódica</title>\n'
    exitText += '   </head>\n'
    exitText += '   <body>\n'
    exitText += '       <table>\n'
    exitText += content
    exitText += '       </table>\n'
    exitText += '   </body>\n'
    exitText += '</html>'

    html = open('periodic_table.html', 'w')
    html.write(exitText)
    html.close()

def createCSS():
    content = 'table {\nborder-collapse: collapse;\n}\n.td\n{font-size: 7pt; width: 5%; border: 1px solid black;\npadding:10px;\n}'
    css = open('style.css', 'w')
    css.write(content)
    css.close()

if __name__ == '__main__':
    createTable()