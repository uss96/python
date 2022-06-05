def say_hello_name(name) :
    print ("안녕하세요, ", name)

def say_hello_name_msg(name, msg) :
    print("안녕하세요, ", name, msg)

def get_sum(start, end):
    hap = 0
    for i in range(start, end+1):
        hap += i
    return hap