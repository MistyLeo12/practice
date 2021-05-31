# def alert(number, threshold):
#     print(f"Sensor picked up {number}. Making {number}/{threshold}")


# while True:
#     threshold = 10
#     input_stream = input()
#     if int(input_stream) > threshold:
#         alert(int(input_stream), threshold)
inputA = '11101'
x = int(inputA, 2)
y = int('1', 2)
return_list = []
for i in inputA:
    if (int(i, 2) & y):
        return_list.append(int(i, 2))
print(len(return_list))
print(x & y)
print(x >> y)                                   