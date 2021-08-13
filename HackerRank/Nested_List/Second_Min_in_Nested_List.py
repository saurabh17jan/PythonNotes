import math

if __name__ == '__main__':

    min_value = math.inf
    min_ppl = []
    second_min_value = math.inf
    second_min_ppl = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score == min_value:
            # check if current score is the new lowest_value
            min_ppl.append(name)
        elif score < min_value:
            # check if current score is lower then that previous lowest_value
            second_min_value = min_value
            second_min_ppl = min_ppl
            min_value = score
            min_ppl = [name]
        elif score == second_min_value:
            # check if current score is equal to  second_lowest_value
            second_min_ppl.append(name)
        elif score < second_min_value and score > min_value:
            # check if current score lies between lowest and the second_lowest_value
            second_min_value = score
            second_min_ppl = [name]
    second_min_ppl.sort()
    for i in second_min_ppl:
        print(i)

