from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import Connection, text
from sqlalchemy.exc import SQLAlchemyError
import logging

TAILLE_LOT = 1000

load_dotenv()

def valeur_texte(valeur):
    """Transforme une valeur CSV manquante en None."""

    if pd.isna(valeur):
        return None

    texte = str(valeur).strip()

    if texte == "":
        return None

    return str(texte)


def valeur_entier(valeur):
    """Convertit une valeur en entier ou None."""

    if pd.isna(valeur):
        return None
    
    return int(valeur)


def valeur_decimal(valeur):
    """Convertit une valeur monétaire en Decimal ou None."""

    if pd.isna(valeur):
        return None

    return float(str(valeur))


def valeur_booleen(valeur):
    """Convertit oui/non en booléen Python."""

    texte = str(valeur).strip().lower()

    if texte == "oui":
        return True

    if texte == "non":
        return False

    raise ValueError(
        f"Valeur booléenne inattendue : {valeur!r}"
    )
    
def inserer_lots(conn: Connection, nom_table: str, requete: str, lignes, rejets,):
    """
    Insère les données par lots de 500 lignes.

    En fonctionnement normal, toutes les insertions sont réalisées
    par lots.

    Si PostgreSQL refuse exceptionnellement un lot, un savepoint
    permet d'annuler uniquement ce lot. Les lignes de ce lot sont
    alors testées séparément afin d'identifier précisément celles
    qui doivent être inscrites dans le fichier des rejets.
    """

    instruction = text(requete)

    nombre_insere = 0
    nombre_rejete = 0

    for debut in range(0, len(lignes), TAILLE_LOT):
        lot = lignes[debut:debut + TAILLE_LOT]

        try:
            with conn.begin_nested():
                conn.execute(instruction, lot)

            nombre_insere += len(lot)

        except SQLAlchemyError as erreur_lot:
            logging.warning(
                "%s : échec d'un lot de %d lignes, "
                "recherche des lignes fautives.",
                nom_table,
                len(lot),
            )

            for ligne in lot:
                try:
                    with conn.begin_nested():
                        conn.execute(
                            instruction,
                            [ligne],
                        )

                    nombre_insere += 1

                except SQLAlchemyError as erreur_ligne:
                    rejet = {
                        "table": nom_table,
                        **ligne,
                        "motif_rejet": str(
                            getattr(
                                erreur_ligne,
                                "orig",
                                erreur_ligne,
                            )
                        ),
                    }

                    rejets.append(rejet)
                    nombre_rejete += 1

                    logging.error(
                        "%s : ligne rejetée : %s",
                        nom_table,
                        erreur_ligne,
                    )

    return nombre_insere, nombre_rejete