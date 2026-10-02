from .errors import DivisionByZeroError, ValidationError


def tokenize(expression):
    s = expression.replace(' ','')
    tokens = []
    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit() or char == '.':
            number = ''
            while i < len(s) and (s[i].isdigit() or s[i]=='.'):
                number+=s[i]
                i+=1
            tokens.append(number)
            continue
        elif char == '(' or char == ')':
            tokens.append(char)
            i+=1
            continue
        elif char in '+-*/%':
            if char == '/' and s[i+1]=='/':
                tokens.append('//')
                i+=2
                continue
            elif char == '-' or char == '+':
                if i==0 or s[i-1] in '+-*/%':
                    number = char
                    i+=1
                    while i < len(s) and (s[i].isdigit() or s[i]=='.'):
                        number+=s[i]
                        i+=1
                    tokens.append(number)
                    continue
                else:
                    tokens.append(char)
            else:
                tokens.append(char)
            i+=1
            continue
        i+=1
    return tokens
                
def validate(tokens):
    if not tokens:
        raise ValidationError("Выражение не может быть пустым")

    allowed_chars = "+-*/%//" + '()'

    for token in tokens:
        is_num = token.replace(".", "", 1).replace("-", "", 1).isdigit()
        is_op = token in allowed_chars
        if not (is_num or is_op):
            raise ValidationError(f"Недопустимый символ или формат числа: '{token}'")

    for i in range(len(tokens) - 1):
        t1 = tokens[i]
        t2 = tokens[i + 1]

        t1_is_num = t1.replace(".", "", 1).replace("-", "", 1).isdigit()
        t2_is_num = t2.replace(".", "", 1).replace("-", "", 1).isdigit()

        if t1_is_num and t2_is_num:
            raise ValidationError("Нельзя ставить два числа подряд")

        if not t1_is_num and not t2_is_num:  # noqa: SIM102
            if t1 in "+-*/%//" and t2 in "+-*/%//":
                raise ValidationError("Нельзя ставить два оператора подряд")

    if tokens[0] in '+-*/%//':
        raise ValidationError("Выражение не может начинаться с оператора")
    if tokens[-1] in '+-*/%//':
        raise ValidationError("Выражение не может заканчиваться оператором")

    return True


def infix_to_rpn(tokens):
    output = []
    stack = []

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "//": 2, "%": 2}

    for token in tokens:
        if token.replace('.','',1).replace('-','',1).isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1]!='(' and precedence[stack[-1]]>=precedence[token]):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if token.replace(".", "", 1).replace("-", "", 1).isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise DivisionByZeroError("Делить на ноль нельзя")
                stack.append(a / b)
            elif token == "//":
                if b == 0:
                    raise DivisionByZeroError("Делить на ноль нельзя")
                stack.append(float(a // b))
            elif token == "%":
                if b == 0:
                    raise DivisionByZeroError("Делить на ноль нельзя")
                stack.append(float(a % b))
    return stack[0]


def calculate(expression: str):
    tokens = tokenize(expression)
    validate(tokens)
    rpn_tokens = infix_to_rpn(tokens)
    return evaluate_rpn(rpn_tokens)
