files = ['a.txt',
    # 'b.txt',
    # 'c.txt',
    # 'd.txt',
    # 'e.txt',
    # 'f.txt',
    ]

def reader(idx=0):
    
    curr_file = files[idx]
    # read file
    with open(curr_file) as f:
        content = f.readlines()
        return content
    # r----------------------------


def writer(content, idx=0):
        
    curr_file = files[idx]
    # write file out
    with open(curr_file+'_2out.txt', 'a') as the_file:
            the_file.write(str(content))
    # try:
    #     with open(curr_file+'_out.txt', 'a') as the_file:
    #         for i in content:
    #             the_file.write(i)


        