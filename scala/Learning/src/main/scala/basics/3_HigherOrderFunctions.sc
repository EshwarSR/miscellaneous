// Functions which take functions as parameters and return funcrions are called "Higher order Functions".
// Function types are represented as A => B, where its a function which takes param of type A and return type B.
// Anonymous function syntax: (x: Int) => x * x

object HigherOrderFunctions
{
  def sum(f: Int => Int, a: Int, b: Int) : Int = {
    def loop(a: Int, acc: Int): Int = {
      if (a > b) acc
      else loop(a + 1, f(a) + acc)
    }
    loop(a, 0)
  }

  println(sum(x => x * x, 3, 5))
}

HigherOrderFunctions

// Currying
object HigherOrderFunctions2
{
  def product(f: Int => Int)(a: Int, b: Int): Int = {
    if (a>b) 1 else f(a) * product(f)(a+1, b)
  }

  println(product(x => x * x)(3, 4))

  def fact(n: Int): Int = product(x => x)(1, n)
  println(fact(3))

  def mapReduce(f: Int => Int, combine: (Int, Int) => Int, zero: Int)(a: Int, b: Int): Int = {
    if (a > b) zero
    else combine(f(a), mapReduce(f, combine, zero)(a+ 1, b))
  }
  println(mapReduce(x => x , (x, y) => x * y,1)( 3, 4))

}

HigherOrderFunctions2
