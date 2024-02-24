import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Set page config to wide mode
st.set_page_config(layout="wide")

def lissajous(t, A, B, a, b, delta):
    x = A * np.sin(a * t)
    y = B * np.sin(b * t + delta)
    return x, y
col1, col2 = st.columns(2)

st.title(LISSAJOUS FIGURE)

def draw_lissajous(A, B, a, b, delta):

    with col1:

        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = lissajous(t, A, B, a, b, delta)
        plt.figure(figsize=(10, 10))
        plt.plot(x, y, 'b-', linewidth=2)  # Increase line width
        plt.xlabel('X', fontsize=30)  # Increase font size
        plt.ylabel('Y', fontsize=30)  # Increase font size
        plt.title('Lissajous Figure', fontsize=30, fontweight='bold')  # Increase font size and make title bold
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')  # Add gridlines with specific style
        plt.xticks(fontsize=20)  # Increase font size of tick labels on x-axis
        plt.yticks(fontsize=20)  # Increase font size of tick labels on y-axis
        plt.tight_layout()  # Adjust layout for better spacing
        st.pyplot()

    with col2:

        plt.figure(figsize=(4, 2))
        plt.plot(t, x, 'r-', linewidth=2)
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('X Wave Intensity', fontsize=8)
        plt.title('X Wave Intensity', fontsize=8, fontweight='bold')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.tight_layout()
        st.pyplot()
        plt.figure(figsize=(4, 2))
        plt.plot(t, y, 'b-', linewidth=2)
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Y Wave Intensity', fontsize=8)
        plt.title('Y Wave Intensity', fontsize=8, fontweight='bold')
        plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
        plt.tight_layout()
        st.pyplot()
def main():

    st.markdown("---")
    st.sidebar.write("## Enter Parameters:")
    A = st.sidebar.number_input("AMPLITUDE OF X WAVE", min_value=50, value=200)
    B = st.sidebar.number_input("AMPLITUDE OF Y WAVE", min_value=50, value=300)
    a = st.sidebar.number_input("FREQUENCY OF X WAVE", min_value=1, max_value=200, value=3)
    b = st.sidebar.number_input("FREQUENCY OF Y WAVE", min_value=1, max_value=200, value=4)
    delta = st.sidebar.number_input("PHASE DIFFERENCE", min_value=0.0, max_value=2*np.pi, value=np.pi/2)
    st.markdown("---")
    draw_lissajous(A, B, a, b, delta)
st.set_option('deprecation.showPyplotGlobalUse', False)
if __name__ == "__main__":
    main()
