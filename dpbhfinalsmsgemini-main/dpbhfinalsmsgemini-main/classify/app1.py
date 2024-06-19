import streamlit as st
from geminiai import DarkPatternClassifier, extract_arrays_from_input_string

def main():
    st.title(' Classify the dark pattern')

    website = st.text_input('Enter Website URL:')
    defects = st.text_area('Enter Defects/Content (in JSON format):', '[ "defect1", "defect2", ... ]')
    
    if st.button('Classify Dark Pattern'):

        classifier = DarkPatternClassifier()
        result = classifier.classify_dark_pattern(defects, website)

        st.subheader('Result:')
        st.write(result)
        content,dark_patterns = extract_arrays_from_input_string(result)

    else:
        st.error('Input details')

if __name__ == '__main__':
    main()
