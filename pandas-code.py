import pandas as pd

url = "https://pinkanakorn.gdcatalog.go.th/dataset/a1daf72e-91d0-4583-ba2a-6939b9f79f99/resource/abb21ea2-f187-494e-bd8b-a1082805c39d/download/pda_11_03-.csv"

pd.read_csv(url, encoding='thai')