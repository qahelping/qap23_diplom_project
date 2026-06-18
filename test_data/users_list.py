USERS_LIST = [
    {
        "id": 8512096,
        "name": "Adityanandana Guneta",
        "email": "guneta_adityanandana@rutherford-schuster.example",
        "gender": "male",
        "status": "active",
    },
    {
        "id": 8512093,
        "name": "Ghanshyam Namboothiri",
        "email": "namboothiri_ghanshyam@oreilly.example",
        "gender": "female",
        "status": "active",
    },
    {
        "id": 8512092,
        "name": "Gitanjali Chattopadhyay",
        "email": "gitanjali_chattopadhyay@christiansen.example",
        "gender": "male",
        "status": "inactive",
    },
    {
        "id": 8512091,
        "name": "Aslesha Joshi",
        "email": "aslesha_joshi@hamill-nienow.example",
        "gender": "male",
        "status": "active",
    },
    {
        "id": 8512090,
        "name": "Som Dutta",
        "email": "som_dutta@jast-cassin.example",
        "gender": "female",
        "status": "inactive",
    },
    {
        "id": 8512089,
        "name": "Ashlesh Tagore",
        "email": "tagore_ashlesh@hudson.test",
        "gender": "male",
        "status": "active",
    },
    {
        "id": 8512088,
        "name": "Puneet Bharadwaj",
        "email": "bharadwaj_puneet@bosco.example",
        "gender": "female",
        "status": "inactive",
    },
    {
        "id": 8512087,
        "name": "Mohini Jain CPA",
        "email": "mohini_jain_cpa@bednar.test",
        "gender": "female",
        "status": "active",
    },
    {
        "id": 8512086,
        "name": "Bakula Dubashi Sr.",
        "email": "bakula_sr_dubashi@dibbert.test",
        "gender": "male",
        "status": "active",
    },
    {
        "id": 8512085,
        "name": "Vasudeva Shah",
        "email": "shah_vasudeva@howell-daniel.example",
        "gender": "female",
        "status": "inactive",
    },
]


def get_user_by_id(user_id):
    for user in USERS_LIST:
        if user["id"] == int(user_id):
            return user
    return None
