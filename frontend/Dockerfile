# production stage
FROM node:19-alpine3.15 as build-stage
# make the 'app' folder the current working directory

WORKDIR /app
# copy both 'package.json' and 'package-lock.json'
COPY package*.json ./
# install project dependencies
RUN npm i
# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
# build app for production with minification
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]