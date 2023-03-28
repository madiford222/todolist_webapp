import streamlit as st
from function_list import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My To Do App")
st.subheader("This is my to do list.")
st.subheader("egg?")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label = "Add a to-do", on_change = add_todo, 
              key = "new_todo")

# st.session_state