
import sys
import math
import copy
import inspect

class Node:
    def __init__(self, children):
        self.children = children
        self.type = None
       # print("Node")
    def evaluate(self):
      #  print("Evaluate")
        return 0
    def execute(self):
        pass

class NumberNode(Node):
    def __init__(self, v):
        self.value = int(v)
        #print("NumberNode " + str(self.value))
    def evaluate(self):
      #  print("Evaluate NumberNode")
        return self.value
    def execute(self):
      #print("Execute NumberNode " + str(self.value))
        #print self.value
        return self.value

class UpdateArrayNode(Node):
    def __init__(self, varName, index, update):
        self.name = varName
        self.index = index
        self.update = update
    def execute(self):
     #   print "entereing the monsterrrrrreer"
     #   print self.name
     #   print self.index
     #   print self.update
        global var
        var[self.name][self.index.execute()] = self.update.execute()

      #  print "leaving onsters"



class GetVariable(Node):
    def __init__(self, variable):
        self.value = variable
   #    print("NumberNode")
    def evaluate(self):
    #   print("Evaluate NumberNode")
        return self.value
    def execute(self):
    #   print("Execute GetVariable")
        global var
     #   print var[self.value]
        return var[self.value]

class ListNode(Node):
    def __init__(self, listElements):
        self.value = listElements
    #    print("NumberNode")
    def evaluate(self):
    #    print("Evaluate NumberNode")
        return self.value
    def execute(self):
     #   print("Execute GetVariable")
        return self.value

class StringNode(Node):
    def __init__(self, v):
        self.value = v
        #self.value = self.value[1:-1] # to eliminate the left and right double quotes
    #    print("StringNode")
    def evaluate(self):
    #    print("Evaluate StringNode")
        return self.value
    def execute(self):
   #     print("Execute StringNode")
        return self.value

class PrintNode(Node):
    def __init__(self, v):
        self.value = v
    #    print("PrintNode")
    def evaluate(self):
    #    print("Evaluate PrintNode")
        return 0
    def execute(self):
     #   print "lets try to print"
     #   print self.value
        while(hasattr(self.value,'execute')):
            self.value = self.value.execute()

        #print (type(self.value))
        if(type(self.value) == list):
            self.value = construct(self.value)

        print (repr(self.value))

def construct(param):
    a = list()
    for i in param:
        while(hasattr(i, 'execute')):
            i = i.execute()
        a.append(i)
    return a


class IndexNode(Node):
    def __init__(self, list1, index):
        self.list = list1
        self.indexList = index
      #  print("IndexNode")
    def execute(self):

        a = self.list
        for i in self.indexList:
            if(i != None):
                d =  i
                a = a.execute()[i.execute()]

        return a

class WhileNode(Node):
    def __init__(self, condition, thenBlock):
        self.condition = condition
        self.thenBlock = thenBlock
    def evaluate(self):
        return 0
    def execute(self):
        i = 0
       # print "Param1 " + str(self.condition.p1.execute())
        #print "Param2 " + str(self.condition.p2.execute())
        #print "Result: " + str(self.condition.execute())
        a = copy.deepcopy(self.thenBlock)
        c = copy.deepcopy(self.condition)
        while(self.condition.execute()):
            self.thenBlock.execute()
            b = copy.deepcopy(a)
            d = copy.deepcopy(c)
            self.thenBlock = b
            self.condition = d
            i = i + 1;
class ForNode(Node):
    def __init__(self, condition, thenBlock):
        self.condition = condition
        self.thenBlock = thenBlock
      #  print("IfNode")
    def evaluate(self):
       # print("Evaluate IfNode")
        return 0
    def execute(self):
        #print("Execute IfNode condition : " + str(self.condition))
        print('node not working yet')
class IfNode(Node):
    def __init__(self, c, t, e):
        self.condition = c
        self.thenBlock = t
        self.elseBlock= e
      #  print("IfNode")
    def evaluate(self):
       # print("Evaluate IfNode")
        return 0
    def execute(self):
        #print("Execute IfNode condition : " + str(self.condition))

        if(self.condition.execute()):
         #   print "THEN BLOCKKKKK"
         #   print self.thenBlock
            self.thenBlock.execute()
        else:
          #  print "ELSE BLOCKKKKK"
         #   print self.elseBlock
            self.elseBlock.execute()

