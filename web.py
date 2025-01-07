import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions.write_todos(todos)

st.title("My Todo App")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="new_todo", label_visibility='hidden', placeholder="Add a new Todo...",
              on_change=add_todo, key="new_todo")
