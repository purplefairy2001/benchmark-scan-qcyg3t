def authenticate(token):
    """Authenticate using the provided token."""
    if not token:
        raise ValueError('Token must not be empty')
    return {'authenticated': True, 'token_prefix': token[:4]}
