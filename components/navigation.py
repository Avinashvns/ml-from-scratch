import streamlit as st

from pages.home import show_home

# =====================================================
# NAVIGATION FUNCTION
# =====================================================

def run_navigation():

    with st.sidebar:

        main_page = st.radio(
            "🚀 Avinash ML Hub",
            [
                "🏠 Home",
                "🔥 Scratch ML",
                "🤖 Scikit Learn"
            ]
        )

        sub_page = None

        # =================================================
        # SCRATCH SUB MENU
        # =================================================

        if main_page == "🔥 Scratch ML":

            # st.markdown("### Algorithms")

            sub_page = st.radio(
                "Algorithms",
                [
                    "Linear Regression",
                    "KNN",
                    "K-Means",
                    "Logistic Regression"
                ]
            )

        # =================================================
        # SCIKIT SUB MENU
        # =================================================

        elif main_page == "🤖 Scikit Learn":

            st.markdown("### Algorithms")

            sub_page = st.radio(
                "Choose Algorithm",
                [
                    "Linear Regression",
                    "KNN"
                ]
            )

    # =====================================================
    # HOME PAGE
    # =====================================================

    if main_page == "🏠 Home":

        show_home()

    # =====================================================
    # SCRATCH ML
    # =====================================================

    elif main_page == "🔥 Scratch ML":

        # =============================================
        # LINEAR REGRESSION
        # =============================================

        if sub_page == "Linear Regression":

            st.title("📈 Linear Regression")

            st.latex(r"y = mx + c")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    Linear Regression
                </div>

                <div class="card-text">
                    Predict values using a straight line equation.
                </div>

            </div>
            """, unsafe_allow_html=True)

        # =============================================
        # KNN
        # =============================================

        elif sub_page == "KNN":

            st.title("📍 KNN")

            st.latex(r"d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    KNN Algorithm
                </div>

                <div class="card-text">
                    Classification using nearest neighbors.
                </div>

            </div>
            """, unsafe_allow_html=True)

        # =============================================
        # K-MEANS
        # =============================================

        elif sub_page == "K-Means":

            st.title("🎯 K-Means")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    K-Means Clustering
                </div>

                <div class="card-text">
                    Group data points into clusters.
                </div>

            </div>
            """, unsafe_allow_html=True)

        # =============================================
        # LOGISTIC REGRESSION
        # =============================================

        elif sub_page == "Logistic Regression":

            st.title("📊 Logistic Regression")

            st.latex(r"\sigma(z)=\frac{1}{1+e^{-z}}")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    Logistic Regression
                </div>

                <div class="card-text">
                    Binary classification using sigmoid function.
                </div>

            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # SCIKIT LEARN
    # =====================================================

    elif main_page == "🤖 Scikit Learn":

        if sub_page == "Linear Regression":

            st.title("🤖 Sklearn Linear Regression")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    Scikit Learn Linear Regression
                </div>

                <div class="card-text">
                    Machine learning using Scikit-Learn library.
                </div>

            </div>
            """, unsafe_allow_html=True)

        elif sub_page == "KNN":

            st.title("🤖 Sklearn KNN")

            st.markdown("""
            <div class="card">

                <div class="card-title">
                    Scikit Learn KNN
                </div>

                <div class="card-text">
                    Classification using Scikit-Learn KNN.
                </div>

            </div>
            """, unsafe_allow_html=True)