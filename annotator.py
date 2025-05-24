import requests, sys
from io import StringIO

def read_vcf(path):
    with open(path, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.strip().split('\t')
            chrom, pos, id_, ref, alt, qual, filter_, info = fields[:8]
            yield {"CHROM": chrom, "POS": pos, "ID": id_, "REF": ref, "ALT": alt, "QUAL": qual, "FILTER": filter_, "INFO": info}

# def get_rsid(chrom, pos, ref, alt):    
#     #url = f"https://rest.ensembl.org/vep/human/region/{chrom}:{pos}{ref}/{alt}"
#     url = f"https://api.genohub.org/v1/variants/{chrom}-{pos}-{ref}-{alt}"
#     headers = {"Accept": "application/json"}

#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         try:
#             rsid = data[0].get('id', None)
#             return rsid if rsid else "No rsID found"
#         except (IndexError, KeyError):
#             return "No rsID found"
#     else:
#         return f"Error {response.status_code}: {response.text}"

def get_rsid(chrom, pos, ref, alt):
    server = "https://rest.ensembl.org"
    ext = "/vep/homo_sapiens/region"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    variant = f"{chrom} {pos} {ref} {alt}"
    data = {"variants": [variant]}
    
    response = requests.post(f"{server}{ext}", headers=headers, json=data)
    
    if not response.ok:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
    decoded = response.json()
    if decoded and 'id' in decoded[0]:
        return decoded[0]['id']
    else:
        return "rsID not found"

def annotate_variant(rsid):
    server = "https://rest.ensembl.org"
    ext = f"/vep/human/id/{rsid}?"
    
    response = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
    
    if not response.ok:
        print(f"Error: {response.status_code} - {response.text}")
        return None
        
    decoded = response.json()
    return (decoded)


# def main ():
#     variant = read_vcf("dummy_test.vcf")
#     for v in variant:
#     #     print(v)
#     #     #print(get_rsid(1, v["POS"], v["REF"], v["ALT"]))
#     #     # print(v["CHROM"], v["POS"], v["ID"], v["REF"], v["ALT"], v["QUAL"], v["FILTER"], v["INFO"])

#     variant = annotate_variant("rs372634384")
#     print(variant)

if __name__ == "__main__":
    main()
    # if len(sys.argv) != 2:
    #     print("Usage: python annotator.py <path_to_vcf>")
    #     sys.exit(1)

    # vcf_path = sys.argv[1]
    # read_vcf(vcf_path)