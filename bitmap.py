import sys 

bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''

print("Bitmap message, by Dennis Osadchuk")
print("Enter the message to display it with the bitmap")
message = input("> ")

if message == "":
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == " ":
            print(" ", end="")
        else:
            print(message[i % len(message)], end="")
    print()