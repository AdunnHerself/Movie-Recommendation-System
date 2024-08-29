import pickle as pkl
import streamlit as st
import lzma

# Set a custom title and layout
st.set_page_config(page_title="Movie Recommendation System", layout="centered")

# Load the datasets
movie_dataset = pkl.load(open('movies_dataset.pkl', 'rb'))

#Load model

# Function to load and decompress the model
def load_compressed_model(filepath):
    with lzma.open(filepath, 'rb') as compressed_file:
        model = pkl.load(compressed_file)
    return model

# Path to your compressed model file
compressed_model_path = 'similarity.pkl.xz'

# Load the model
similarity = load_compressed_model(compressed_model_path)
#similarity = pkl.load(open('similarity.pkl', 'rb'))

# Sidebar for page selection
page = st.sidebar.selectbox("Select a Page", ["Home", "Recommendation"])

if page == "Home":
    st.markdown("""
    <style>
    .main-title {
        font-size: 28px; /* Slightly reduced size */
        
        font-family: 'Arial', sans-serif;
        
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 20px; /* Adjusted size */
        
        font-family: 'Arial', sans-serif;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    .text {
        font-size: 16px;
        
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .example {
        font-size: 18px;
        
        font-family: 'Arial', sans-serif;
    }
    .contact {
        font-size: 16px;
        
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
    }
    .disclaimer {
        font-size: 16px;
        
        font-family: 'Arial', sans-serif;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-title'>🎬 Welcome to the Movie Recommendation System 🍿</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Introduction</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>Welcome to the Movie Recommendation System! This web application helps you find movies or TV shows similar to the one you select. By selecting a movie or TV show, this system provides you with personalized recommendations based on a similarity metric.</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>How It Works</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>The recommendation system employs a similarity metric to identify titles similar to your selection. It uses a Netflix dataset from Kaggle, leveraging features such as the director, cast, genres, and description of each title.</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Technologies Used</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'><ul><li><b>Streamlit</b>: For building the interactive web application.</li><li><b>Python</b>: The programming language used for data processing and recommendation metric.</li><li><b>Machine Learning</b>: Utilized for calculating similarities between different titles.</li></ul></div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Getting Started</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'><ol><li>Select a movie or TV show from the dropdown menu.</li><li>Click on the 'Recommend' button to receive suggestions.</li></ol></div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Example Recommendations</div>", unsafe_allow_html=True)
    st.markdown("<div class='example'><ul><li>If you love 'Inception', you might enjoy 'Interstellar'.</li><li>If you love 'Inception', you might enjoy 'The Prestige'.</li></ul></div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Contact Information</div>", unsafe_allow_html=True)
    st.markdown("<div class='contact'>For support or feedback, please reach out to <a href='mailto:lasisiromoke4@gamil.com'>lasisiromoke4@gamil.com</a>.</div>", unsafe_allow_html=True)

    st.markdown("<div class='subheader'>Disclaimer</div>", unsafe_allow_html=True)
    st.markdown("<div class='disclaimer'>The recommendations are based on the data available and the similarity metric used.</div>", unsafe_allow_html=True)

    st.markdown("<div class='text'>To get started, use the sidebar menu to navigate to the 'Recommendation' page.</div>", unsafe_allow_html=True)

elif page == "Recommendation":
    # Add a header with a custom style
    st.markdown(
        """
        <style>
        .main-header {
            font-size:40px;
             
            font-family: 'Arial', sans-serif;
            
            margin-bottom: 20px;
        }
        .recommendation {
            font-size:18px;
            
            font-family: 'Arial', sans-serif;
            margin-bottom: 10px;
        }
        .poster {
            display: block;
            margin-left: auto;
            margin-right: auto;
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Add the movie poster at the top
    st.markdown("<div class='main-header'>🎬 Movie Recommendation System 🍿</div>", unsafe_allow_html=True)

    st.image("movie_poster.png", caption="", use_column_width=True)


    def recommend_movie(movie_name): 
        movie_index = movie_dataset[movie_dataset['title'] == movie_name].index[0]
        similar_movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda vector: vector[1])

        recommendations = []

        for i in similar_movies[1:6]:  # Skip the first movie (itself)
            recommendations.append(f"If you love '{movie_name}', you might enjoy '{movie_dataset.iloc[i[0]].title}'.")
        
        return recommendations

    # Single-column layout
    selected_movie = st.selectbox('Select a Movie/TV Show:', movie_dataset['title'])

    if st.button('Recommend'):
        result = recommend_movie(selected_movie)
        st.markdown("<h3 style=''>Recommended Movies/TV Shows:</h3>", unsafe_allow_html=True)
        for recommendation in result:
            st.markdown(f"<div class='recommendation'>{recommendation}</div>", unsafe_allow_html=True)

    # Add a footer
    st.markdown(
        """
        <hr>
        <div style='text-align:center;'>
            <p style='font-family:Verdana; color:#555555;'>Developed by Adun</p>
        </div>
        """, unsafe_allow_html=True
    )
