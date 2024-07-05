import random
class tictactoe():
    def __init__(self) -> None:
        self.d=[]
        self.blk1=[[" ","|"," ","|"," "],[" ","|"," ","|"," "],[" ","|"," ","|"," "]]
        self.indx={1:[0,0],2:[0,2],3:[0,4],4:[1,0],5:[1,2],6:[1,4],7:[2,0],8:[2,2],9:[2,4]}
        self.c=[0,2,4]
        self.r=[0,1,2]
    
    # function to dispaly the board.
    def disp(self,blk1):
        for i in range(0,3):
            for j in range(0,5):
                print(self.blk1[i][j]," ",end="")
            if i!=2:
                print("\n---- ---- ----")

    #function to check any 3 consecutive blocks are occupied by same symbol
    def check(self,sym,blk1)->bool:
        if blk1[0][0] == blk1[0][2] == blk1[0][4] ==sym:
            return True
        elif blk1[1][0] == blk1[1][2] == blk1[1][4]==sym:
            return True
        elif blk1[2][0] == blk1[2][2] == blk1[2][4] ==sym:
            return True
        
        if blk1[0][0] == blk1[1][2] == blk1[2][4] ==sym:
            return True
        elif blk1[0][4] == blk1[1][2] == blk1[2][0] ==sym:
            return True
        
        if blk1[0][0] == blk1[1][0] == blk1[2][0] ==sym:
            return True
        elif blk1[0][2] == blk1[1][2] == blk1[2][2] ==sym:
            return True
        elif blk1[0][4] == blk1[1][4] == blk1[2][4] ==sym:
            return True
        


    #function to choose computers move.
    def comp(self,blk,d,indx)->int:
        
        eLi=[1,2,3,4,5,6,7,8,9]
        ele=random.choice(eLi)
        if ele in d:
            self.comp(blk,d,indx)
        else:
            d.append(ele)
            print("\nThe computer chooses:",ele)
            dim=self.indx.get(ele)
            rw=dim[0]
            co=dim[1]
            self.blk1[rw][co]="X"
            
    # function for the users move    
    def user(self,blk,d,indx):
        f=True
        while f:
            ch=int(input("\nEnter your choice:"))
            eLi=[1,2,3,4,5,6,7,8,9]
            if ch not in eLi:
                print("\nInvalid choice.")
            else:
                f=False
            
        if ch in d:
            print("\nAlready chosen")
            self.user(blk,d,indx)
        else:
            d.append(ch)
            dim=self.indx.get(ch)
            rw=dim[0]
            co=dim[1]
            self.blk1[rw][co]="O"
    
#main
print("----------------Tic Tac Toe game---------------")
flag=1
while(flag==1):
    flag =int(input("Press 1 to start.\n0 to quit.\n"))
    if flag==1:
        c=tictactoe() 
        print("\nLets start!!!")
        print(" 1 | 2 | 3 \n--- --- ---\n 4 | 5 | 6 \n--- --- ---\n 7 | 8 | 9 ")
        i=True
        count=0
        while i:
            count=count+2
            if count>8:
                c.comp(c.blk1,c.d,c.indx)
                c.disp(c.blk1)
                ckc=c.check("X",c.blk1)
                if ckc==True:
                    print("\nYou Lose!")
                    break
                print("\nTie")
                break
            c.comp(c.blk1,c.d,c.indx)
            c.disp(c.blk1)
            ckc=c.check("X",c.blk1)
            if ckc==True:
                print("\nYou Lose!")
                break
           
            c.user(c.blk1,c.d,c.indx)
            c.disp(c.blk1)
            ckc=c.check("O",c.blk1)
            if ckc==True:
                print("\nCongratulations!!!")
                break
            
    elif flag==0:
        print("Thank you for playing. :)") 
    else:
        flag=1
        print("\nInvalid Choice.")
              