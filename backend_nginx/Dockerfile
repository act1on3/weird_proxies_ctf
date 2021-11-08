FROM nginx:1.20.1-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN mkdir /usr/share/nginx/imgs/
COPY imgs/ /usr/share/nginx/imgs/
COPY public/ /usr/share/nginx/html/
RUN chmod -R 777 /usr/share/nginx/
RUN chmod 777 /usr/share/nginx/