USERS_LIST = [
    {
        "id": 8538628,
        "name": "Aagneya Joshi",
        "email": "joshi_aagneya@mante-barrows.example",
        "gender": "female",
        "status": "inactive",
    },
    {
        "id": 8538626,
        "name": "Chaitan Banerjee",
        "email": "chaitan_banerjee@bednar.example",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8538625,
        "name": "Pres. Sarada Dutta",
        "email": "sarada_dutta_pres@macejkovic-lebsack.example",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8538622,
        "name": "Pres. Mina Jain",
        "email": "jain_pres_mina@bruen.test",
        "gender": "female",
        "status": "inactive",
    },
    {
        "id": 8538620,
        "name": "Gov. Harinakshi Kaniyar",
        "email": "kaniyar_gov_harinakshi@harber-mertz.example",
        "gender": "female",
        "status": "inactive",
    },
    {
        "id": 8538619,
        "name": "Datta Rana",
        "email": "rana_datta@denesik-breitenberg.test",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8538617,
        "name": "Chitrangada Ganaka",
        "email": "ganaka_chitrangada@little-haag.test",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8538615,
        "name": "Fr. Daksha Bhattacharya",
        "email": "fr_bhattacharya_daksha@wilderman-ernser.example",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8538614,
        "name": "Bheeshma Bhattathiri CPA",
        "email": "bhattathiri_cpa_bheeshma@kuhic.test",
        "gender": "female",
        "status": "active",
    },
    {
        "id": 8538613,
        "name": "Rep. Chandraayan Iyer",
        "email": "iyer_rep_chandraayan@block.test",
        "gender": "male",
        "status": "active",
    },
]


def get_user_by_id(user_id):
    for user in USERS_LIST:
        if user["id"] == int(user_id):
            return user
    return None
