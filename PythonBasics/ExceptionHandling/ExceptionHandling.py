import traceback


def simple_interest(amount, time, rate):
    try:
        if rate > 100 or rate < 0:
            raise ValueError(rate)

        if time > 30 or time < 0:
            raise ValueError(time)

        interest = (amount * rate * time) / 100
        return interest
    except Exception as e:
        raise e


print("case 1 ****")
print(simple_interest("anshul", 4, 9))

print("case 2 ****")
simple_interest(100, 50, 9)

print("case 3 ****")
simple_interest(100, 50, -9)

# def addition():
#     try:
#         a = int(input("Provide value of a : "))
#         b = int(input("Provide value of b : "))
#         print("Devision of a and b is ", a/b)
#     except ZeroDivisionError as err:
#         print("Not divided by Zero, Provide some valid value")
#         print("Error : ", err)
#         traceback.print_exc()
#     except ValueError:
#         print("Please provide valid integer as Value of a or b")
#     except:
#         traceback.print_exc()
#     else:
#         print("Within the Else Block")
#     finally:
#         print("This is finally block")
#
# addition()
