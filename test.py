from config import config

if __name__ == '__main__':
    proxy_sites = config.proxy_sites()
    print(len(proxy_sites))
