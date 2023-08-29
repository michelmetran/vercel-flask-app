# Vercel

Em maio de 2022 passei a estudar alternativas ao Heroku.
Consegui fazer o _deploy_ de uma aplicação Flask na Vercel

- [How to deploy a Python/Flask App to Vercel](https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k)

<br>

---

### Vercel CLI

Para fazer **_deploy_** de aplicações usando o Vercel, é recomendado ter o [Vercel CLI](https://vercel.com/cli) instalado!
Inicialmente vi qual o **npm** que eu tinha e o **node**.
E para isso é preciso dar o comando abaixo

```
npm --version
node --version
```

Na tentativa de instalar o Vercel CLI, deu um erro sobre o _Node_. É preciso que ele tenha, no mínimo, a versão 12!
[DigitalOcean: Como instalar o Node.js no Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04-pt)

Para instalar o npm, se eventualmente não tenha instalado...

```
sudo apt install npm
npm --version
```

<br>

Para instalar o Vercel CLI, usei o comando abaixo.

```
yarn global add vercel
```

<br>

---

### _Deploy_

Consegui fazer o deploy via _push_ e também via comando `vercel`.
É necessário explicitar a localização do arquivo, usando um `vercel.json` com o seguinte conteúdo.

```json
{
  "version": 2,
  "builds": [
    { "src": "src/index.py", "use": "@vercel/python" },
    { "src": "data/*.json", "use": "@vercel/static" }
  ],
  "routes": [{ "src": "/(.*)", "dest": "src/index.py" }]
}
```

<br>

---

### Problemas

Notei que se tiver `psycopg2` no _requirements.txt_ dá ruim!
