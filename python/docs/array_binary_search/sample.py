def binary_search(list_in, target):
    jump_size = int(len(list_in) / 2)
    search_point = jump_size
    latch = False

    while target != list_in[search_point]:
        if target > list_in[search_point] and latch == False:
            jump_size = int((jump_size + 1) / 2)
            search_point += jump_size

            if jump_size == 1:
                latch = True

        elif target < list_in[search_point] and latch == False:
            jump_size = int((jump_size + 1) / 2)
            search_point -= jump_size

            if jump_size == 1:
                latch = True

        else:
            return -1
    return search_point


binary_search([-131, -82, 0, 27, 42, 68, 87, 93, 95, 99, 150, 151, 179], 129)
