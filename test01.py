def asteroidCollision(asteroids):
    res = []
    for char in asteroids:
        if char < 0 and not res:
            res.append(char)
        elif char > 0:
            res.append(char)
        elif char < 0 and res:
            answer = False
            while res[-1] > 0:
                if res[-1] < abs(char):
                    res.pop()
                if res[-1] == abs(char):
                    res.pop()
                    break
                else:
                    break
            if answer == True:
                res.append(char)
    return res

print(asteroidCollision([-1,2,-1,2,-3,4]))
