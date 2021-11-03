from guizero import App, PushButton, Text, TextBox, ListBox, Box

MainWindow = App("Cash Register", 800, 800)

CustomerBox = Box(MainWindow, layout="grid", border = 1)
ProductBox = Box(MainWindow, layout ="grid", border = 1)
CartBox = Box(MainWindow, layout = "grid",border = 1)

CustText = Text(CustomerBox, text = "Customer ID Number", grid=[0,0])
CustIDTextBox = TextBox(CustomerBox, grid=[0,1])

EnterCustButton = PushButton(CustomerBox, text="Enter", grid=[1,1])
AddCustButton = PushButton(CustomerBox, text="Add/Edit Customer", grid=[2,1])
CustNameText = Text(CustomerBox, text = "Name:", grid=[0,2])
CustPhoneText = Text(CustomerBox, text = "Phone:", grid=[1,2])

EnterProductButton = PushButton(ProductBox, text="Enter", grid=[1,1])
ProductText = Text(ProductBox, text = "Product ID Number", grid=[0,0])
ProductIDTextBox = TextBox(ProductBox, grid=[0,1])
AddProductButton = PushButton(ProductBox, text="Add/Edit Product", grid=[2,1])
ProdNameText = Text(ProductBox, text="Name:", grid=[0, 2])
ProdCostText = Text(ProductBox, text = "$", grid=[1,2])

PurchaseButton = PushButton(CartBox, text = "Purchase", grid=[0,0])
CartListBox = ListBox(CartBox, grid=[0,1])
TotalText = Text(CartBox, text = "Total: $0.00", grid=[0,2])
CheckOutButton = PushButton(CartBox, text = "Check Out", grid = [0,3])
