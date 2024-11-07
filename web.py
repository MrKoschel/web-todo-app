import streamlit as st
import functions

todos = functions.open_todos_file()


def add_todo():
    todo = st.session_state["add"]
    todos.append(todo + "\n")
    functions.override_todos_file(todos)


st.title("My TODO App")
for item in todos:
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos = functions.open_todos_file()
        todos.remove(item)
        functions.override_todos_file(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="", placeholder="Add TODO", on_change=add_todo, key="add")



