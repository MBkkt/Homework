if __name__ == '__main__':
    arr = list(map(lambda x: x**5, range(1, 150)))
    for a in arr:
        for b in arr:
            for c in arr:
                for d in arr:
                    s = sum((a, b, c, d))
                    if s in arr:
                        print(a, b, c, d, s)
