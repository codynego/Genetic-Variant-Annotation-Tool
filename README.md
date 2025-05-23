
# 🧬 Genetic Variant Annotation Tool

**Genetic Variant Annotation Tool** is a user-friendly application that helps scientists, clinicians, and developers interpret DNA mutations (genetic variants) by explaining what a change in a person’s DNA might mean — even if you don’t have a background in biology.

---

## 🚀 Features

* 🔍 Accepts raw genetic variant input (e.g. chromosome, position, reference and alternate base).
* 🧪 Queries database to annotate variants with:

  * Affected gene
  * Mutation impact on protein
  * Consequence type (e.g. missense, synonymous)
  * Protein and codon changes
* 🧠 Converts complex biological data into **easy-to-understand summaries**
* 📦 JSON and human-readable outputs
* 📚 Built for educational, research, and clinical support purposes

---

## 🛠️ How It Works

1. 📝 **Input** a variant:

   * Example: `chr9:136149229 G>A`

2. 📊 Returns data like:

   * Which **gene** is affected (`CDKN2A`)
   * How the **protein** is changed (Arginine → Histidine)
   * Type of mutation (**missense variant** = protein is altered)

3. 💡 **Displays an human readable and undrstandable interpretation** like:

   > “This variant changes the CDKN2A gene and may alter the protein’s behavior. Further clinical analysis may be needed.”

---

## 📥 Example Input

```json
{
  "chromosome": "9",
  "position": "136149229",
  "reference": "G",
  "alternate": "A"
}
```

---

## 📤 Example Output

```json
{
  "gene": "CDKN2A",
  "most_severe_consequence": "missense_variant",
  "amino_acids": "R/H",
  "protein_position": 24,
  "summary": "This variant affects the CDKN2A gene and causes an amino acid change from Arginine (R) to Histidine (H)."
}
```

---

## ⚙️ Installation

```bash
git clone https://github.com/codynego/genetic-variant-annotation-tool.git
cd genetic-variant-annotation-tool
pip install -r requirements.txt
```

---

## 🧪 Usage

### Command line:

```bash
python annotator.py --chr 9 --pos 136149229 --ref G --alt A
```

### Output:

```bash
Gene: CDKN2A
Effect: missense_variant
Protein change: R → H at position 24
Summary: This may affect protein function.
```

---

## 🧰 Built With

* [Python](https://www.python.org/)
* [Ensembl REST API](https://rest.ensembl.org/)
* [Requests](https://docs.python-requests.org/)
* Optional:  Streamlit (for a web app interface)

---

## 📌 Why This Matters

Mutations in our DNA can lead to diseases like cancer, but not all mutations are harmful. This tool helps you identify **what changed**, **where it changed**, and **what it might mean** — helping researchers, developers, and clinicians make more informed decisions.

---

## 🙋 Who Is It For?

* 👩‍🔬 Researchers studying human genetics
* 🧑‍⚕️ Clinicians investigating patient mutations
* 👨‍💻 Developers building genetic tools
* 🧑‍🎓 Students learning bioinformatics

---

## 🧠 Roadmap Ideas

* [ ] Add pathogenicity prediction (ClinVar/gnomAD integration)
* [ ] Add web UI (Streamlit/Flask)
* [ ] Export report as PDF/CSV
* [ ] Support batch annotation

---

## 🤝 Contributing

Contributions are welcome! Whether you're adding features, fixing bugs, or improving documentation, feel free to open a PR.

---

## 📜 License

MIT License. Feel free to use and adapt the project.

---

## ✨ Acknowledgments

* [Ensembl](https://www.ensembl.org) for the free and powerful variant annotation API.
* [OpenAI](https://openai.com) for guidance on explanation and communication.

---