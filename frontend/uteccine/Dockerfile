# Imagen base de Node.js
FROM node:14-alpine

# Directorio de trabajo de la aplicación
WORKDIR /app

# Copiar los archivos necesarios para instalar las dependencias
COPY package*.json ./

# Instalar las dependencias de la aplicación
RUN npm install

# Copiar el resto de los archivos de la aplicación
COPY . .

# Compilar la aplicación para producción

RUN npm install vue-router
RUN npm install axios
RUN npm install vuex
RUN npm run build

# Exponer el puerto 8080
EXPOSE 8080

# Comando para iniciar la aplicación
CMD [ "npm", "run", "serve" ]


