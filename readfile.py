from brutils import cpf, cnpj
import pandas as pd
import csv


def read_file(file):

    header = ["cpf", "private", "incompleto", "data_da_ultima_compra", "ticket_medio",
              "ticket_da_ultima_compra", "loja_mais_frequente", "loja_da_ultima_compra"]

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=" ",
                                fieldnames=header, skipinitialspace=True)

        data = [row for row in reader]

        df = pd.DataFrame(data[1:])

        df = df.replace(',', '.', regex=True)

        df = df.replace('NULL', pd.NA)

        df["ticket_medio"] = pd.to_numeric(
            df["ticket_medio"], errors='coerce')

        df["ticket_da_ultima_compra"] = pd.to_numeric(
            df["ticket_da_ultima_compra"], errors='coerce')

        df["cpf_valido"] = df["cpf"].apply(
            lambda x: cpf.validate(cpf.sieve(x)) if pd.notnull(x) else False)

        df["loja_mais_frequente_valido"] = df["loja_mais_frequente"].apply(
            lambda x: cnpj.validate(cnpj.sieve(x)) if pd.notnull(x) else False)

        df["loja_da_ultima_compra_valido"] = df["loja_da_ultima_compra"].apply(
            lambda x: cnpj.validate(cnpj.sieve(x)) if pd.notnull(x) else False)

        df["data_da_ultima_compra"] = pd.to_datetime(
            df["data_da_ultima_compra"], format='%Y-%m-%d', errors='coerce')

        df["cpf"] = df["cpf"].str.replace(
            '.', '', regex=True).str.replace('-', '', regex=True)

        df["loja_mais_frequente"] = df["loja_mais_frequente"].str.replace(
            '.', '', regex=True).str.replace('-', '', regex=True).str.replace('/', '', regex=True)

        df["loja_da_ultima_compra"] = df["loja_da_ultima_compra"].str.replace(
            '.', '', regex=True).str.replace('-', '', regex=True).str.replace('/', '', regex=True)

        df = df.astype({
            "private": int,
            "incompleto": int,
        })

        return df
