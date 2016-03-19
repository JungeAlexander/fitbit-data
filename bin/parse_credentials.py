def parse_client_credentials(client_id_secret_file):
    client_id = client_secret = None
    with open(client_id_secret_file, 'r') as fhandle:
        for line in fhandle:
            line_split = line.split('=')
            if len(line_split) != 2:  # skip lines not following 'key = value' scheme
                continue
            k, v = [x.strip() for x in line_split]
            if k == 'id':
                client_id = v
            elif k == 'secret':
                client_secret = v
    if not client_id:
        raise IOError('Could not read client id from file {}.'.format(client_id_secret_file))
    if not client_secret:
        raise IOError('Could not read client secret from file {}.'.format(client_id_secret_file))
    return client_id, client_secret
        
def parse_tokens(access_refresh_token_file):
    access_token = refresh_token = None
    with open(access_refresh_token_file, 'r') as fhandle:
        for line in fhandle:
            line_split = line.split('=')
            if len(line_split) != 2:  # skip lines not following 'key = value' scheme
                continue
            k, v = [x.strip() for x in line_split]
            if k == 'ACCESS_TOKEN':
                access_token = v
            elif k == 'REFRESH_TOKEN':
                refresh_token = v
    if not access_token:
        raise IOError('Could not read access token from file {}.'.format(access_refresh_token_file))
    if not refresh_token:
        raise IOError('Could not read refresh token from file {}.'.format(access_refresh_token_file))
    return access_token, refresh_token