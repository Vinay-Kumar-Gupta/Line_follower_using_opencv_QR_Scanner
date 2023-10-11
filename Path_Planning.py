def LSRB():
    land_marks = {"A":[0,2],"B":[3,5],"C":[6,8],"H":[16,18],"G":[19,20],"F":[22,24],"E":[26,28],"D":[29,31]}
    rules = ["LBL","LBS","LBR","SBL","SBS","SBR","RBL","RBS","RBR"]
    values = ["S","R","B","R","B","L","B","L","S"]
    
    def_path = "LBLLBLLBLRRLSSSBLBLLBLLBLLLBLLBL"

    while 1:
        start = input("Enter Start : ")
        stop = input("Enter Stop : ")

        start = land_marks[start][1]
        stop = land_marks[stop][0]+1
        short_path = def_path[start:stop]
        path = short_path
        while "B" in path:
            count=0
            for i in rules:
                if i in path:
                    path = path.replace(i,values[count])
                count+=1
        while "B" not in path:
            print(path)
            break
    # return path
                
# input_path = input("Enter Your path : ")
LSRB()
