
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftLESSTHANGREATERTHANLESSTHANEQUALGREATERTHANEQUALNOTEQUALEQUALSleftINleftPLUSMINUSleftFLRDIVleftPOWERleftMODleftTIMESDIVIDEleftLPARENRPARENleftLCURLYRCURLYAND ASEQUAL COMMA DIVIDE ELSE EQUALS FLRDIV GREATERTHAN GREATERTHANEQUAL IF IN INTEGER LBRACKET LCURLY LESSTHAN LESSTHANEQUAL LPAREN MINUS MOD NOT NOTEQUAL OR PLUS POWER PRINT RBRACKET RCURLY REAL RPAREN SEMICOLON STRING TIMES VARIABLE WHILEprogram : block block : LCURLY statement statement_tail RCURLY\n             | emptyblock : VARIABLE LPAREN expression RPAREN blockstatement_tail : statement statement_tailstatement_tail : emptystatement : PRINT LPAREN VARIABLE RPAREN SEMICOLON statement : PRINT LPAREN STRING RPAREN SEMICOLON statement : PRINT LPAREN expression RPAREN SEMICOLON statement : IF LPAREN expression RPAREN block emptystatement : IF LPAREN expression RPAREN block ELSE blockstatement : WHILE LPAREN expression RPAREN blockstatement : VARIABLE LBRACKET expression RBRACKET ASEQUAL expression SEMICOLONstatement : VARIABLE ASEQUAL expression SEMICOLON\n                 | VARIABLE ASEQUAL list_index SEMICOLONstatement : VARIABLE ASEQUAL list SEMICOLONstatement : listexpression : expression POWER expression\n                  | expression FLRDIV expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression PLUS expression\n                  | expression MINUS expression\n                  | expression MOD expression\n                  | expression GREATERTHANEQUAL expression\n                  | expression LESSTHANEQUAL expression\n                  | expression GREATERTHAN expression\n                  | expression LESSTHAN expression\n                  | expression AND expression\n                  | expression OR expression\n                  | expression NOTEQUAL expression\n                  | expression EQUALS expression\n                  | expression IN list\n                  | NOT expressionexpression : LPAREN expression RPARENlist : LBRACKET list_elements future_list_elements RBRACKET\n            | list PLUS listlist_elements : expression\n                     | list\n                     | emptyfuture_list_elements : COMMA expression future_list_elements\n                            | COMMA list future_list_elements\n                            | empty_listexpression : STRINGexpression : REAL\n                  | INTEGER\n                  | STRING LBRACKET INTEGER RBRACKETexpression : list_indexexpression : VARIABLEexpression : VARIABLE LPAREN expression RPARENlist_index : VARIABLE index_taillist_index : list index_tail index_tail : LBRACKET expression RBRACKET index_tail\n                  | emptyempty_list :  empty : '
    
