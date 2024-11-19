-- Crear tabla usuarios
CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  correo VARCHAR(255) UNIQUE NOT NULL,
  contraseña VARCHAR(255) NOT NULL,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla eventos
CREATE TABLE eventos (
  id SERIAL PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  descripcion TEXT NOT NULL,
  fecha DATE NOT NULL,
  hora TIME NOT NULL,
  ubicacion VARCHAR(255) NOT NULL,
  capacidad INTEGER NOT NULL,
  precio DECIMAL(10, 2) NOT NULL,
  imagen VARCHAR(255),
  creado_por INTEGER REFERENCES usuarios(id)
);

-- Crear tabla categorias_eventos
CREATE TABLE categorias_eventos (
  id SERIAL PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  descripcion TEXT NOT NULL
);

-- Crear tabla eventos_categorias
CREATE TABLE eventos_categorias (
  id SERIAL PRIMARY KEY,
  evento_id INTEGER REFERENCES eventos(id),
  categoria_id INTEGER REFERENCES categorias_eventos(id)
);

-- Crear tabla compras
CREATE TABLE compras (
  id SERIAL PRIMARY KEY,
  usuario_id INTEGER REFERENCES usuarios(id),
  evento_id INTEGER REFERENCES eventos(id),
  fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  cantidad INTEGER NOT NULL,
  total DECIMAL(10, 2) NOT NULL
);

-- Crear tabla entradas
CREATE TABLE entradas (
  id SERIAL PRIMARY KEY,
  compra_id INTEGER REFERENCES compras(id),
  numero INTEGER NOT NULL,
  codigo_barras VARCHAR(255) NOT NULL
);