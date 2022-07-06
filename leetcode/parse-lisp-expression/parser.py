class Parser:
    def __init__(self, expr: str):
        self.value_stack = []
        self.operator_stack = []
        self.dict = {}
        self.reg = 0

        self.str_i = 0
        self.expr = expr

    def parse_word(self):
        if self.expr[self.str_i] in (' ', '(', ')'):
            self.str_i += 1
            return self.expr[self.str_i-1]

        space_index = self.str_i + 1
        while space_index < len(self.expr):
            if self.expr[space_index] == ' ' or self.expr[space_index] == ')':
                break
            space_index += 1

        word = self.expr[self.str_i : space_index]
        self.str_i = space_index
        if self.expr[self.str_i] == ' ':
            self.str_i += 1
        return word

    def get_value(self, key):
        temp = self.dict.get(key, None)
        return temp if temp is not None else int(key)

    def parse(self):
        while self.str_i < len(self.expr):
            word = self.parse_word()
            print(word)

            if word == '(':
                self.operator_stack.append('(')
                for v in self.dict:
                    self.operator_stack.append(v)
                    self.value_stack.append(self.dict[v])
            elif word == ' ':
                pass
            elif word in ('add', 'mult', 'let'):
                self.operator_stack.append(word)
                if word == 'let':
                    self.value_stack.append('(')
            elif word == ')':
                oper = self.operator_stack.pop()
                if oper == 'add':
                    a, b = self.value_stack.pop(), self.value_stack.pop()
                    self.reg = self.get_value(a) + self.get_value(b)
                elif oper == 'mult':
                    a, b = self.value_stack.pop(), self.value_stack.pop()
                    self.reg = self.get_value(a) * self.get_value(b)
                elif oper == 'let':
                    self.reg = self.get_value(self.value_stack.pop())
                    self.value_stack.pop()
                else:
                    assert False
                oper = self.operator_stack.pop()
                while oper != '(':
                    self.dict[oper] = self.value_stack.pop()
                    oper = self.operator_stack.pop()
                if len(self.operator_stack) and self.operator_stack[-1] == 'let' and self.value_stack[-1] != '(':
                    variable_name = self.value_stack.pop()
                    self.dict[variable_name] = self.reg
                else:
                    self.value_stack.append(self.reg)
            else:
                if self.operator_stack[-1] == 'let':
                    if self.value_stack[-1] != '(':
                        variable_name = self.value_stack.pop()
                        self.dict[variable_name] = self.get_value(word)
                    else:
                        self.value_stack.append(word)
                else:
                    self.value_stack.append(self.get_value(word))
        return self.get_value(self.value_stack.pop())


if __name__ == '__main__':
    # parse = Parser('(let x 3 x 2 x)')  # 2
    # parse = Parser('(let x 2 (add x 3))')  # 5
    # parse = Parser('(let x 1 y 2 x (add x y) (add x y))')  # 5
    # parse = Parser('(let x 2 (mult x (let x 3 y 4 (add x y))))')  # 14
    parse = Parser('(let x 2 (add (let x 3 (let x 4 x)) x))')  # 6
    print(parse.parse())
