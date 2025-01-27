# run as is then change j to 12
# use the debugger to show the i counter increasing
i = 1
j = 120
while i < 42:
    i = i * 2
    if i > j:
        break
# The break statement exits the loop when a certain condition is met
# Its "friend" is the continue statement, which moves to the next part of the loop without exiting the loop

else:
    print("Loop expired: ", i)

print("Final value: ", i)



# # Using break and continue in a loop
# for i in range(1, 6):
#     if i == 3:
#         print("Skipping number 3")
#         continue  # Skip the current iteration when i is 3
#     elif i == 5:
#         print("Breaking the loop when i is 5")
#         break  # Exit the loop when i is 5
#     print(f"Processing number {i}")