class BlockNode(Node):
    def __init__(self, sl):
        self.statementNodes = sl
        #print("BlockNode")
        #print iter(sl)
    def evaluate(self):
        #print("Evaluate BlockNode")
        return 0
    def execute(self):
        #print "EXECUTE BLOCK"
        for statement in self.statementNodes:
         #   print statement
            statement.execute()

class AssignNode(Node):
    def __init__(self, varName, value):
        self.varName = varName
        self.value = value
    def execute(self):
    #    print "EXECUTE ASSIGN NODE"
        global var
        a =  self.varName
        b = self.value
        c = var
        var[self.varName] = self.value.execute()
    #    print var

class BinaryOpNode(Node):
    def __init__(self, param1, param2, operation):
        self.p1 = param1
        self.p2 = param2
        self.op = operation
    def execute(self):
      #  print "Binary Op Parameters Start"
        global var
      #  print var

      #  self.p1 = GetVariable('i')
      #  self.p2 = NumberNode(1)
      #  print self.p1
       # print self.p2

        #print "Binary Op Parameters End"

        while(hasattr(self.p1, 'execute')):
            self.p1 = self.p1.execute()

        while(hasattr(self.p2, 'execute')):
            self.p2 = self.p2.execute()


        if self.op == '+':
            return self.p1 + self.p2
        elif self.op  == '-':
            return self.p1 - self.p2
        elif self.op  == '**':
            return self.p1 ** self.p2
        elif self.op  == '//':
            return int(math.floor(self.p1 / self.p2))
        elif self.op  == '*':
            return self.p1 * self.p2
        elif self.op  == '/':
            return self.p1 / self.p2
        elif self.op  == '%':
            return self.p1 % self.p2
        elif self.op  == '<=':
            if(self.p1 <= self.p2):
                return 1
            else:
                return 0
        elif self.op  == '>=':
            if(self.p1 >= self.p2):
                return 1
            else:
                return 0
        elif self.op  == '<':
         #   print "Perform Less Than : " + str(self.p1) + " " + str(self.p2)
            if(self.p1 < self.p2):
                return 1
            else:
                return 0
        elif self.op  == '>':
            if(self.p1 > self.p2):
                return 1
            else:
                return 0
        elif self.op  == '<>':
            if(self.p1 != self.p2):
                return 1
            else:
                return 0
        elif self.op == 'and':
            if(self.p1 and self.p2):
                return 1
            else:
                return 0
        elif self.op == 'or':
            if(self.p1 or self.p2):
                return 1
            else:
                return 0
        elif self.op == '==':
            if(self.p1 == self.p2):
                return 1
            else:
                return 0
        elif self.op == 'in':
            if(self.p1 in construct(self.p2)):
                return 1
            else:
                return 0
        elif self.op == 'not':
            return not(self.p1)

class FunctionNode(Node):
    def __init__(self, funcName, param1):
        self.funcName = funcName
        self.param1 = param1
    def execute(self):
        print ('Lets run function NODE ' + str(self.funcName) + " " + str(self.param1))

isError = False

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'print' : 'PRINT',
   'or'   : 'OR',
   'and'  : 'AND',
    'in'  : 'IN',
    'not' : 'NOT'
}

tokens = (
   'INTEGER',
   'REAL',
   'STRING',
   'PLUS',
   'POWER',
   'FLRDIV',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'GREATERTHANEQUAL',
   'NOTEQUAL',
   'EQUALS',
   'LESSTHANEQUAL',
   'GREATERTHAN',
   'LESSTHAN',
   'IN',
   'MOD',
   'AND',
   'OR',
   'NOT',
   'SEMICOLON',
   'ASEQUAL',
   'VARIABLE',
   'LCURLY',
   'RCURLY',
   'PRINT',
   'IF',
   'WHILE',
   'FOR',
   'ELSE'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'
t_LESSTHANEQUAL = r'\<\='
t_GREATERTHANEQUAL = r'\>\='
t_NOTEQUAL = r'\<\>'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_EQUALS = r'\=\='
t_MOD = r'\%'
t_AND = r'and'
t_OR = r'or'
t_POWER = r'\*\*'
t_FLRDIV = r'//'
t_NOT = r'not'
t_IN = r'in'
t_SEMICOLON = r'\;'
t_ASEQUAL = r'\='
t_WHILE = r'while'
t_FOR = r'for'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_IF = r'if'
t_ELSE = r'else'
t_PRINT = r'print'

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'\"[^"]*\"'
    t.value = str(t.value[1:-1])
    #t.value = str(t.value)
    return t

var = {}


def t_VARIABLE(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    global var
    t.type = reserved.get(t.value,'VARIABLE')
    if(t.value not in var and t.type == 'VARIABLE'):
        var[t.value] = None
    return t

t_ignore  = ' \t'

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LESSTHAN', 'GREATERTHAN', 'LESSTHANEQUAL', 'GREATERTHANEQUAL', 'NOTEQUAL', 'EQUALS'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FLRDIV'),
    ('left', 'POWER'),
    ('left', 'MOD'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'LCURLY', 'RCURLY')
)

