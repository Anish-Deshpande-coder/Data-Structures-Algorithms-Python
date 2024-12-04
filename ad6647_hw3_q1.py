def postfix_calculator(expression, variables):
    stack = []
    expression_list = list(expression)
    for token in expression.list:
        if token.isdigit():
            stack.append(int(token))
        elif token in variables:
            stack.append(variables[token])
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(int(left) + int(right))
            elif token == '-':
                stack.append(int(left) - int(right))
            elif token == '*':
                stack.append(int(left) * int(right))
            elif token == '/':
                stack.append(int(left) // int(right))
            else:
                raise Exception("Cannot recognize operator")
    return stack.pop()


variables_dict = {}
while True:
    prompt = input("--> ")
    prompt_list = list(prompt)
    if prompt == "done()":
        break
    if '=' in prompt_list:
        variable_name, postfix_expression = prompt.split('=', 1)
        variable_name = variable_name.strip()
        postfix_expression = postfix_expression.strip()
        value = postfix_calculator(postfix_expression, variables_dict)
        variables_dict[variable_name] = value
        print(variable_name)
    else:
        result = postfix_calculator(prompt, variables_dict)
        print(result)




    