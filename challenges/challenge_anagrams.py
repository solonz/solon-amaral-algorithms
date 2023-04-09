def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string = quicksort(first_string)
    second_string = quicksort(second_string)

    if len(first_string) == 0 or len(second_string) == 0:
        return (first_string, second_string, False)

    return (first_string, second_string, first_string == second_string)


def quicksort(string):
    if len(string) <= 1:
        return string
    else:
        pivot = string[0]
        less = []
        greater = []

        less = [el for el in string[1:] if el <= pivot]
        greater = [el for el in string[1:] if el > pivot]

        return quicksort("".join(less)) + pivot + quicksort("".join(greater))
