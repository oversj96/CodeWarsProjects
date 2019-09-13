def who_eats_who(zoo):
    dict_foodchain = {"bear": ("chicken", "cow", "leaves", "sheep", "bug", "big-fish"),
                      "antelope": "grass",
                      "big-fish": "little-fish",
                      "bug": "leaves",
                      "chicken": "bug",
                      "cow": "grass",
                      "fox": ("chicken", "sheep"),
                      "giraffe": "leaves",
                      "lion": ("antelope", "cow"),
                      "panda": "leaves",
                      "sheep": "grass"}
    mosh_pit = zoo.split(',')
    i = 0
    output = [zoo]
    while i < len(mosh_pit) - 2:
        for anim, food in dict_foodchain.items():
            if mosh_pit[i] is anim and mosh_pit[i + 1] in food:
                output.append(anim + " eats " + mosh_pit.pop(i + 1))
            elif i > 0 and mosh_pit[i] is anim and mosh_pit[i - 1] in food:
                output.append(anim + " eats " + mosh_pit.pop(i - 1))
        i += 1
    output.append(mosh_pit[0])
    return output


print(who_eats_who("fox,bug,chicken,grass,sheep"))
print()
