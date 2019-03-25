// Class definitions

// Abstract classes may not contain function definitions.
// An object CANNOT be created from abstract classes using new.

abstract class IntSet
{
  def incl(x: Int): IntSet
  def contains(x: Int): Boolean
  def union(other: IntSet): IntSet
}

// Lets create a binary search tree for illustration purposes.

class NonEmpty (elem: Int, left: IntSet, right: IntSet) extends IntSet
{
  def contains(x: Int): Boolean = {
    if(x < elem) left contains x
    else if (x > elem) right contains x
    else true
  }

  // incl return a new data structure, it keeps the old one intact. (Both might share the same sub trees)
  // this method is called persistent data structures.
  def incl(x: Int): IntSet = {
    if (x < elem) new NonEmpty(elem, left incl x, right)
    else if (x > elem) new NonEmpty(elem, left, right incl x)
    else this
  }

  def union(other: IntSet): IntSet = {
    ((left union right) union other) incl elem
  }
  override def toString: String = "{" + left + elem + right + "}"

}

class Empty extends IntSet
{
  def contains(x: Int): Boolean = false
  def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
  override def toString: String = "."
  def union(other: IntSet): IntSet = other
}

// Both Empty and NonEmpty are extended by IntSet, i.e they are subclass of IntSet.
// That means, Empty and NonEmpty can be used where ever IntSet is required

// When a definition is mentioned in super class and we are redefining it in subclass, then override keyword is mandatory


// Object definitions, one can argue that there can be only one Empty instance.

// So in that case we can define an object directly and use it.
// Defining object is same as class but use keyword object instead of class.
// No other instances of it can be created.
// Singleton objects are values and its name evaluates to itself


// Driver code
object driver
{
  val t1 = new NonEmpty(3, new Empty, new Empty)
  println(t1)
  val t2 = t1 incl 4
  println(t2)

}

driver