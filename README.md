# Evaluación Técnica: Backend

Este proyecto es una aplicación web desarrollada con Django que tiene como objetivo gestionar usuarios, productos y categorías, implementando una serie de características y requisitos.

## Requerimientos

El proyecto cumple con los siguientes requisitos:

1. **Gestión de Usuarios:**

   - Registro de usuarios.
   - Autenticación de usuarios.
   - Aprobación por parte del administrador de Django para que los usuarios puedan acceder a funciones adicionales.

2. **Gestión de Productos:**
   - Almacenamiento de productos con información que incluye nombre, estado, categorías e imágenes.
   - Acceso a la información básica de productos (nombre y estado) para usuarios no registrados.
   - Acceso completo a información detallada de productos (nombre, estado, categorías e imágenes) para usuarios registrados y aprobados.
   - Capacidad para que usuarios aprobados modifiquen y eliminen productos.
   - Filtros de búsqueda en la lista de productos por nombre, estado y categorías.

## Modelo de Negocios

El modelo de negocios implementado en el proyecto se basa en las siguientes reglas:

1. No es necesario el registro para visualizar el nombre y estado de un producto.
2. El registro es obligatorio para acceder a información detallada de productos, incluyendo nombre, estado, categorías e imágenes.
3. Se requiere la aprobación de un usuario por parte del administrador para realizar modificaciones o eliminaciones de productos.
4. La lista de productos incluye filtros de búsqueda por nombre, estado y categorías, y solo muestra productos aprobados.

## Cómo Probar el Proyecto

1. Accede a la carpeta `backend`.
2. Siga las instrucciones contenidas en el archivo README para un correcto despliegue.
