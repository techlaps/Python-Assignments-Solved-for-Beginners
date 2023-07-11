maths_mul_table_num = int(input("Enter a number to create the mathematics multiplication table? "))
maths_mul_table_end_num = int(input("Enter a number for end position of mathematics multiplication table?"))

print("\nMathematics multiplication table of {} till {}".format(maths_mul_table_num, maths_mul_table_end_num))
for i in range(1, (maths_mul_table_end_num + 1)):
    print("{}x{}={}".format(i, maths_mul_table_num, (i*maths_mul_table_num)))