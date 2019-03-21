// Call by value, call by name.
// Call by value is where the evaluation is done right after the call
// In call by name, the evaluation is done everytime when ever it is called.

// If CBV evaluation of an expression e terminates, CBN of e also terminates. The converse need not be true.

// Function definitions: The def operator is always call by name. Its right hand side is always evaluated for every time it is called.
// It can take parameters. Can also mention return types.

def square(x: Int) = x * x
def first(x: Int, y: Int) = x
print("First ")
println(first(3,4))

// Scala uses call by value, to force to use call by name, use => operator. CBV To avoid computations of same exp multiple times.
def constOne(x: Int, y: => Int) = 1
print("constOne ")
println(constOne(10,5))

// Value Definitions: The val operator is always call by value. Its right hand side is evaluated right after the definition. And later on the name refers to value.
val x = 2
val y = square(x)
print("val y = ")
println(y)


// Calculate the square root of a double.
// Using Newtons method
// 1. Start with an initial estimate y. (lets pick 1)
// 2. Repeatedly improve the estimate by taking the mean of y and x/y.

// A function to compute the iteration step
// Note: Recursive functions in Scala require explicit return type mention. For non recursive functions return type is optional.
// The Double after parameters is the return type.
def abs(x: Double) = if (x < 0) -x else x

def isGoodEnough(guess: Double, x: Double) = 
	abs(guess * guess - x) / x < 0.001

def improve(guess: Double, x: Double): Double = 
	( guess + x/guess ) / 2

def sqrtIter (guess: Double, x: Double): Double = 
	if (isGoodEnough(guess, x)) guess
	else sqrtIter(improve(guess,x), x)

def sqrt (x: Double): Double = 
	sqrtIter(1.0, x)

print("Sqrt of 2: ")
println(sqrt(2))

print("Sqrt of 1e60: ")
println(sqrt(1e60))