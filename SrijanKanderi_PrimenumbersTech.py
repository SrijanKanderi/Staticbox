def is_part_of_series(lst):
    ## Remove duplicates from lst
    lst = list(set(lst))
    templist = []

    if min(lst)<0:
        print("Negative entries in lst ignored. Showing results for n>1 only: \n")

    def f(n):
        if n == 0:
            ans = 0
        if n == 1:
            ans = 1
        if n > 1:
            ans = 9 * (f(n - 1)) - 7 * (f(n - 2))
        return ans

    ###Append series into templist upto the max element in lst
    flag = True
    counter = 0
    while flag == True:
        if f(counter) <= max(lst):
            templist.append(f(counter))
            counter += 1

        else:
            flag = False



    print("Input Lst:",lst)

    common_elements = [x for x in lst if x in templist]

    if len(common_elements) < len(lst) and len(common_elements) != 0:
        print("All the elements dont belong to series. Showing matching entries:\n",common_elements)

    if len(common_elements) == len(lst):
        print("All the elements of lst belong to series.")

    if len(common_elements) == 0:
        print("None of the elements in array belong to the series")



lst = input("Enter integers of the lst divided by comma").split(",")
lst = list(map(int,lst))
is_part_of_series(lst)




















