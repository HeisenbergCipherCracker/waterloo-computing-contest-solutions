"""
Troy is planning to take a group photo of the students at CCO and has asked you for help.
There are K students, numbered from 1 to K. Troy has forgotten the students’ heights, but
remembers that no two students have the same height.
Troy has prepared a sequence A1, A2, . . . , AN representing the order of students in the group
photo, from left to right. It is possible for a student to appear multiple times in A. You
aren’t sure how this group photo would be taken, but you’re unwilling to assume that Troy
made a mistake.
Troy will ask you Q queries of the form x y, which is a compact way of asking “Given
the sequence of students Ax, Ax+1, . . . , Ay, can their heights form an alternating sequence?”
More precisely, we denote the height of the ith student as h[i]. If there exists an assignment
of heights h[1], h[2], . . . , h[K] such that h[Ax] > h[Ax+1] < h[Ax+2] > h[Ax+3] < . . . h[Ay],
answer YES; otherwise answer NO.
Note that each of the Q queries will be independent: that is, the assignment of heights for
query i is independent of the assignment of heights for query j so long as i 6= j.
"""


"""

Author: Seyed Ali Mirmohammad
"""


def calculate_heights(K=[5, 3, 8, 2, 6, 1, 7, 4]):
    #! Let k represent the students number (from range 1 to K)
    #! Let Order be the students sort as an array(sort from left to right)
    #! Let h[i] be the height of the student
    def sort_student_list(arr=K):
        """
        This is a function to preprocess the students using bubble sort algorithm
        O(n^2)
        """
        nonlocal K
        n = len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        
        return arr
    
    seq = sort_student_list()
    def is_form_alternative_sequence(x,y,form=seq):
        nonlocal seq
        n = len(form)
        """h[Ax] > h[Ax+1] < h[Ax+2] > h[Ax+3] < . . . h[Ay]"""
        #!Lets go with the above example:
        if x > 1 or y>n or x >= y:
            return False
        
        #! We need a set of numbers to generate unique array
        unique_arr = set()
        for i in range(x-1,y):
            if form[i] in unique_arr:
                return False
            
            unique_arr.add(form[i])
        
        for i in range(x-1,y-2):
            if (form[i] > form[i+1]< form[i+2]) or (form[i] < form[i+1] > form[i+2]):
                continue
            else:
                return False
            
        
        return False
    queries = [(2, 5), (1, 4), (3, 7)]

    for query in queries:
        result= is_form_alternative_sequence(x=query[0],y= query[1])
        if result:
            print("YES")
        else:
            print("no!")


if __name__ == "__main__":
    calculate_heights()
