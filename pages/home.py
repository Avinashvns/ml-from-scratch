# import streamlit as st

# def show_home():

#     # =====================================================
#     # PAGE CONFIG
#     # =====================================================

#     st.set_page_config(
#         page_title="ML From Scratch",
#         page_icon="🚀",
#         layout="wide"
#     )

#     # =====================================================
#     # HERO SECTION
#     # =====================================================

#     st.markdown("""
#     <h1 style='text-align:center;
#                font-size:70px;
#                margin-bottom:0px;'>
#         🚀 ML From Scratch
#     </h1>
#     """, unsafe_allow_html=True)

#     st.markdown("""
#     <h3 style='text-align:center;
#                color:gray;
#                margin-top:0px;'>
#         Learn Machine Learning Through Mathematics,
#         Visualization and Pure Python Coding
#     </h3>
#     """, unsafe_allow_html=True)

#     st.write("")
#     st.write("")

#     # =====================================================
#     # HERO IMAGES
#     # =====================================================

#     col1, col2 = st.columns(2)

#     with col1:

#         st.image(
#             "https://images.unsplash.com/photo-1620712943543-bcc4688e7485",
#             use_container_width=True
#         )

#     with col2:

#         st.image(
#             "https://images.unsplash.com/photo-1677442135136-760c813028c0",
#             use_container_width=True
#         )

#     st.write("")
#     st.write("")

#     # =====================================================
#     # INTRO SECTION
#     # =====================================================

#     st.header("💡 What is this platform?")

#     st.write("""
#     ML From Scratch is an educational platform where you can deeply
#     understand Machine Learning algorithms instead of using them
#     like a black box.

#     This platform focuses on:

#     - Pure Python Implementations
#     - Mathematics Behind ML Algorithms
#     - Step-by-Step Logic Building
#     - Visual Understanding
#     - Real Intuition of Machine Learning
#     """)

#     st.write("")
#     st.write("")

#     # =====================================================
#     # WHAT YOU WILL LEARN
#     # =====================================================

#     st.header("📚 What You Will Learn")

#     col1, col2, col3 = st.columns(3)

#     with col1:

#         st.subheader("🧠 Logic")

#         st.write("""
#         Understand how algorithms work internally
#         step by step.
#         """)

#     with col2:

#         st.subheader("📐 Mathematics")

#         st.write("""
#         Learn formulas, intuition and mathematical
#         concepts behind Machine Learning.
#         """)

#     with col3:

#         st.subheader("📊 Visualization")

#         st.write("""
#         Visualize Machine Learning concepts using
#         graphs and interactive examples.
#         """)

#     st.write("")
#     st.write("")

#     # =====================================================
#     # AI IMAGE SECTION
#     # =====================================================

#     st.header("🤖 Artificial Intelligence")

#     st.image(
#         "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
#         use_container_width=True
#     )

#     st.write("")
#     st.write("")

#     # =====================================================
#     # ALGORITHMS SECTION
#     # =====================================================

#     st.header("🚀 Algorithms Included")

#     col1, col2 = st.columns(2)

#     with col1:

#         st.markdown("""
#         - 📈 Linear Regression  
#         - 🎯 KNN  
#         - 🧠 K-Means  
#         - 📊 Logistic Regression  
#         """)

#     with col2:

#         st.markdown("""
#         - 🌳 Decision Tree  
#         - 📚 Naive Bayes  
#         - ⚡ Perceptron  
#         """)

#     st.write("")
#     st.write("")

#     # =====================================================
#     # MISSION SECTION
#     # =====================================================

#     st.header("🎯 Mission")

#     st.write("""
#     The mission of this platform is to simplify
#     Machine Learning by teaching algorithms from
#     scratch using coding, mathematics and
#     visualization.
#     """)

#     st.write("")
#     st.write("")

#     # =====================================================
#     # GITHUB BUTTON
#     # =====================================================

