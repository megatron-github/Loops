"""
 *****************************************************************************
   FILE:          microwave.py

   DESCRIPTION:	This program will countdown the second on the microwave for 
                  you.
                  
                  Here is a sample interaction with this program:
                  Enter the digits as input to the microwave: 10:03
                  10:03
                  10:02
                  10:01
                  10:00
                  9:59
                  9:58
                  9:57
                  ...
                  0:03
                  0:02
                  0:01
                  0:00
                  
 *****************************************************************************
"""

def main():
    """ This function will print out every count of second
        from input time to 0:00 """
      
    input_time = input("Enter the digits as input to the microwave: ")
    minute = int(input_time[:input_time.find(":")])  
    second = int(input_time[input_time.find(":") + 1:])
    #time = the total minutes in input time
    time = minute * 60 + second
    
    for count in range(1, time + 2):
        #when input is 1:00 or 4:00,
        #minus the minutes by one and ad 59 to second
        if second == 0 and minute > 0:
            print("{:01d}:{:02d}".format(minute, second))
            minute = minute - 1
            second = second + 59
        #when input is 0:00, break the loops
        if second == 0 and minute == 0:
            print("{:01d}:{:02d}".format(minute, second))
            break
        if count > 0:
            print("{:01d}:{:02d}".format(minute, second))
            second = second - 1
            
# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
