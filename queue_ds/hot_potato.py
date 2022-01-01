def hot_potato(name_list, num):
    sim_queue = []

    for name in name_list:
        sim_queue.insert(0, name)

    while len(sim_queue) > 1:
        for i in range(num):
            sim_queue.insert(0, sim_queue.pop())
    
        sim_queue.pop()
    
    return sim_queue.pop()


if __name__ == '__main__':
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

