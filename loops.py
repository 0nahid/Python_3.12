import time

start_time = time.time()
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")
x = 10
# while x > 0:
#     print(x)
#     x = x - 1

x = 10
for i in range(10, 0, -1): # here 10 is the start, 0 is the end and -1 is the step
    print(i)
    


# 0.6869761943817139
# 0.7406010627746582
# 0.6910970211029053
# 0.7653689384460449
# 0.6037797927856445