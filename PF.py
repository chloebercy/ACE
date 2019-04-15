

def GPA_points(grade):
    GPA_SUM = 0 
    
    A_Grade = ["A", "a"] 
    B_Grade = ["B", "b"] 
    C_Grade = ["C", "c"] 
    D_Grade = ["D", "d"] 
    
    if grade in A_Grade:
        GPA_SUM = GPA_SUM + 4.0
    elif grade in B_Grade:
        GPA_SUM = GPA_SUM + 3.0
    elif grade in C_Grade:
        GPA_SUM = GPA_SUM + 2.0
    elif grade in D_Grade:
        GPA_SUM = GPA_SUM + 1.0

    return GPA_SUM

def GPA(class1grade, class2grade, class3grade, class4grade, class5grade, class6grade, numweights):
    GPA_T = 0
    GPA_T= GPA_T + GPA_points(class1grade)
    GPA_T= GPA_T + GPA_points(class2grade)
    GPA_T= GPA_T + GPA_points(class3grade)
    GPA_T= GPA_T + GPA_points(class4grade)
    GPA_T= GPA_T + GPA_points(class5grade)
    GPA_T= GPA_T + GPA_points(class6grade)
    GPA_T= GPA_T + numweights
    GPA_T = GPA_T / 6
    return GPA_T
    
print GPA("A", "A", "A", "A", "B", "A", 3)