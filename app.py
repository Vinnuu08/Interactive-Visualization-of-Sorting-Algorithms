
import streamlit as st
import time
import random

st.set_page_config(
    page_title="Sorting Algorithm Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Visualization of Sorting Algorithms")
st.write("Learn sorting algorithms through animation!")

if "numbers" not in st.session_state:
    st.session_state.numbers = random.sample(range(5, 100), 10)

algorithm = st.selectbox(
    "Select Sorting Algorithm",
    ["Bubble Sort", "Selection Sort", "Insertion Sort"]
)

speed = st.slider("Animation Speed", 0.1, 1.0, 0.5)

if st.button("Generate New Numbers"):
    st.session_state.numbers = random.sample(range(5, 100), 10)

def bubble_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr.copy()

def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr.copy()

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        yield arr.copy()

def display_bars(arr):
    chart_data = {
        "Index": list(range(len(arr))),
        "Value": arr
    }
    st.bar_chart(chart_data, x="Index", y="Value")

st.subheader("Original Numbers")
display_bars(st.session_state.numbers)

if st.button("Start Sorting"):
    arr = st.session_state.numbers.copy()

    if algorithm == "Bubble Sort":
        steps = bubble_sort(arr)
        complexity = "O(n²)"
    elif algorithm == "Selection Sort":
        steps = selection_sort(arr)
        complexity = "O(n²)"
    else:
        steps = insertion_sort(arr)
        complexity = "O(n²)"

    st.subheader("Sorting Animation")
    chart = st.empty()

    for step in steps:
        with chart.container():
            display_bars(step)
        time.sleep(speed)

    st.success("Sorting Completed Successfully!")

    st.write("Time Complexity:", complexity)
    st.write("Selected Algorithm:", algorithm)

st.info("Choose an algorithm and click Start Sorting.")
