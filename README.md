# lesson22
Creating a Point of Sale System Part 1

The File Contains all the Widgets that will be used in the point of sale system.  Use the code to start your project.  Feel free to modify the gui as needed to fit your enhancements.

Part 1 
Make two list of lists structures.  One called Products, another called Customers.

Customers will be formatted like this:
[CustomerNumber, Name, phoneNumber]

Example:
Customers = [["9230", "John Doe", 4192229999], ["0001","First Customer", 8886667777], ["0002", "Second Customer", 7659287162]]

Products will be formatted like this:
[Barcode number, name of product, price, quantity]

Example:
Products = [["10232", "Pens Pack of 10", 2.99, 43], ["11111", "Folders", 3.99, 34], ["00001", "Pencils", .99, 24], ["92932", "Stationary", 4.99, 53]]

Using these two data structures.  Program the GUI so that when you type in the correct product ID and press the enter button, it will populate the labels.  Do the same for the Customers.

When the user presses purchase, it should populate the listbox with the product name and price.

What happens when the user hasn't entered a product ID yet?

We will handle this issue in the next lesson.

