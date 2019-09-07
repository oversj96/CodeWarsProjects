def diamond(n):
    if(n < 1 or n % 2 == 0):
        return None
    else:
        pyramid = []      
        for i in range(1, n+1, 2):
            row = ""
            spaces = (n - i) // 2
            for j in range(0, spaces):
                row += " "
            for k in range(0, i):
                row += "*"
                if(k == i-1):
                    row += "\n"
            pyramid.append(row)
            bottom = pyramid[0:len(pyramid)-1]
            bottom.reverse()
        diamond = pyramid + bottom
        return ''.join(diamond)

print(diamond(5))