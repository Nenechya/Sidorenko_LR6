from Sidorenko_LR6_Methods_part1 import user_inp, average_grade, is_good

math_grade = user_inp()
phys_grade = user_inp()
chem_grade = user_inp()


print(average_grade(math_grade, phys_grade, chem_grade))
is_good(math_grade, phys_grade, chem_grade)