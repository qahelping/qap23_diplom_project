def prepare_header(gores_token):
    return {
        "Authorization": f"Bearer {gores_token}",
        "Accept": "application/json",
        "Content-type": "application/json",
    }


class HttpClient:
    pass
