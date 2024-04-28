if __name__ == '__main__':
    s = input()
    al=False
    aln=False
    dig=False
    l=False
    u=False
    for i in range(len(s)):
        if(s[i].isalpha()):
            al=True
        if(s[i].isalnum()):
            aln=True
        if(s[i].isdigit()):
            dig=True
        if(s[i].isupper()):
            u=True
        if(s[i].islower()):
            l=True
                    
print(al,"\n",aln,"\n",dig,"\n",l,"\n",u,sep="")