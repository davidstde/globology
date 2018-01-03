#! python3

from shutil import copyfile
from os import path

def continents(c):
    return {
        1: 'africa',
        2: 'americas',
        3: 'antarctica',
        4: 'asia',
        5: 'europe',
        6: 'oceania'
}[c]

def contries(c):
    p = '.\\' + continents(c) + '\\_names.txt'
    names = []

    if not path.exists(p):
        print('can\'t read names.txt')
    else:
        for line in open(p):
            try:
                li = line.strip()
                if not li.startswith('#'):
                    names.append(line.rstrip())
            except:
                print('...')
    return names

c = int(input('''
Select the continent:
    1. Africa
    2. Americas
    3. Antarctica
    4. Asia
    5. Europe
    6. Oceania
'''))
src = '.\\template.md'
names = contries(c)
count = 0

for name in names:
    dst = '.\\' + continents(c) + '\\' + name + '.md'
    if not path.exists(dst):
        copyfile(src, dst)
        count +=1

print('{} files are copied.'.format(count))
