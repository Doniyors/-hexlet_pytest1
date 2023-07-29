stack = []  # В Python стек реализован через список
not stack  # Список пуст
# True
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
not stack  # Список не пустой
# False
stack
# [1, 2, 3]
stack.pop()  # В стеке [1, 2]
# 3
stack.pop()  # В стеке [1]
# 2
stack.pop()  # В стеке пусто
# 1
not stack
# True

def test_stack():
    stack = []
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три — уже избыточно
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_stack1():
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'

def test_stack2():
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'


def test_emptiness():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack
    
