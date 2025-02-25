# Используем базовый образ nginx
FROM nginx:alpine

# Копируем HTML файл в директорию nginx
COPY index.html /usr/share/nginx/html/index.html
