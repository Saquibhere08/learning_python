#Case Study: Retail Billing (Kirana Store)
#item details
item_price1,item1_qty=40,2
item_price2,item2_qty=30,3

#calculate total
item_total1= item_price1 * item1_qty
item_total2= item_price2 * item2_qty

#subtotal
subtotal=item_total1 +item_total2

#discount
discount=20
final_total=subtotal-discount

#print
print("Subtotal: ",subtotal)
print("Discount: ",discount)
print("Total: ",final_total)