#     st.link_button(
#         "💻 View GitHub Repository",
#         "https://github.com/Avinashvns/ml-from-scratch"
#     )

# Streamlit Home Page with Realistic ML Graphs


import streamlit as st



def show_home():

    # =====================================================
    # HERO SECTION
    # =====================================================

    st.markdown(
        """
        <h1 style='text-align:center; font-size:65px;'>
            🚀 ML From Scratch
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style='text-align:center; color:gray;'>
            Learn Machine Learning Through Mathematics,
            Visualization and Pure Python Coding
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # =====================================================
    # HERO IMAGE
    # =====================================================

    st.image(
        "https://images.unsplash.com/photo-1677442136019-21780ecad995",
        use_container_width=True,
        caption="Artificial Intelligence & Machine Learning"
    )

    st.write("")

    # =====================================================
    # AI / ML IMAGE SECTION
    # =====================================================

    # col1, col2 = st.columns(2)

    # with col1:

    #     st.image(
    #         "https://images.unsplash.com/photo-1620712943543-bcc4688e7485",
    #         use_container_width=True,
    #         caption="Machine Learning"
    #     )

    # with col2:

    #     st.image(
    #         "https://images.unsplash.com/photo-1677442135136-760c813028c0",
    #         use_container_width=True,
    #         caption="Artificial Intelligence"
    #     )

    # st.write("")

    # =====================================================
    # INTRO SECTION
    # =====================================================

    st.header("💡 What is this platform?")

    st.write("""
    ML From Scratch is an educational platform where you can deeply
    understand Machine Learning algorithms instead of using them
    like a black box.

    This project focuses on:

    - Pure Python Implementations
    - Mathematics Behind Algorithms
    - Visual Learning
    - Step-by-Step Logic
    - Real Intuition Building
    """)

    st.write("")
    st.write("")

    # =====================================================
    # LEARNING SECTION
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            "https://images.unsplash.com/photo-1620712943543-bcc4688e7485",
            use_container_width=True,
            caption="Machine Learning"
        )

    with col2:

        st.image(
            "https://images.unsplash.com/photo-1677442135136-760c813028c0",
            use_container_width=True,
            caption="Artificial Intelligence"
        )

    st.write("")

    st.header("📚 What You Will Learn")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("🧠 Logic")

        st.write("""
        Understand how Machine Learning algorithms
        work internally.
        """)

    with col2:

        st.subheader("📐 Mathematics")

        st.write("""
        Learn formulas, intuition and mathematical
        concepts deeply.
        """)

    with col3:

        st.subheader("📊 Visualization")

        st.write("""
        Visualize algorithms using graphs and
        interactive examples.
        """)

    st.write("")
    st.write("")

    # =====================================================
    # AI LEARNING SECTION
    # =====================================================

    st.header("🤖 AI & Machine Learning")

    st.image(
        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
        use_container_width=True,
        caption="Future of Artificial Intelligence"
    )

    st.write("")
    st.write("")

    # =====================================================
    # ALGORITHMS SECTION
    # =====================================================

    st.header("🚀 Algorithms Included")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        - 📈 Linear Regression
        - 🎯 KNN
        - 🧠 K-Means
        - 📊 Logistic Regression
        """)

    with col2:

        st.markdown("""
        - 🌳 Decision Tree
        - 📚 Naive Bayes
        - ⚡ Perceptron
        """)

    st.write("")
    st.write("")

    # =====================================================
    # MISSION
    # =====================================================

    st.header("🎯 Mission")

    st.write("""
    The mission of this platform is to simplify Machine Learning
    by teaching algorithms from scratch using coding,
    mathematics and visualization.
    """)

    st.write("")

    # =====================================================
    # GITHUB BUTTON
    # =====================================================

    st.link_button(
        "💻 View GitHub Repository",
        "https://github.com/Avinashvns/ml-from-scratch"
    )

