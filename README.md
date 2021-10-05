# weird_proxies_ctf

Insiperd by [https://github.com/GrrrDog/weird_proxies](https://github.com/GrrrDog/weird_proxies)

## Installation
- `docker-compose build`
- `docker-compose up`
- task access `http://localhost:8081/`

## Steps
1. In index.html find path `/wiki/`
2. Exploit SSRF via misconfigured ProxyPass
3. 