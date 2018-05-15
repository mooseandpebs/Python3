



def get_list(num_items):
    nums = []
    for x in range(0,num_items):
        nums.append(x)
    return nums


items = get_list(12)

def windows(items_list,window_size):
    start=0
    while start < len(items_list):
        yield int(start),int(start+window_size)
        start += (window_size/2)


for (start,end) in windows(items,4):
    print('start:{} end:{} list:{}'.format(start,end,items[start:end]))