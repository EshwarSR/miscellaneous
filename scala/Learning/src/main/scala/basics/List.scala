package basics

import java.util.NoSuchElementException

// Traits are similar to Interfaces in Java, but more powerful because they can also have definitions.
// Traits are used when we need something like multiple inheritance, as Scala supports only SingleInheritance.
// Traits are similar to classes but the main difference is that it cannot take parameters.

trait List[T] {

  def isEmpty: Boolean
  def head: T
  def tail: List[T]

}

class Cons[T](val head: T, val tail: List[T]) extends List[T]{

  def isEmpty: Boolean = false

}

class Nil[T] extends List[T]{

  def isEmpty: Boolean = true
  def head: Nothing = throw new NoSuchElementException("Nil.head")
  def tail: Nothing = throw new NoSuchElementException("Nil.tail")

}
