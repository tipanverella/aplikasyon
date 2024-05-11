"""
	Hello world Streamlit app
"""

from datetime import date
import streamlit as st


def main():
    """bring it all together"""
    st.title("Bonjou!")
    st.write(f"Jodi a se: {date.today()}")
    name = st.text_input("Kouman ou rele?")
    if name:
        st.markdown(f"### Bonjou, {name}")
        st.latex(
            r"""a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) """
        )


if __name__ == "__main__":
    main()
