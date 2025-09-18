from time import ctime as T
def changecase(func):
  def minore():
    a=f"{T()}\n{func().upper()}\n{T()}"
    return a
  return minore
@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

print(T())