import matplotlib.pyplot as plt


file_path = f'C:/Users/Paul/Downloads/'
scores = []
with open(file_path + 'temp5.txt') as f:
    for line in f.readlines():
        scores.append(float(line))


print(scores)

print(f"average: {sum(scores) / len(scores):0.4f}")
print(f"min: {min(scores)}")
print(f"max: {max(scores)}")





