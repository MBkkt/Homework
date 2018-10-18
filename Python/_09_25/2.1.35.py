''' Календарь. Составьте программу cal . ру, получающую в аргументах
командной строки два числа, m и у, и выводящую месячный календарь
для месяца m в году у, как в следующем примере: '''
import calendar


def draw(m, y):
    d = {12: 'December', 1: 'January', 2: 'February',
         3: 'March', 4: 'April', 5: 'May',
         6: 'June', 7: 'July', 8: 'August',
         9: 'September', 10: 'October', 11: 'November', }
    ans = f'{d[m]} {y}\n'
    ans += 'S\tM\tTu\tW\tTh\tF\tS\n'
    s = ''
    for k, i in enumerate(calendar.Calendar(firstweekday=6).itermonthdays(y, m), start=1):
        if i == 0:
            i = ''
        if k % 7 == 0:
            ans += f'{s}{i}\n'
            s = ''
        else:
            s += f'{i}\t'

    return ans


if __name__ == '__main__':
    month, year = map(int, input().split())
    print(draw(month, year))
