def find_chars1(string1,string2):
    "version N implementation to find the intersect of string1 and string2"
    return_str = ""
    for char in string1:
        if char in string2 and char not in return_str:
            return_str += char  
    return return_str
    



def find_chars2(string1, string2):
    "version N*N implementation to find the intersect of two strings"
    return_str = ""
    for char in string1:
            for xchar in string2:
                    if char == xchar and char not in return_str:
                        return_str += char
    return return_str

            



def compact_array(array):
    "returns a compacted list removing duplicates"
    return list(set(array))





def rotate_array(array, n):
    "rotates array by n positions"
    for counter in range(n):
        array.insert(0, array.pop())
    return array






 def lcm(*values):
    "takes any number of comma seperated values and returns the lcm of the numbers"
    values = set([abs(int(v)) for v in array])
    print values
    if values and 0 not in values:
        n = n0 = max(values)
        values.remove(n)
        while any( n % m for m in values ):
            n += n0
            return n
    return 0



















