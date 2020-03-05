import sys,os
import glob
import collections

print("Checking for broken symlinks...")

links = []
broken = []

curr_txt_files = glob.iglob('C:\\git_intg_cleanup\\fusion\\11.13.20.01' + '\\**\\*.txt', recursive=True)

for itm in curr_txt_files:
    head,tail = os.path.split(itm)
    links.append(tail)

print(len(links))  
print([item for item, count in collections.Counter(links).items() if count > 1])

for path in curr_txt_files:
    print(1)
    if os.path.islink(path):
        target_path = os.readlink(path)
        if not os.path.isabs(target_path):
            target_path = os.path.join(os.path.dirname(path),target_path)             
        if not os.path.exists(target_path):
            links.append(path)
            broken.append(path)
        else:
            links.append(path)
    else:
        # If it's not a symlink we're not interested.
        continue

print(len(links), 'symlinks found...')
if broken == []:
    print('OK')
else:
    print("broken symlink(s) found:")
    for link in broken:
        print(link)
