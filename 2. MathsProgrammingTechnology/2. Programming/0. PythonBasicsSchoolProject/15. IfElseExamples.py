# Shopping Cart Discount:
# Scenario: An online store offers a 10% discount if the cart total exceeds $100.  10 % means 10 parts out of 100 parts will be discounted. So you have to pay 90 out of 100 parts.
print("\n\nShoppingDiscounts:  ")
def discountedPrice(cart_total):
    if cart_total > 100:
        discount = cart_total * 0.10
        final_price = cart_total - discount
        # final_price = cart_total * 0.9   ## This is same as above
        print("Discount applied! Your final price is:", final_price)
        return final_price
    else:
        print("No discount applied! Your total is:", cart_total)
        return cart_total

discountedPrice(200)
discountedPrice(80)
discountedPrice(100)
discountedPrice(101)  # Buying products worth 101$ is cheaper than buying products worth 100$ because, we get 10% off on 101$ and spend only 90.9$


# Traffic Light Simulation:
# Scenario: Control the behavior of a traffic light based on the current color.
print("\n\nTrafficAction:  ")
def trafficActions(light_color):
    if light_color == "green":
        print("Go!")
    elif light_color == "yellow":
        print("Slow down!")
    elif light_color == "red":
        print("Stop!")

trafficActions('green')
trafficActions('yellow')
trafficActions('red')



#Grade Calculator:
#Scenario: Assign letter grades based on numerical scores.
print("\n\nGradeCalulation:  ")
def gradeCalculator(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Your grade is:", grade)
    return grade
gradeCalculator(45)
gradeCalculator(102)
gradeCalculator(93)
gradeCalculator(80)