def has_same_ingredients(medicine1, medicine2):

    medicine1[1].sort()
    medicine2[1].sort()

    if len(medicine1[1]) <= len(medicine2[1]):
        for i in range(len(medicine1[1])):
            if medicine2[1][i][0] != medicine1[1][i][0]:
                return False
        return True
    else:
        return False


def isStronger(medicine1, medicine2):
    sum_of_divs = 0

    if has_same_ingredients(medicine2, medicine1):
        for i in range(len(medicine2[1])):
            sum_of_divs += medicine1[1][i][1] - medicine2[1][i][1]

        if sum_of_divs > 0:
            return True
        else:
            return False

    else:
        return False


def leastStronger(medicine, lst_of_meds):
    sums = dict()

    for ind in range(len(lst_of_meds)):
        sum_of_divs = 0
        med = lst_of_meds[ind]

        if has_same_ingredients(medicine, med) and isStronger(med, medicine):
            for i in range(len(medicine[1])):
                sum_of_divs += med[1][i][1] - medicine[1][i][1]

            sums[ind] = sum_of_divs

    if sums == {}:
        return []
    else:
        minimum_difference = min(sums.values())

        for k, v in sums.items():
            if v == minimum_difference:
                index = k

        return lst_of_meds[k]


def strongRelation(list_of_medicines):
    result = list()

    for medicine in list_of_medicines:
        stronger_medicines = list()

        for med in list_of_medicines:
            if isStronger(med, medicine) is True:
                stronger_medicines.append(med[0])

        result.append((medicine, stronger_medicines))

    return result


if __name__ == "__main__":
    A = ("A", [("p", 5), ("q", 3)])
    B = ("B", [("p", 4), ("q", 3)])
    C = ("C", [("p", 3)])
    D = ("D", [("p", 4.5), ("q", 3), ("r", 1)])

    print(has_same_ingredients(A, D))
    print(isStronger(A, D))

    # print(leastStronger(B, [A, C, D]))

    list_of_medicines = [A, B, C, D]
    print(strongRelation(list_of_medicines))
