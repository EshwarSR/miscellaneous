object BlocksAndScope
{
  //  Blocks are defined within {}
  //  The last expression in the block is the return value
  def sqrt (x: Double): Double = {
    def abs(x: Double) = if (x < 0) -x else x

    def isGoodEnough(guess: Double, x: Double) =
      abs(guess * guess - x) / x < 0.001

    def improve(guess: Double, x: Double): Double =
      ( guess + x/guess ) / 2

    def sqrtIter (guess: Double, x: Double): Double =
      if (isGoodEnough(guess, x)) guess
      else sqrtIter(improve(guess,x), x)

    sqrtIter(1.0, x)
  }

  println(sqrt(2))
  println(sqrt(1e-6))
  println(sqrt(1e60))

}

BlocksAndScope