import pandas as pd

weight1 = 0.5
weight2 = 0.5
bias = 0

test_input = [(0, 0), (0, 1), (1, 0), (1, 1)]
correct_outputs = [False, True, True, True]
outputs = []

for test_input, correct_outputs in zip(test_input, correct_outputs):
    linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
    output = int(linear_combination > 0 )
    is_correct_string = 'Yes' if output == correct_outputs else 'No'
    outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

#print the result
num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
output_frame = pd.DataFrame(outputs, columns = ['Input 1', ' Input 2', ' Linear combination', ' Active Ouput', ' Is Correct'])
if not num_wrong:
    print("You got it!")
else:
    print("You have {} wrong.">format(num_wrong))

print(output_frame.to_string(index = False)) #index索引去掉
