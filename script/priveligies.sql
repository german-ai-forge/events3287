-- Crear usuario 'eventos_usuario'
CREATE ROLE eventos_usuario WITH PASSWORD 'contraseña_segura';

-- Asignar privilegios de lectura y escritura
GRANT SELECT, INSERT, UPDATE ON TABLE usuarios TO eventos_usuario;
GRANT SELECT, INSERT ON TABLE eventos TO eventos_usuario;
GRANT SELECT ON TABLE categorias_eventos TO eventos_usuario;
GRANT SELECT ON TABLE eventos_categorias TO eventos_usuario;
GRANT SELECT, INSERT ON TABLE compras TO eventos_usuario;
GRANT SELECT ON TABLE entradas TO eventos_usuario;