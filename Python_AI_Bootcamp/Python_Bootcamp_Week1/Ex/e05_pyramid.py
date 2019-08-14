def pyramid(level, symbol, is_reverse):
    if is_reverse:
        j = 1
        for i in range(level):
            print(" " * level, symbol * j)
            j += 2
            level -= 1
    else:
        j = 1
        level = level*2-1
        for i in range(level):
            print(" "*j, symbol*level)
            j += 1
            level -= 2


pyramid(5, "A", False)
pyramid(8, "%", True)
pyramid(6, "*" , False)
