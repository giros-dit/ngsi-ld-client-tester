FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 8083
ENTRYPOINT ["nginx","-g","daemon off;"]