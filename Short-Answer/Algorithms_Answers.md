#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Linear Time - it has one loop.


b) 0(n^2) - Quadratic Time - it's has a loop nested in a loop


c) 0(n) - Linear Time - it's a recursion that keeps calling itself and reducing each call by 1

## Exercise II

def egg_drop_test(n):

  if you drop egg from top floor and it doesnt break:
    return "you have unbreakable egg"

  else if you drop egg from bottom floor and it breaks:
    return "you have weak eggs"

  else start testing which floor will crack the egg.
    can traverse each floor ground-up or start with the middle floor

    mid_floor is the building floors / 2

    if at mid_floor and egg doesnt break:
      keep going up one floor at a time til egg breaks.

      if egg breaks:
        return all the floors below current floor.
    
    else if it does break at mid floor:
      keep doing down until it doesnt break
      return current floor and below. 

runtime: 0(log n) since it's a binary search