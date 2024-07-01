import random
import streamlit as st 
def generate_num() -> int:
    num=random.randint(0,101)
    return num

def guess_num(num) -> int:
        count=0
        while True:
            guess=st.text_input("Enter your guess:")
            if st.button("OK"):
                if guess.isdigit():
                    guess=int(guess)
                    if guess<=100 and guess>=0:
                        if guess==num:
                            st.success("Congratulations!! Your Answer is correct!")
                            count+=1
                            break
                        elif guess>num:
                            st.error("Oops!! Wrong Answer!")
                            st.error("Try a smaller value.")
                            count+=1
                        elif guess<num:
                            st.error("Oops!! Wrong Answer!")
                            st.error("Try a greater value.")
                            count+=1
                    else:
                        st.error("Please enter a number in range 0 to 100") 
                else:
                    st.error("Please enter a number.")
        return count
                
def main():
    num=generate_num()
    if num>=0:
        count=guess_num(num)
    st.success("Number of tries:",count)
main()