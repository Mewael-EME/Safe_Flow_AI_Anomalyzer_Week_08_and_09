def convert_ip_to_int(ip):
    try:
        return int(float(ip))
    except (ValueError, TypeError):
        return None
