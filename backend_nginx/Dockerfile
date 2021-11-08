FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN mkdir /usr/share/nginx/imgs/
COPY imgs/ /usr/share/nginx/imgs/
COPY public/ /usr/share/nginx/html/
# TODO: change flag path if need
COPY flag /usr/share/nginx/
RUN chmod -R 777 /usr/share/nginx/
RUN chmod 777 /usr/share/nginx/