import streamlit as st

st.title("🧬 DNA Sequence Analyzer")
st.write("A simple bioinformatics tool built with Python.")

# Get DNA sequence from user
dna = st.text_input("Enter your DNA sequence:")
dna = dna.upper()

# Analyze button
if st.button("Analyze DNA"):

    # Check whether DNA is valid
    valid = len(dna) > 0

    for base in dna:
        if base not in "ATGC":
            valid = False

    if valid:
        # Count nucleotides
        a = dna.count("A")
        t = dna.count("T")
        g = dna.count("G")
        c = dna.count("C")

        # Calculate sequence length
        length = len(dna)

        # Calculate GC percentage
        gc = ((g + c) / length) * 100

        # Display results
        st.subheader("DNA Analysis Results")
        st.write("Sequence:", dna)
        st.write("Length:", length)
        st.write("Adenine (A):", a)
        st.write("Thymine (T):", t)
        st.write("Guanine (G):", g)
        st.write("Cytosine (C):", c)
        st.write("GC Percentage:", round(gc, 2), "%")

    else:
        st.error("Invalid DNA sequence! Enter only A, T, G, C.")
