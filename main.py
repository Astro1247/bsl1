import sys

import lexer, pfcode_translator, pf_interpreter

if __name__ == '__main__':
    print("Welcome to BSL1 programming language tool menu")
    print("""
        1. Run lexer
        2. Run postfix translator
        3. Run postfix code interpreter
        
        0. Exit
    """)
    choice = 3
    choiceMap = {1: 'lexer', 2: 'translator', 3: 'interpreter', 0: 'exit'}
    try:
        choice = int(choice)
    except ValueError:
        raise Exception("Invalid input")
    if choice not in choiceMap.keys():
        raise Exception("Wrong choice")
    if choice == 1:
        lexer.lex()
        print('tableOfSymb:{0}'.format(lexer.tableOfSymb))
    elif choice == 2:
        pfcode_translator.postfixTranslator()
    elif choice == 3:
        pf_interpreter.postfixInterpreter()
    else:
        raise NotImplementedError("This menu option is not implemented yet")
