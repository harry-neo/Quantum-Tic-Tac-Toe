### Used for Streamlit layout and widgets
import math
from shutil import move
from requests import get
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from game import get_random_value, validate



def main():
    menu = ["Play","Instruction","About"]
    option = st.sidebar.selectbox("Menu",menu)

    if option=='Play':
        st.subheader('Quantum Playground!')
        st.write("Computer -> |0>")
        st.write("User -> |1>")
        psi = '|Ψ>'

        if 'board' not in st.session_state:
            st.session_state.board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
            st.session_state.available_moves=[0,1,2,3,4,5,6,7,8,9]
        
        moves = st.selectbox("Make your move", st.session_state.available_moves)
        #1
        if moves==1:
            if st.session_state.board[0,0]==psi:

                st.session_state.board[0,0] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        #2
        elif moves==2:
            if st.session_state.board[0,1]==psi:

                st.session_state.board[0,1] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #3
        elif moves==3:
            if st.session_state.board[0,2]==psi:

                st.session_state.board[0,2] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

        #4
        elif moves==4:
            if st.session_state.board[1,0]==psi:

                st.session_state.board[1,0] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #5
        elif moves==5:
            if st.session_state.board[1,1]==psi:

                st.session_state.board[1,1] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #6
        elif moves==6:
            if st.session_state.board[1,2]==psi:

                st.session_state.board[1,2] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #7
        elif moves==7:
            if st.session_state.board[2,0]==psi:

                st.session_state.board[2,0] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #8
        elif moves==8:
            if st.session_state.board[2,1]==psi:

                st.session_state.board[2,1] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)
        
        #9
        elif moves==9:
            if st.session_state.board[2,2]==psi:

                st.session_state.board[2,2] = get_random_value()

                user_flag = validate(st.session_state.board)

                if not user_flag:
                    st.dataframe(st.session_state.board)
                    st.session_state.available_moves = list()
                
                comp_square = np.random.randint(1,9)
                col = math.floor((comp_square-1)%3)
                row = math.floor((comp_square-1)/3)
                comp_value = get_random_value()

                if st.session_state.board[row,col] == psi:
                     st.session_state.board[row,col] = comp_value
                
                comp_flag = validate(st.session_state.board)

                if not comp_flag:
                    return 0
                
                st.write("Computer's Move:", comp_square)
                st.write("Computer's Value:", comp_value)
                st.dataframe(st.session_state.board)
            else:
                st.dataframe(st.session_state.board)

    elif option=='Instruction':
        st.subheader('Instructions')
        psi = '|Ψ>'
        board = np.array([[psi,psi,psi],[psi,psi,psi],[psi,psi,psi]])
        st.dataframe(board)
        instruction_1 = """
        The above board represents the initial state of the game.

        |Ψ> represents the superposition state!

        Always, the user is given the chance to make the first move.

        In classical Tic-Tac-Toe the user plays 0 and the computer plays 1. However, unlike its classical counterpart, in 
        Quantum tic-tac-toe there's no 100% probability that the 
        chosen move will result in state 1(|1>) or state 0(|0>).

        The squares in the 3x3 grid are numbered as follows
        """
        st.write(instruction_1)
        board_numbering = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
        st.write(board_numbering)

        instruction_2 = """
        The user can select any space from the 3x3 grid using the selection menu and press the 
        submit button.

        (Note: To go back, select a value from the menu!)
        """
        st.write(instruction_2)

    else:
        st.subheader("About")
        # Add Image
        img = Image.open('./IBM QC.jpeg')
        st.image(img)
        about = """
        Quantum Tic-Tac-Toe: A Hybrid of Quantum and Classical Computing.

        This version of Quantum Tic-Tac-Toe is made by modifying some rules and adding some different
        types of moves. Through this, we want to show that a game as simple as Tic-Tac-Toe could be
        made much more exciting and fun by involving quantum circuits. The players have an option to
        choose from two different types of moves. The classical move which measures the box and results
        in collapse and the quantum move which entangles two separate boxes and favours the player if the
        control box collapses in his favour. 

        Created using Python, Qiskit, Streamlit.

        References: 

        (1)https://www.researchgate.net/publication/338113536_Quantum_Tic-Tac-Toe_A_Hybrid_of_Quantum_and_Classical_Computing
        
        (2)Generalized Quantum Tic-Tac-Toe Ananya Kumar1, Ang Yan Sheng1, and Chai Ming Huang
        
        (3)Bloch Sphere - YouTube Channel

        """
        st.write(about)

if __name__=='__main__':
    condition = main()
    if condition==0:
        st.subheader('Game Over')