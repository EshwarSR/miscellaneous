// Class definition
class Rational(x: Int, y: Int)
{
  // require is a predefined function which takes condition and message string as parameters
  //  if the condition becomes false, IllegalArgumentException is thrown with the message string
  require(y != 0, "denominator cannot be zero")

  // A secondary constructor which takes only one parameter
  // this when used in function definition is a constructor.
  // The default constructor of the class is the definition itself. invoked in the RHS this in below example
  def this(x: Int) = this(x, 1)

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a%b)

  private val g = gcd(x, y)

  val numer = x / g
  val denom = y / g

  // In the same class numer and denom can be accessed either as numer and denom or as this.numer and this.denom
  def add(that: Rational): Rational = {
    new Rational(
      numer * that.denom + denom * that.numer,
      denom * that.denom
    )
  }

  def neg : Rational = new Rational(-1 * numer,denom )

  def sub(that: Rational): Rational = add(that.neg)

  def less(that: Rational): Boolean = numer * that.denom < that.numer * denom

  // this is same as this in Java
  def max(that: Rational): Rational = if(less(that)) that else this

  // example of + operator as a method
  def + (that: Rational): Rational = {
    new Rational(
      numer * that.denom + denom * that.numer,
      denom * that.denom
    )
  }

  override def toString = numer + "/" + denom

}

// Driver code
object Rationals
{
  val x = new Rational(1,2)
  println(x.numer)
  println(x.denom)

  val y = new Rational(3,4)

  println(x.add(y))

//  Lets take 3 rationals and do a - b - c
  val a = new Rational(1,3)
  val b = new Rational(5,7)
  val c = new Rational(3,2)
  print("a-b-c = ")
  println(a.sub(b).sub(c))

  println(b.add(b))

  print("a less b ")
  println(a.less(b))

  print("max of a and b ")
  println(a.max(b))

  // Below lines produce the IllegalArgumentException
  //  val t = new Rational(1,0)
  //  t.add(t)

  print("Single parameter Rational ")
  println(new Rational(2))

  // In scala calls can be infix. Ex: a.add(b) can be written as a add b
  print("Using infix call :")
  println(a add b)

  // With the help of above infix notation we can do something like operator overloading as we do in C++
  print("Using + operator : ")
  println(a + b)

  // When using operator symbols as function names, the precedence is calculated based on the first character in the function name
  // Same precedence rules as that of Java

}

Rationals
