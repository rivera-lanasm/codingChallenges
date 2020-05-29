

## Arrays Introduction
- DVD box anaology
- convept of capacity, size
- The two most primitive Array operations are writing elements into them, and reading elements from them. 
  - All other Array operations are built on top of these two primitive operations.
- Array Capacity VS Length: capacity is an attribute of the array, length is not tracked as an attribute
- When an Array is given as a parameter, without any additional information, you can safely assume that length == capacity

**Max consecutive Ones in Binary Array**
using recursion:
~~~
object Solution {
  
    def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
      val nums_l = nums.toList

      def loop(cur: List[Int], acc: Int, c_seq: List[Int]): Int = cur match {
        case h :: t if h ==0 => loop(t, 0, c_seq.concat(List(acc)))
        case h :: t if h ==1 => loop(t, acc + h, c_seq)
        case _      => c_seq.concat(List(acc)).max
      }

  loop(nums_l, 0, List(0))
    }

}



~~~