_lr_action_items = {'LCURLY':([0,75,83,84,122,],[3,3,3,3,3,]),'VARIABLE':([0,3,4,6,11,12,13,14,17,18,19,20,21,26,27,37,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,74,75,80,81,82,83,84,85,108,109,110,111,112,113,114,121,122,124,125,],[5,8,-3,8,32,-17,32,8,38,32,32,32,32,32,32,-2,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-37,5,-14,-15,-16,5,5,-36,-4,-7,-8,-9,32,-56,-12,-10,5,-13,-11,]),'$end':([0,1,2,4,37,75,108,],[-56,0,-1,-3,-2,-56,-4,]),'PRINT':([3,4,6,12,14,37,74,75,80,81,82,83,84,85,108,109,110,111,113,114,121,122,124,125,],[7,-3,7,-17,7,-2,-37,-56,-14,-15,-16,-56,-56,-36,-4,-7,-8,-9,-56,-12,-10,-56,-13,-11,]),'IF':([3,4,6,12,14,37,74,75,80,81,82,83,84,85,108,109,110,111,113,114,121,122,124,125,],[9,-3,9,-17,9,-2,-37,-56,-14,-15,-16,-56,-56,-36,-4,-7,-8,-9,-56,-12,-10,-56,-13,-11,]),'WHILE':([3,4,6,12,14,37,74,75,80,81,82,83,84,85,108,109,110,111,113,114,121,122,124,125,],[10,-3,10,-17,10,-2,-37,-56,-14,-15,-16,-56,-56,-36,-4,-7,-8,-9,-56,-12,-10,-56,-13,-11,]),'LBRACKET':([3,4,6,8,11,12,13,14,17,18,19,20,21,24,26,27,28,32,33,35,37,38,39,44,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,72,74,75,80,81,82,83,84,85,87,108,109,110,111,112,113,114,117,121,122,124,125,],[11,-3,11,18,11,-17,11,11,11,11,11,11,11,67,11,11,71,67,11,67,-2,67,71,67,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-37,-56,-14,-15,-16,-56,-56,-36,67,-4,-7,-8,-9,11,-56,-12,67,-10,-56,-13,-11,]),'ELSE':([4,37,75,83,108,113,],[-3,-2,-56,-56,-4,122,]),'RCURLY':([4,6,12,14,15,16,36,37,74,75,80,81,82,83,84,85,108,109,110,111,113,114,121,122,124,125,],[-3,-56,-17,-56,37,-6,-5,-2,-37,-56,-14,-15,-16,-56,-56,-36,-4,-7,-8,-9,-56,-12,-10,-56,-13,-11,]),'LPAREN':([5,7,9,10,11,13,17,18,19,20,21,26,27,32,38,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[13,17,20,21,27,27,27,27,27,27,27,27,27,72,72,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ASEQUAL':([8,79,],[19,112,]),'NOT':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'STRING':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[28,28,39,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'REAL':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'INTEGER':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,71,72,112,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,106,30,30,]),'COMMA':([11,22,23,24,25,28,29,30,31,32,35,66,68,69,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,117,118,119,123,],[-56,48,-38,-39,-40,-44,-45,-46,-48,-49,-56,-52,-54,-34,-51,-37,-36,48,48,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-56,-47,-50,-53,]),'RBRACKET':([11,22,23,24,25,28,29,30,31,32,35,41,47,49,66,68,69,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,115,116,117,118,119,123,],[-56,-55,-38,-39,-40,-44,-45,-46,-48,-49,-56,79,85,-43,-52,-54,-34,-51,-37,-36,-55,-55,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,117,-35,118,-41,-42,-56,-47,-50,-53,]),'PLUS':([12,23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[33,54,33,-44,-45,-46,-48,-49,54,33,-49,-44,54,54,54,-48,33,54,54,-52,-54,54,54,-51,-37,-36,54,33,-18,-19,-20,-21,-22,-23,-24,54,54,54,54,54,54,54,54,33,54,-35,54,-56,-47,-50,54,-53,]),'POWER':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[50,-56,-44,-45,-46,-48,-49,50,-56,-49,-44,50,50,50,-48,-56,50,50,-52,-54,50,50,-51,-37,-36,50,-56,-18,50,-20,-21,50,50,-24,50,50,50,50,50,50,50,50,-33,50,-35,50,-56,-47,-50,50,-53,]),'FLRDIV':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[51,-56,-44,-45,-46,-48,-49,51,-56,-49,-44,51,51,51,-48,-56,51,51,-52,-54,51,51,-51,-37,-36,51,-56,-18,-19,-20,-21,51,51,-24,51,51,51,51,51,51,51,51,-33,51,-35,51,-56,-47,-50,51,-53,]),'TIMES':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[52,-56,-44,-45,-46,-48,-49,52,-56,-49,-44,52,52,52,-48,-56,52,52,-52,-54,52,52,-51,-37,-36,52,-56,52,52,-20,-21,52,52,52,52,52,52,52,52,52,52,52,-33,52,-35,52,-56,-47,-50,52,-53,]),'DIVIDE':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[53,-56,-44,-45,-46,-48,-49,53,-56,-49,-44,53,53,53,-48,-56,53,53,-52,-54,53,53,-51,-37,-36,53,-56,53,53,-20,-21,53,53,53,53,53,53,53,53,53,53,53,-33,53,-35,53,-56,-47,-50,53,-53,]),'MINUS':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[55,-56,-44,-45,-46,-48,-49,55,-56,-49,-44,55,55,55,-48,-56,55,55,-52,-54,55,55,-51,-37,-36,55,-56,-18,-19,-20,-21,-22,-23,-24,55,55,55,55,55,55,55,55,-33,55,-35,55,-56,-47,-50,55,-53,]),'MOD':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[56,-56,-44,-45,-46,-48,-49,56,-56,-49,-44,56,56,56,-48,-56,56,56,-52,-54,56,56,-51,-37,-36,56,-56,56,56,-20,-21,56,56,-24,56,56,56,56,56,56,56,56,-33,56,-35,56,-56,-47,-50,56,-53,]),'GREATERTHANEQUAL':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[57,-56,-44,-45,-46,-48,-49,57,-56,-49,-44,57,57,57,-48,-56,57,57,-52,-54,57,57,-51,-37,-36,57,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,57,57,-31,-32,-33,57,-35,57,-56,-47,-50,57,-53,]),'LESSTHANEQUAL':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[58,-56,-44,-45,-46,-48,-49,58,-56,-49,-44,58,58,58,-48,-56,58,58,-52,-54,58,58,-51,-37,-36,58,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,58,58,-31,-32,-33,58,-35,58,-56,-47,-50,58,-53,]),'GREATERTHAN':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[59,-56,-44,-45,-46,-48,-49,59,-56,-49,-44,59,59,59,-48,-56,59,59,-52,-54,59,59,-51,-37,-36,59,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,59,59,-31,-32,-33,59,-35,59,-56,-47,-50,59,-53,]),'LESSTHAN':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[60,-56,-44,-45,-46,-48,-49,60,-56,-49,-44,60,60,60,-48,-56,60,60,-52,-54,60,60,-51,-37,-36,60,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,60,60,-31,-32,-33,60,-35,60,-56,-47,-50,60,-53,]),'AND':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[61,-56,-44,-45,-46,-48,-49,61,-56,-49,-44,61,61,61,-48,-56,61,61,-52,-54,-34,61,-51,-37,-36,61,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,61,-31,-32,-33,61,-35,61,-56,-47,-50,61,-53,]),'OR':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[62,-56,-44,-45,-46,-48,-49,62,-56,-49,-44,62,62,62,-48,-56,62,62,-52,-54,-34,62,-51,-37,-36,62,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,62,-35,62,-56,-47,-50,62,-53,]),'NOTEQUAL':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[63,-56,-44,-45,-46,-48,-49,63,-56,-49,-44,63,63,63,-48,-56,63,63,-52,-54,63,63,-51,-37,-36,63,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,63,63,-31,-32,-33,63,-35,63,-56,-47,-50,63,-53,]),'EQUALS':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[64,-56,-44,-45,-46,-48,-49,64,-56,-49,-44,64,64,64,-48,-56,64,64,-52,-54,64,64,-51,-37,-36,64,-56,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,64,64,-31,-32,-33,64,-35,64,-56,-47,-50,64,-53,]),'IN':([23,24,28,29,30,31,32,34,35,38,39,40,41,42,43,44,45,46,66,68,69,70,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,107,117,118,119,120,123,],[65,-56,-44,-45,-46,-48,-49,65,-56,-49,-44,65,65,65,-48,-56,65,65,-52,-54,65,65,-51,-37,-36,65,-56,-18,-19,-20,-21,-22,-23,-24,65,65,65,65,65,65,65,65,-33,65,-35,65,-56,-47,-50,65,-53,]),'RPAREN':([28,29,30,31,32,34,35,38,39,40,45,46,66,68,69,70,73,74,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,117,118,119,123,],[-44,-45,-46,-48,-49,75,-56,76,77,78,83,84,-52,-54,-34,105,-51,-37,-36,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,119,-56,-47,-50,-53,]),'SEMICOLON':([28,29,30,31,32,35,42,43,44,66,68,69,73,74,76,77,78,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,117,118,119,120,123,],[-44,-45,-46,-48,-49,-56,80,81,82,-52,-54,-34,-51,-37,109,110,111,-36,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-56,-47,-50,124,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,75,83,84,122,],[2,108,113,114,125,]),'empty':([0,6,11,14,24,32,35,38,44,75,83,84,87,113,117,122,],[4,16,25,16,68,68,68,68,68,4,4,4,68,121,68,4,]),'statement':([3,6,14,],[6,14,14,]),'list':([3,6,11,13,14,17,18,19,20,21,26,27,33,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,72,112,],[12,12,24,35,12,35,35,44,35,35,35,35,74,87,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,103,35,35,35,]),'statement_tail':([6,14,],[15,36,]),'list_elements':([11,],[22,]),'expression':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[23,34,40,41,42,45,46,69,70,86,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,107,120,]),'list_index':([11,13,17,18,19,20,21,26,27,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,67,72,112,],[31,31,31,31,43,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'future_list_elements':([22,86,87,],[47,115,116,]),'empty_list':([22,86,87,],[49,49,49,]),'index_tail':([24,32,35,38,44,87,117,],[66,73,66,73,66,66,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_run_program','main.py',452),
  ('block -> LCURLY statement statement_tail RCURLY','block',4,'p_block_def','main.py',456),
  ('block -> empty','block',1,'p_block_def','main.py',457),
  ('block -> VARIABLE LPAREN expression RPAREN block','block',5,'p_function_def','main.py',466),
  ('statement_tail -> statement statement_tail','statement_tail',2,'p_block_statement_tail','main.py',471),
  ('statement_tail -> empty','statement_tail',1,'p_block_statement_tail_e','main.py',481),
  ('statement -> PRINT LPAREN VARIABLE RPAREN SEMICOLON','statement',5,'p_block_print_variable','main.py',485),
  ('statement -> PRINT LPAREN STRING RPAREN SEMICOLON','statement',5,'p_block_print_string','main.py',489),
  ('statement -> PRINT LPAREN expression RPAREN SEMICOLON','statement',5,'p_block_print_expr','main.py',493),
  ('statement -> IF LPAREN expression RPAREN block empty','statement',6,'p_block_if','main.py',497),
  ('statement -> IF LPAREN expression RPAREN block ELSE block','statement',7,'p_block_if_else','main.py',501),
  ('statement -> WHILE LPAREN expression RPAREN block','statement',5,'p_statement_while','main.py',505),
  ('statement -> VARIABLE LBRACKET expression RBRACKET ASEQUAL expression SEMICOLON','statement',7,'p_statement_assign_array','main.py',510),
  ('statement -> VARIABLE ASEQUAL expression SEMICOLON','statement',4,'p_statement_assign','main.py',515),
  ('statement -> VARIABLE ASEQUAL list_index SEMICOLON','statement',4,'p_statement_assign','main.py',516),
  ('statement -> VARIABLE ASEQUAL list SEMICOLON','statement',4,'p_statement_assign_list','main.py',525),
  ('statement -> list','statement',1,'p_statement_expr','main.py',531),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','main.py',539),
  ('expression -> expression FLRDIV expression','expression',3,'p_expression_binop','main.py',540),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','main.py',541),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','main.py',542),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','main.py',543),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','main.py',544),
  ('expression -> expression MOD expression','expression',3,'p_expression_binop','main.py',545),
  ('expression -> expression GREATERTHANEQUAL expression','expression',3,'p_expression_binop','main.py',546),
  ('expression -> expression LESSTHANEQUAL expression','expression',3,'p_expression_binop','main.py',547),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression_binop','main.py',548),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','main.py',549),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','main.py',550),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','main.py',551),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binop','main.py',552),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_binop','main.py',553),
  ('expression -> expression IN list','expression',3,'p_expression_binop','main.py',554),
  ('expression -> NOT expression','expression',2,'p_expression_binop','main.py',555),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','main.py',565),
  ('list -> LBRACKET list_elements future_list_elements RBRACKET','list',4,'p_list_builder','main.py',569),
  ('list -> list PLUS list','list',3,'p_list_builder','main.py',570),
  ('list_elements -> expression','list_elements',1,'p_list_elements','main.py',581),
  ('list_elements -> list','list_elements',1,'p_list_elements','main.py',582),
  ('list_elements -> empty','list_elements',1,'p_list_elements','main.py',583),
  ('future_list_elements -> COMMA expression future_list_elements','future_list_elements',3,'p_list_future_elements','main.py',590),
  ('future_list_elements -> COMMA list future_list_elements','future_list_elements',3,'p_list_future_elements','main.py',591),
  ('future_list_elements -> empty_list','future_list_elements',1,'p_list_future_elements','main.py',592),
  ('expression -> STRING','expression',1,'p_expression_string','main.py',601),
  ('expression -> REAL','expression',1,'p_expression_number','main.py',605),
  ('expression -> INTEGER','expression',1,'p_expression_number','main.py',606),
  ('expression -> STRING LBRACKET INTEGER RBRACKET','expression',4,'p_expression_number','main.py',607),
  ('expression -> list_index','expression',1,'p_expression_list_index','main.py',619),
  ('expression -> VARIABLE','expression',1,'p_expression_variable','main.py',623),
  ('expression -> VARIABLE LPAREN expression RPAREN','expression',4,'p_expression_function','main.py',630),
  ('list_index -> VARIABLE index_tail','list_index',2,'p_list_index','main.py',637),
  ('list_index -> list index_tail','list_index',2,'p_list_index_1','main.py',646),
  ('index_tail -> LBRACKET expression RBRACKET index_tail','index_tail',4,'p_index_tail','main.py',654),
  ('index_tail -> empty','index_tail',1,'p_index_tail','main.py',655),
  ('empty_list -> <empty>','empty_list',0,'p_empty_list','main.py',672),
  ('empty -> <empty>','empty',0,'p_empty','main.py',676),
]
