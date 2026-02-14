#Case Study 2 : Education Result Evaluation
marks=82

if marks>=75:
    category="Distinction"
elif marks>=60:
    category="First Class"
elif marks>=40:
    category="Pass Class"
else:
    category="Fail"

print("Student scored: ",marks)
print("Result Category: ",category)
