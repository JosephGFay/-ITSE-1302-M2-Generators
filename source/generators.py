from utils import Answer, Question, exercise

@exercise
def generators():
  
  Question(1, """
		Implement a generator called “squares” to yield the square of all numbers from (a) to (b). 
 	""")
  
  def squares(a, b):
    while a < b:
      yield a ** 2
      a += 1
  
  results = [x for x in squares(0,10)]
  Answer(f"squares(0,10): {results}")
      
  Question(2, """
		Create a generator to yield all the even numbers from 1 to (n).
 	""")
  
  def even(n):
    i = 1
    while i < n:
      if i % 2 == 0:
        yield i
      i += 1
  
  results = [x for x in even(10)]
  Answer(f"even(10): {results}")
  
  Question(3, """
		Create another generator to yield all the odd numbers from 1 to (n).
 	""")
  
  def odd(n):
    i = 1
    while i < n:
      if i % 2 == 1:
        yield i
      i += 1
  
  results = [x for x in odd(10)]
  Answer(f"odd(10): {results}")
  
  Question(4, """
		Implement a generator that returns all numbers from (n) down to 0.
 	""")
  
  def descend(n):
    while n >= 0:
      yield n
      n -= 1
      
  results = [x for x in descend(10)]
  Answer(f"descend(10): {results}")
  
  Question(5, """
		Create a generator to return the fibonnaci sequence starting from the first element up to (n).
 	""")
  
  def fibonacci(n):
    i = 0
    first = 0
    second = 1
    while i < n:
      if i == 0 or i == 1:
        yield i
      else:
        value = first + second
        first = second
        second = value
        yield value
      i += 1
        
  results = [x for x in fibonacci(12)]
  Answer(f"fibonacci(12): {results}")
  
  Question(6, """
		Implement a generator that returns all consecutive pairs of numbers from 0 to (n).
 	""")
  
  def pairs(n):
    i = 0
    while i < n:
      yield (i, i+1)
      i += 1
  
  results = [x for x in pairs(5)]
  Answer(f"pairs(5): {results}")  