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

# HOW I DEBUGGED MY CODE:
# 1. I ran the code and saw odd numbers whereby my target was to remove them and have even numbers .
# 2. I checked the terminal and it was giving the odd numbers.
# 3. I found the problem: removing items while looping caused issues.
# 4. I also noticed the return statement was inside the loop.
# 5. I realized that the return statement was causing the function to exit prematurely, which is why it was not processing all items in the list.
#6. I decided to move the return statement outside the loop so that it would only return after all items have been processed.
#7. I moved the return statement outside the loop and ran the code again to see if it worked.
#8. I fixed it by making the loop finish and return at the end.
#9. I moved the return statement outside the loop and ran the code again to see if it worked.
#10. I ran the code again and it worked as expected, giving me only the even numbers in the list.
#11. Now the function gives the correct result of the even numbers.