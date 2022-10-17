import streamlit as st


if 'num' not in st.session_state:
    st.session_state.num = 0


choices1 = ['no answer', 'manila', 'tokyo', 'bangkok']
choices2 = ['no answer', 'thailand', 'japan', 'philippines']

qs1 = [('What is the capital of Japan', choices1),
    ('What is the capital of Philippines', choices1),
    ('What is the capital of Thailand', choices1)]
qs2 = [('What country has the highest life expectancy?', choices2),
    ('What country has the highest population?', choices2),
    ('What country has the highest oil deposits?', choices2)]


def main():
    for _, _ in zip(qs1, qs2): 
        placeholder = st.empty()
        num = st.session_state.num
        with placeholder.form(key=str(num)):
            st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
            st.radio(qs2[num][0], key=num+1, options=qs2[num][1])          
                      
            if st.form_submit_button():
                st.session_state.num += 1
                if st.session_state.num >= 3:
                    st.session_state.num = 0 
                placeholder.empty()
            else:
                st.stop()


main()
