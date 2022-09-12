print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')
special_commands = ['!help', '!done']
available_format = ['plain', 'bold', 'italic', 'header',
                    'link', 'inline-code', 'new-line',
                    'unordered-list', 'ordered-list']
memory = []
form = {'plain':'', 'bold':'**', 'italic':'*',
        'header':'#', 'inline-code':'`',
        'link':'', 'new-line':'\n'}

while True:
    x = input('Choose a formatter: ')
    if x not in special_commands + available_format:
        print('Unknown formatting type or command')
    elif x == '!help':
        print('Available formatters: ', end='')
        print(*available_format)
        print('Special commands: ', end='')
        print(*special_commands)
    elif x == '!done':
        with open('[MRKD]output.md', 'w') as file:
            for i in memory:
                file.write(i)
        break

    elif x in available_format:
        if x == 'header':
            while True:
                lvl = input('Level: ')
                if lvl not in '123456':
                    print('The level should be within the range of 1 to 6')
                else:
                    if len(memory) == 0:
                        text = int(lvl) * form['header'] + ' ' + input('Text: ')
                    else:
                        text = '\n' + int(lvl) * form['header'] + ' ' + input('Text: ')
                    memory.append(text)
                    memory.append('\n')
                    print(*memory,sep='')
                    break
        elif x == 'bold':
            text = form['bold'] + input('Text: ') + form['bold']
            memory.append(text)
            print(*memory,sep='')
        elif x == 'italic':
            text = form['italic'] + input('Text: ') + form['italic']
            memory.append(text)
            print(*memory,sep='')
        elif x == 'plain':
            text = input('Text: ')
            memory.append(text)
            print(*memory,sep='')
        elif x == 'inline-code':
            text = form['inline-code'] + input('Text: ') + form['inline-code']
            memory.append(text)
            print(*memory,sep='')
        elif x == 'new-line':
            text = form['new-line']
            memory.append(text)
            print(*memory,sep='')
        elif x == 'link':
            label = input('Label: ')
            url = input('URL: ')
            text = '[' + label + ']' + '(' + url + ')'
            memory.append(text)
            print(*memory,sep='')
        elif x == 'ordered-list':
            while True:
                rows = input('Numbers of rows: ')
                if int(rows) <= 0:
                    print('The number of rows should be greater than zero')
                else:
                    if len(memory) != 0 and '\n' not in memory[-1]:
                        memory.append('\n')
                    for i in range(1, int(rows) + 1):
                        memory.append(f"{i}{'.'} {input(f'Row #{i}: ')}\n")
                    print(*memory,sep='')
                    break
        elif x == 'unordered-list':
            while True:
                rows = input('Numbers of rows: ')
                if int(rows) <= 0:
                    print('The number of rows should be greater than zero')
                else:
                    if '\n' not in memory[-1]:
                        memory.append('\n')
                    for i in range(1, int(rows) + 1):
                        memory.append(f"* {input(f'Row #{i}: ')}\n")
                    print(*memory, sep='')
                    break