def checkStrings(p1,  p2):
    if(str(type(p1) == '<type \'str\'>') and str(type(p2) == '<type \'str\'>')):
        return 1
    else:
        return 0

def checkNumbers(p1, p2):
    v1 = str(type(p1))
    v2 = str(type(p2))
    if((v1 == '<type \'int\'>' or v1 == '<type \'float\'>') and (v2 == '<type \'int\'>' or v2 == '<type \'float\'>')):
        return 1
    else:
        return 0

def checkSemantic(p1, p2):
    if(type(p1) == type(p2)):
        return 1
    else:
        return 0

stmt_list = []

def p_run_program(p):
    '''program : block '''
    p[1].execute()

def p_block_def(p):
    '''block : LCURLY statement statement_tail RCURLY
             | empty'''
    #print "3 " + str(p[2])
    #print "2 " + str(p[3])
    if(type(p[3]) != type(None)):
        p[0] = p[3] + [(p[2])]
        p[0] = (p[0])[::-1]
    p[0] = BlockNode(p[0])

def p_function_def(p):
    '''block : VARIABLE LPAREN expression RPAREN block'''
    p[0] = p[5]


def p_block_statement_tail(p):
    '''statement_tail : statement statement_tail'''
    if type(p[2]) != type(None):
        p[2].append(p[1])
        p[0] = p[2]
        #print "Append " + str(p[0])
    else:
            #print "first " + str([p[1]])
      p[0] = [p[1]]

def p_block_statement_tail_e(p):
    '''statement_tail : empty'''
    p[0] = list()

def p_block_print_variable(p):
    '''statement : PRINT LPAREN VARIABLE RPAREN SEMICOLON '''
    p[0] = PrintNode(GetVariable(p[3]))

def p_block_print_string(p):
    '''statement : PRINT LPAREN STRING RPAREN SEMICOLON '''
    p[0] = PrintNode(StringNode(p[3]))

def p_block_print_expr(p):
    '''statement : PRINT LPAREN expression RPAREN SEMICOLON '''
    p[0] = PrintNode(p[3])

def p_block_if(p):
    '''statement : IF LPAREN expression RPAREN block empty'''
    p[0] = IfNode(p[3], p[5], BlockNode(list()))

