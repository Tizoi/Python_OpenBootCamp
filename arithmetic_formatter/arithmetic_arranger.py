import re

import operator
ops = { "+": operator.add, "-": operator.sub }
 

# Arranges a list of strings formated in a simple arithmetic operation ('operand operator operand')
# where operands can be integer numbers and operators can be either - or +. The result of the 
# arrangement is a string formatted on four rows, the first row contains the first row of
# operands, the second the operators and second operands, and the third a separator. If a boolean True
# Parameter is also passed it solves the problems, adding a fourth row with the solutions.
#
# Input Example:
#    ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
# 
# Output Example:
#    ['  11      3801      1      123         1\n',
#     '+  4    - 2999    + 2    +  49    - 9380\n',
#     '----    ------    ---    -----    ------']
# @author: Abel Ramos Samper
  
def arithmetic_arranger(problems: list, solve: bool = False):
    global ops

    if len(problems)>5:
      return 'Error: Too many problems.'
  
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
  
    for index, problem in enumerate(problems):
      elements = problem.split(' ')
      
      operand_1 =  elements[0].strip()
      operand_2 =  elements[2].strip()
      operator = elements[1].strip()
      result = ''
      separator = ''

      if(re.search('\D',operand_1) != None or re.search('\D',operand_2) != None):
        return "Error: Numbers must only contain digits."
  
      if(len(operand_1)>4 or len(operand_2)>4):
        return 'Error: Numbers cannot be more than four digits.'
    
      if(operator!='+' and operator!='-' ):
        return "Error: Operator must be '+' or '-'."
      
      if solve:
        if(index+1 < len(problems)):
          result += str(ops[operator](int(operand_1) ,int(operand_2)))
        else:
          result += str(ops[operator](int(operand_1) ,int(operand_2))) 
      
      if(len(operand_2)<len(operand_1)):
        for n in range(len(operand_1)-len(operand_2)):
          operand_2 = ' '+operand_2
          
      operand_2 = operator.strip() + ' ' + operand_2
      
      if(len(operand_1)<len(operand_2)):
        while(len(operand_1)<len(operand_2)):
          operand_1 = ' '+operand_1
    
      separator = '---'
      while (len(operand_1)>len(separator) or len(operand_1)>len(separator)):
        separator +='-'
      
      if solve:
        while len(result)<len(operand_2):
          result = ' '+result

      if(index+1 < len(problems)):
        first_row  += operand_1 + '    '
        second_row += operand_2 + '    '
        third_row += separator + '    '
        fourth_row += result + '    '
        continue

      if solve:
        first_row  += operand_1 + '\n'
        second_row += operand_2 + '\n'
        third_row += separator  + '\n'
        fourth_row += result
        return first_row + second_row + third_row + fourth_row
      
      first_row  += operand_1 + '\n'
      second_row += operand_2+ '\n'
      third_row += separator

  
    return first_row + second_row + third_row 