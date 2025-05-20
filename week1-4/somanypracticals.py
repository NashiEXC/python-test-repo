count= int(input("Nuber of books: "))
price= float(input("price of books: "))
subtotal = price * count
gst = 0.07 * subtotal
total= subtotal + gst
print(f"subtotal: {subtotal}\n gst: {gst}\n total: {total}")
