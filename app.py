import streamlit as st
import pandas as pd
import requests
from annotator import annotate_variant, read_vcf
import tempfile


def run_annotation(selected_rsid=None):
    if st.button("🔍 Annotate Variant"):
        with st.spinner(f"Querying Ensembl VEP for {selected_rsid}..."):
            result = annotate_variant(selected_rsid)

        if result:
            st.success("✅ Annotation Retrieved Successfully!")
            st.subheader("📋 Annotation Summary")

            # Handle response if it's a list
            if isinstance(result, list) and result:
                annotation = result[0]
            else:
                annotation = result

                    

            # Display relevant keys
            keys_to_display = [
                'id', 'assembly_name', 'most_severe_consequence',
                'transcript_consequences', 'colocated_variants'
            ]
            print(annotation.keys())
            print(annotation["strand"])
            for key in keys_to_display:
                if key in annotation:
                    st.markdown(f"### 🔹 {key.replace('_', ' ').title()}")
                    st.write(annotation[key])
            st.markdown("### 🔹 SUMMARY")
            st.write("this is a sumamry")
        else:
            st.error("❌ Failed to retrieve annotation from Ensembl.")




st.set_page_config(page_title="Variant Annotation Tool", layout="wide")
st.title("🧬 Variant Annotation (VEP - Ensembl)")

st.markdown("""
Upload a file with variant RSIDs (e.g., from dbSNP or 1000 Genomes), select a row, and get functional annotations using Ensembl's VEP API.
""")

# --- File Upload ---
uploaded_file = st.file_uploader("📁 Upload your VCF file", type=["vcf"])
rsid = st.text_input(placeholder="e.g rs11577344", label="enter your rsid (optional):")




if uploaded_file:
    # Read VCF using your generator function
    with tempfile.NamedTemporaryFile(delete=False, suffix=".vcf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    records = list(read_vcf(tmp_path))
    df = pd.DataFrame(records)

    if df.empty:
        st.warning("⚠️ No data found in the VCF file.")
    else:
        # Automatically use 'ID' column (VCF rsIDs)
        rsid_column = "ID"
        st.write("✅ Detected RSID column: `ID`")

        # Row selection dropdown
        row_index = st.selectbox(
            "🔢 Select Row to Annotate",
            options=df.index,
            format_func=lambda i: f"Row {i} - {df.at[i, rsid_column]}"
        )

        selected_rsid = str(df.at[row_index, rsid_column])

        if not selected_rsid or selected_rsid == ".":
            st.error("❌ No RSID found in the selected row.")
        else:
            # Annotate Button
            run_annotation(st, selected_rsid)
elif rsid:
    run_annotation(rsid)
else:
    st.info("📌 Please upload a `.vcf` file to begin.")
