from _11_06.tools import Factory

if __name__ == '__main__':
    try:
        F = Factory(load=True, count=100, debug=True)
    except Exception as e:
        print(e)
