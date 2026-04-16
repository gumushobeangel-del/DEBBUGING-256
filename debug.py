def clean_database(record_ids):
# Requirement: Remove all odd numbers from the list
  for record_id in record_ids[:]:  # Iterate over a copy of the list to avoid modification issues
   if record_id % 2 != 0:
    record_ids.remove(record_id)
  return record_ids
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [3, 4, 6, 9, 10]



def clean_database(record_ids):
  new_list = []  # Open a new list to store even numbers
  for record_id in record_ids:
    if record_id % 2 == 0:  # Check if the number is even
      new_list.append(record_id)  # Put even numbers to the new list
  return new_list  # Return the new list containing only even numbers
# Test Case
data = [1, 3, 4, 6, 7, 9, 10]
cleaned = clean_database(data)
print(f"Final List: {cleaned}")
# EXPECTED: [4, 6, 10]
# ACTUAL: [4, 6, 10]


# COMMENTS USING THE ORIGINAL LIST:
# 1. I ran the code and saw odd numbers whereby my target was to remove them and have even numbers .
# 2. I checked the terminal and it was giving the odd numbers.
# 3. I found the problem: removing items while looping caused issues.
# 4. I also noticed the return statement was inside the loop.
# 5. I realized that the return statement was causing the function to exit prematurely.
#6. I decided to fix the issue by moving the return statement outside the loop, allowing the loop to finish processing all items before returning the final list.
#7. I moved the return statement outside the loop and ran the code again to see if it worked.
#8. I fixed it by making the loop finish and return at the end.
#9. I ran the code again and it still gave me odd numbers, which meant that the issue was not fully resolved.
#10. I realized that the issue was that I was modifying the list while iterating over it, which caused some items to be skipped.
#11. To fix this, I decided to iterate over a copy of the list (using record_ids[:]) to avoid modifying the original list while iterating.
#10. I ran the code again and it worked as expected, giving me only the even numbers in the list.
#11. The final output is [4, 6, 10], which is the expected result.
#12. The issue was that modifying the list while iterating caused some items to be skipped
#11. Now the function gives the correct result of the even numbers.
#13. The issue was that the return statement was inside the loop, 
#14.which caused the function to exit after processing only the first item. By moving the return statement outside the loop, 
#15.we ensure that all items are processed before returning the final list.
#16. The final output is now correct, and the function works as intended to remove odd numbers and return only even numbers in the list.


#MY COMMENTS USING THE NEW LIST:
#1. I created a new list called new_list to store only the even numbers.
#2. I iterated through each record_id in the original list and checked if it was even.
#3. If the record_id was even, I appended it to the new_list.
#4. After the loop, I returned the new_list which contains only the even numbers.
#5. I ran the code again and it worked as expected, giving me only the even numbers in the list.
#6. The final output is [4, 6, 10], which is the expected result.
#7. This approach avoids modifying the original list while iterating, which can lead to unexpected behavior. By creating a new list, 
#8.we ensure that we are not altering the list we are iterating over, thus avoiding any issues with skipping elements or incorrect indexing.
#9.The function now correctly returns a list of even numbers, and the original list remains unchanged if needed for other operations.
