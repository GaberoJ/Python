import sys

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    if int(sys.argv[1]) > len(f.readlines()):
        sys.exit('Столько булочек мы еще не продали')
    f.seek(8 * (int(sys.argv[1]) - 1))
    f.write(sys.argv[2])

# пример для консоли: python .\task7.py 3 9999,9