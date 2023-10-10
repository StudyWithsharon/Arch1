#Input_ser
Widget_input = int(input("Enter the number of Widgets you want to order "))
Gizmo_input = int(input("Enter the number of Widgets you want to order "))

#Fixed_data
Widget_weight = 75
Gizmo_weight = 112

#Processing
Total_weight = Widget_input * Widget_weight + Gizmo_input * Gizmo_weight

#Output giving the result
print("The total weight of your order is", Total_weight)
