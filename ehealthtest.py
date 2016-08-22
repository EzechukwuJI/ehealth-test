
## Project:           eHealth Africa Short Programming Test
## Author:           Ezechukwu James Ikechukwu
## Date:              21/08/2016
## Language:       Python
## Github Repo:   https://github.com/EzechukwuJI/ehealth-test.git






'''AN ALGORITHM TO TRAVERSE A TREE - DEPTH FIRST

The depth-first tree traversal otherwise known as depth-first search is an algorithm
for searching a tree data structure. This approach starts at an arbitrary node and
explores as far as possible along each branch before branching off to another node.
Tree traversal using the Depth-first approach is more efficiently handled using a recursive
approach.

Given a tree or a graph dataset with multiple level eg. A large filesystem with multi level
sub directories and sub-sub directories, or a system wide search for a file, an arbitrary node
such as a top-level directory is chosen and explored to its depths (all the sub-directories and
sub-sub directories there in) before returning to the top-level directories to pick another
node (top-level directory) and repeat same.

Illustratively:

Given a filesystem with directories A, B, C each having multi-level sub directories.
Randomly pick a starting point eg. point A, search through the system, if object found is a file
and filename is equal to the file been searched for, return the file, else if object found is a directory,
and object has sub-directories, pick a random start point eg. point Aa, search through its sub-directories.

If object is the last on the current directory (sub-directory Aa) and the directory (sub-directory Aa) is the
last in the sub-directories under A, and file not found, add Aa to the searched_sub_list array (This is
necessary to avoid repetition) then return to directory's (A) top-level directories. At this point, look
through searched_sub_list array and randomly pick another node not already in the searched_sub_list
array eg. point Ab repeat process as with point Aa until file is found.

If object is the last on the current directory(A)  and directory(An) is the last in the sub-directories under A,
and file not found, add A to the searched_list array (This is necessary to avoid repetition) then return to
system's top-level directories. At this point, look through searched_list array and randomly pick another
node not already in the searched_list array eg. point C repeat process as with point A until file is found.

This guarantees an exhaustive search through the entire file system and ensures each directory is searched
just once.
'''



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


def lcm(values):
	values = set([abs(int(v)) for v in values])
	if values and 0 not in values:
		n = n0 = max(values)
		values.remove(n)
		while any( n % m for m in values ):
			n += n0
		return n
	return 0















