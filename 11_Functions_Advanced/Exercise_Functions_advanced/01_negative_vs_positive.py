numbers = [int(x) for x in input().split()]


def find_negatives_positives(nums_list: list, ns=0, ps=0):
    for num in nums_list:
        if num < 0:
            ns += num
        else:
            ps += num
    return ns, ps


negatives, positives = find_negatives_positives(numbers)
print(f"{negatives}\n{positives}")
print("The negatives are stronger than the positives" if abs(negatives) > positives
      else "The positives are stronger than the negatives")
