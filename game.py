### Used for defining functions

from qiskit import *
import numpy as np
import streamlit as st
from sympy import false


def quantum_superposition():
    
    circuit = QuantumCircuit(1,1)

    circuit.h(0) #applying Hadamard gate

    circuit.measure(0,0)

    simulator = Aer.get_backend('aer_simulator')

    result = simulator.run(circuit).result().get_counts()

    return result

def get_random_value():
    res = quantum_superposition()
    # print(res)

    values = list(res.values())
    keys = list(res.keys())
    # print(values)
    # print(keys)
    random_value = '|' +str(keys[np.argmax(values)]) + '>'
    # print(random_value)
    return random_value

def validate(arr):
    """
    This method checks if the game is finished!
    Parameters: arr(numpy array): The array that serves as board
    Returns: returns 0 if any of the following condition is satisfied by any of the player else
    return 1
    """

    flag = True
    ket_zero = '|0>'
    ket_one = '|1>'

    if arr[0,0]==ket_one and arr[1,1]==ket_one and arr[2,2]==ket_one:
        st.success('User has won!')
        flag = false

    elif arr[0,0]==ket_zero and arr[1,1]==ket_zero and arr[2,2]==ket_zero:
        st.success('Computer has won!')
        flag = false

    elif arr[0,2]==ket_one and arr[1,1]==ket_one and arr[2,0]==ket_one:
        st.success('User has won!')
        flag = false
    
    elif arr[0,2]==ket_zero and arr[1,1]==ket_zero and arr[2,0]==ket_zero:
        st.success('Computer has won!')
        flag = false
    
    if flag:
        
        for index in [0,1,2]:
            if(list(arr[index])==[ket_zero, ket_zero, ket_zero]):
                st.success('User has won')
                return 0
        for index in [0,1,2]:
            if(list(arr[index])==[ket_one, ket_one, ket_one]):
                st.success('Computer has won')
                return 0   
        for index in [0,1,2]:
            if(list(arr[:,index])==[ket_one, ket_one, ket_one]):
                st.success('User has won')
                return 0
        for index in [0,1,2]:
            if(list(arr[:,index])==[ket_zero, ket_zero, ket_zero]):
                st.success('Computer has won')
                return 0

        if '|Ψ>' not in arr:
            st.write("It's a draw!")
            return 0
    return 1