def p_block_if_else(p):
    '''statement : IF LPAREN expression RPAREN block ELSE block'''
    p[0] = IfNode(p[3], p[5], p[7])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN block'''
    #print p[3]
    p[0] = WhileNode(p[3], p[5])
def p_statement_for(p):
    '''statement : FOR LPAREN expression RPAREN block'''
    print('forloop being worked on')
    p[0] = ForNode(p[3],p[5])

def p_statement_assign_array(p):
    '''statement : VARIABLE LBRACKET expression RBRACKET ASEQUAL expression SEMICOLON'''
    #print "Waohsdhsdhsdhs"
    p[0] = UpdateArrayNode(p[1],p[3],p[6])

def p_statement_assign(p):
    '''statement : VARIABLE ASEQUAL expression SEMICOLON
                 | VARIABLE ASEQUAL list_index SEMICOLON'''
    a = p[1]
    c = p[2]
    b = p[3]
    d = p[4]
    p[0] = AssignNode(p[1], p[3])
    #ASSIGN NONE IS RECEIVE 'data' and None

def p_statement_assign_list(p):
    '''statement : VARIABLE ASEQUAL list SEMICOLON'''
    a = p[1]
    b = p[3]
    p[0] = AssignNode(p[1], p[3])

def p_statement_expr(p):
    '''statement : list'''
    p[0] = 66766
    global isError
    if(p[1] != None) and (isError == False):
        #print repr(p[1])
        pass

def p_expression_binop(p):
    '''expression : expression POWER expression
                  | expression FLRDIV expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MOD expression
                  | expression GREATERTHANEQUAL expression
                  | expression LESSTHANEQUAL expression
                  | expression GREATERTHAN expression
                  | expression LESSTHAN expression
                  | expression AND expression
                  | expression OR expression
                  | expression NOTEQUAL expression
                  | expression EQUALS expression
                  | expression IN list
                  | NOT expression'''
    try:
        if(p[1] != 'not'):
            p[0] = BinaryOpNode(p[1],p[3], p[2])
        else:
            p[0] = BinaryOpNode(p[2], NumberNode(0), p[1])
    except:
        print ("SEMANTIC ERROR 412")

def p_expression_paren(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_list_builder(p):
    '''list : LBRACKET list_elements future_list_elements RBRACKET
            | list PLUS list'''
    #print p[2]
    if(p[2] == [None]):
        p[0] = ListNode([])
    elif(p[2] == '+'):
        p[0] = ListNode(p[1] + p[3])
    else:
       # print p[2] + p[3]
        p[0] = ListNode(p[2] + p[3])

def p_list_elements(p):
    '''list_elements : expression
                     | list
                     | empty'''
    if(str(type(p[1])) != '<type \'list\'>'):
        p[0] = [p[1]]
    else:
        p[0] = p[1]

def p_list_future_elements(p):
    '''future_list_elements : COMMA expression future_list_elements
                            | COMMA list future_list_elements
                            | empty_list'''
    if (p[1] == []):
        p[0] = []
    else:
        if(type(p[2]) != '<type \'list\'>'):
            p[2] = [p[2]]
        p[0] = p[2] + p[3]

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = StringNode(p[1])

def p_expression_number(p):
    '''expression : REAL
                  | INTEGER
                  | STRING LBRACKET INTEGER RBRACKET'''
    try:
        if(len(p) > 2):
            a = p[1]
            b = p[3]
            p[0] = StringNode(p[1][p[3]])
        else:
            p[0] = NumberNode(p[1])
    except:
        print ("SEMANTIC ERROR")

def p_expression_list_index(p):
    '''expression : list_index'''
    p[0] = p[1]

def p_expression_variable(p):
    '''expression : VARIABLE'''
    try:
        p[0] = GetVariable(p[1])
    except:
        print ("SEMANTIC ERROR")

def p_expression_function(p):
    '''expression : VARIABLE LPAREN expression RPAREN'''
    try:
        p[0] = FunctionNode(p[1], p[3])
    except:
        print ("SEMANTIC ERROR")

def p_list_index(p):
    '''list_index : VARIABLE index_tail'''
    #print "545454545445"
    try:
        p[0] = IndexNode(GetVariable(p[1]),p[2])
        #p[0] = NumberNode(5)
    except:
        print ("SEMANTIC ERROR")

def p_list_index_1(p):
    '''list_index : list index_tail '''
    #print "23232323232"
    try:
        p[0] = IndexNode(p[1], p[2])
    except:
        print ("SEMANTIC ERROR")

def p_index_tail(p):
    '''index_tail : LBRACKET expression RBRACKET index_tail
                  | empty'''
    try:
        if type(p[2]) != type(list()):
            p[2] = [p[2]]
        if type(p[4]) != type(list() and type(p[4]) != type(None)):
            p[4] = [p[4]]
        if(type(p[4]) != type(None)):
            p[2] = p[2] + p[4]
        p[0] = p[2]
    except:
        p[0] = p[1]

#def p_index_tail_empty(p):
 #   '''index_tail: empty'''
  #  p[0] = p[1]

def p_empty_list(p):
    '''empty_list : '''
    p[0] = []

def p_empty(p):
    ''' empty : '''
    p[0] = None

def p_error(p):
    if p:
        if '}' in str(p.value):
            parser.errok()
        else:

            print("ERROR 001: Syntax error at '", str(p.value),"'line:",p.lineno," position:",str(p.lexpos))
         
         # Just discard the token and tell the parser it's okay.
            parser.errok()
    else:
         print("ERROR 002: Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()


program=""
while 'exit' not in program:
  program = input("Sapphire>>:")
  
  
  while 'import' in program:
    p_array=program.split()
    loc=p_array.index('import')
    try:
        imported= open(p_array[loc+1]+".sap")
    except:
        imported= open('libraries/'+p_array[loc+1]+".sap")
    file_str=imported.read()
    imported.close()
    p_array[loc+1]=""
    updated = ' '.join(p_array)

    rep=updated.replace("import ",file_str)
    program=rep
   
  program='{'+program+'}'
  while ';' not in program:
    program2= input(">")
    program=program+program2
  result = parser.parse(program)

if 'exit' in program:
  sys.exit()
#finish forloops and imports