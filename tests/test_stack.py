import pytest

from stack.stack import Stack


def test_stack_push_pop_peek():
    stack = Stack()
    stack.push(3)
    stack.push(1)
    stack.push(5)

    assert len(stack) == 3
    assert stack.peek() == 5
    assert stack.pop() == 5
    assert stack.peek() == 1
    assert len(stack) == 2


def test_stack_min_tracking():
    stack = Stack()
    stack.push(4)
    stack.push(2)
    stack.push(3)
    stack.push(1)

    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 2


def test_stack_errors_on_empty_operations():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.peek()
    with pytest.raises(IndexError):
        stack.min()

