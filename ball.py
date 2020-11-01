"""
 *****************************************************************************
   FILE:        ball.py

   AUTHOR:      Truong Pham

   ASSIGNMENT:  Project 3: Part 2

   DATE:        9/12/18

   DESCRIPTION:	Find the total distance traveled of a drop ball

 *****************************************************************************
"""

def main():
    """ This function calculate the distance traveled by a bouncing
        ball as it drop from a given height """
    drop_height = float(input("Enter initial height: "))
    bounce = float(input("Enter height of first bounce: "))
    bounce_counted = float(input("Enter number of bounces: "))
    
    bounciness = bounce / drop_height
    distance = drop_height
    successive_bounce = bounce
    successive_drop = 0
    
    for count in range(int(bounce_counted)):
        if count >= 0:
            distance = distance + successive_bounce + successive_drop
            successive_drop = successive_bounce
            successive_bounce = bounciness*successive_bounce
            
    print("The total distance the ball traveled " \
          "is {} feet.".format(round(distance, 2)))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
