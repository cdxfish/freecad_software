
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDErightUMINUSCOMMENT DIVIDE EQUALS FLOAT INT LPAREN MINUS NAME PLUS RPAREN TIMESstatement : NAME EQUALS expressionstatement : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : FLOATexpression : INTexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,8,9,10,11,12,],[2,14,14,14,14,14,14,14,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[4,-11,10,4,4,-9,-10,4,4,4,4,4,-7,-11,10,10,-3,-4,-5,-6,-8,]),'LPAREN':([0,4,5,8,9,10,11,12,],[5,5,5,5,5,5,5,5,]),'FLOAT':([0,4,5,8,9,10,11,12,],[6,6,6,6,6,6,6,6,]),'INT':([0,4,5,8,9,10,11,12,],[7,7,7,7,7,7,7,7,]),'$end':([1,2,3,6,7,13,14,16,17,18,19,20,21,],[0,-11,-2,-9,-10,-7,-11,-1,-3,-4,-5,-6,-8,]),'EQUALS':([2,],[8,]),'PLUS':([2,3,6,7,13,14,15,16,17,18,19,20,21,],[-11,9,-9,-10,-7,-11,9,9,-3,-4,-5,-6,-8,]),'TIMES':([2,3,6,7,13,14,15,16,17,18,19,20,21,],[-11,11,-9,-10,-7,-11,11,11,11,11,-5,-6,-8,]),'DIVIDE':([2,3,6,7,13,14,15,16,17,18,19,20,21,],[-11,12,-9,-10,-7,-11,12,12,12,12,-5,-6,-8,]),'RPAREN':([6,7,13,14,15,17,18,19,20,21,],[-9,-10,-7,-11,21,-3,-4,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,8,9,10,11,12,],[3,13,15,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','tokrules.py',100),
  ('statement -> expression','statement',1,'p_statement_expr','tokrules.py',105),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','tokrules.py',110),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','tokrules.py',111),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','tokrules.py',112),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','tokrules.py',113),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','tokrules.py',121),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','tokrules.py',126),
  ('expression -> FLOAT','expression',1,'p_expression_float','tokrules.py',131),
  ('expression -> INT','expression',1,'p_expression_int','tokrules.py',136),
  ('expression -> NAME','expression',1,'p_expression_name','tokrules.py',141),
]
