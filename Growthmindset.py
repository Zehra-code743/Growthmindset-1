
import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import os
import plotly.express as px # type: ignore


# Page Configuration
st.set_page_config(page_title="Data Sweeper - Sterling Integrator", layout='wide', page_icon="🧹")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Select Page", ["Home", "Upload & Process", "About"])

# Footer
footer = "<p style='text-align: center; color: white;'>Created by Shan-E-Zehra © 2025</p>"

if page == "Home":
    st.markdown("<h1 style='text-align: center; color: #F4D03F;'>🧹 Data Sweeper - Sterling Integrator</h1>", unsafe_allow_html=True)
    st.write("Effortlessly clean, transform, and visualize your CSV and Excel files with an intuitive interface.")
    
    # Fix Image Loading Issue
    st.image("https://images.unsplash.com/photo-1593642532973-d31b6557fa68", use_container_width=True)
    st.markdown("---")
    
    st.subheader("🚀 Key Features:")
    features = [
        "📂 Upload multiple CSV/Excel files",
        "🧹 Automatic data cleaning & outlier detection",
        "📊 Interactive visualizations (Bar, Line, Pie, Heatmaps)",
        "🎯 Advanced column filtering & transformations",
        "📥 Export cleaned datasets with a single click",
        "🌙 Modern UI with dark mode support"
    ]
    
    for feature in features:
        st.markdown(f"✅ {feature}")
    
    st.markdown("---")
    st.markdown(footer, unsafe_allow_html=True)

elif page == "Upload & Process":
    st.title("📂 Upload and Process Your Files")
    uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()
            df = pd.read_csv(file) if file_ext == ".csv" else pd.read_excel(file)
            
            st.write(f"### Preview of {file.name}")
            st.dataframe(df.head())

            # Data Cleaning Options
            st.subheader(f"🧹 Data Cleaning for {file.name}")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button(f"Remove Duplicates ({file.name})", key=f"dup_{file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed!")

            with col2:
                if st.button(f"Fill Missing Values ({file.name})", key=f"fill_{file.name}"):
                    df.fillna(df.mean(numeric_only=True), inplace=True)
                    st.success("Missing values filled!")

            with col3:
                if st.button(f"Detect Outliers ({file.name})", key=f"outlier_{file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                    if numeric_cols:
                        outliers = df[numeric_cols].apply(lambda x: x[(x - x.mean()).abs() > 3 * x.std()])
                        st.write("Outlier Summary:")
                        st.dataframe(outliers.dropna(how='all'))
                    else:
                        st.warning("No numeric columns for outlier detection.")
            
            # Column Selection
            selected_cols = st.multiselect(f"Select Columns to Keep for {file.name}", df.columns, default=df.columns)
            df = df[selected_cols]

            # **Automatic Bar Chart Display**
            st.subheader(f"📊 Auto Bar Chart for {file.name}")
            auto_chart = st.checkbox(f"Enable Bar Chart for {file.name}", key=f"chart_{file.name}")

            if auto_chart:
                if df.empty:
                    st.warning("The dataset is empty. Please upload a valid file.")
                else:
                    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
                    categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()

                    if numeric_cols and categorical_cols:
                        x_col = st.selectbox(f"Select X-Axis (Categorical) for {file.name}", categorical_cols, key=f"x_col_{file.name}")
                        y_col = st.selectbox(f"Select Y-Axis (Numeric) for {file.name}", numeric_cols, key=f"y_col_{file.name}")

                        if x_col and y_col:
                            try:
                                fig = px.bar(df, x=x_col, y=y_col, color=x_col, title=f"Bar Chart for {file.name}",
                                             height=500, color_discrete_sequence=px.colors.qualitative.Bold)
                                st.plotly_chart(fig)
                            except Exception as e:
                                st.error(f"Error generating bar chart: {e}")
                        else:
                            st.warning("Please select valid columns for visualization.")
                    else:
                        st.warning("⚠️ Your dataset must have at least one categorical column (e.g., text) and one numeric column (e.g., numbers) to generate a bar chart.")
    
    st.markdown(footer, unsafe_allow_html=True)

elif page == "About":
    st.title("ℹ️ About Data Sweeper")
    st.write("Data Sweeper is an advanced data cleaning and visualization tool, designed to help professionals and researchers efficiently process large datasets with minimal effort.")
    st.write("🎯 Our goal is to provide a user-friendly interface that streamlines data exploration and analysis, making it easier for you to focus on your core tasks and insights.")
    

    # Fix Image Loading Issue
    st.image("https://static.vecteezy.com/system/resources/previews/000/522/943/original/abstract-technology-background-with-the-hi-tech-futuristic-concept-cyber-technology-innovation-background-vector-illustration.jpg", use_container_width=True)
    st.markdown("---")
    st.markdown(footer, unsafe_allow_html=True)
    st.write(" ❤️    CopyRight @2025 Reserved This Website is Created By Shan e Zehra   ❤️ ")






















