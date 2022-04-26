size = 3
data = [0]*(size)   #Initialize the stack
top = -1

def push(x):
  global top
  if top >= size-1:
    print("Stack Overflow")
  else:
    top = top + 1
    data[top] = x


def pop():
  global top
  if top == -1:
    print("Stack Underflow")
  else:
    top = top-1
    data[top] = 0
    return data[top+1]


def peek():
  global top
  if top == -1:
    print("Stack is empty")
  else:
    print(data[top])




push('egg')
push('ham')
push('spam')
push('new')
push('new2')

print(data[0 : top + 1])

print(data[0 : top + 1])
pop()
pop()
pop()
pop()
print(data[0:top+1])

peek()

print(data[0:top+1])
